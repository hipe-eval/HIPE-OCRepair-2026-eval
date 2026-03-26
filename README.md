# HIPE-OCRepair 2026 – Evaluation

This repository contains the official evaluation toolkit for the HIPE-OCRepair 2026 competition, including:

- the [HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) (as a Python package) and the evaluation scripts used to score system outputs;
- the test data used for the evaluation;
- the system submissions;
- the evaluation results;
- a Makefile to run the whole evaluation process.

The repository is designed to ensure transparent and reproducible evaluation of all submitted systems.

**For more information, also have a look at:**

- :checkered_flag: HIPE-OCRepair-2026 results in [HIPE_OCRepair_2026_evaluation_results.md] and on the [website](<[https://hipe-eval.github.io/HIPE-2022/results](https://hipe-eval.github.io/HIPE-OCRepair-2026/results)>).
- :computer: [HIPE-OCRepair 2026](https://hipe-eval.github.io/HIPE-OCRepair-2026/);
- :open_file_folder: HIPE-OCRepair-2026 [data releases](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases);
- :low_brightness: HIPE-OCRepair-2026 [baseline](<[https://github.com/hipe-eval/HIPE-2022-baseline](https://github.com/hipe-eval/HIPE-OCRepair-2026-baseline)>);
- :books: HIPE evaluation campaigns [zenodo community](https://zenodo.org/communities/hipe-eval/?page=1&size=20).

### Task

The shared task focuses on OCR post-correction for historical documents. Participants develop systems that automatically correct OCR errors in historical text.

System outputs are evaluated against gold-standard reference data using the official evaluation scripts provided in this repository.

### Repository structure

```bash
data/
  reference/              # Gold-standard reference JSONL files (one per dataset/split/language)
  reference-dummy/        # Synthetic reference files for dry-run testing
evaluation/
  system-responses/
    submitted/            # Participant submission JSONL files
  system-responses-dummy/
    submitted/            # Dummy baseline files (generated; not committed)
lib/
  score_one.py                # Score a single hypothesis against its reference
  build_rankings.py           # Aggregate per-run scores into ranked TSV files
  build_results_md.py         # Render TSV rankings as a Markdown results page
  create_dummy_baselines.py   # Generate same/random baselines from reference files
  competition_config.json     # Official competition cells and design weights
  teams.json                  # Team name → institution mapping
results/                      # Real pipeline output (regenerated; not committed)
  per-run/
  system-rankings/
results-dummy/                # Dummy pipeline output (regenerated; not committed)
  per-run/
  system-rankings/
HIPE_OCRepair_2026_evaluation_results.md        # Final results page (generated)
HIPE_OCRepair_2026_evaluation_results_dummy.md  # Dummy results page (generated)
```

### Installation

Clone the repository and install the required dependencies:

```bash
git clone git@github.com:impresso/HIPE-OCRepair-2026-eval.git
cd HIPE-OCRepair-2026-eval

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The `requirements.txt` installs the [HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) directly from GitHub. To update it to the latest version:

```bash
pip install --upgrade -r requirements.txt
```

#### To run the evaluation

```bash
make eval-full          # Score submissions, build rankings and results MD
make eval-full-refresh  # Remove all derived files and re-run from scratch
```

Run `make` (or `make help`) to see all available targets.

### Submission format

Submission files are JSONL files (one JSON object per line). Each record must contain the following fields:

```json
{
  "document_metadata": {
    "document_id": "unique-id",
    "primary_dataset_name": "impresso-snippets"
  },
  "ground_truth": {
    "transcription_unit": "Reference transcription text"
  },
  "ocr_hypothesis": {
    "transcription_unit": "Original OCR text (as provided)"
  },
  "ocr_postcorrection_output": {
    "transcription_unit": "Your system's corrected text"
  }
}
```

**File naming convention:**

```
<teamname>_hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>_run<N>.jsonl
```

- `<teamname>`: lowercase alphanumeric characters and hyphens only — **no underscores**
- `<version>`, `<dataset>`, `<split>`, `<language>`: must match the corresponding reference file
- `run<N>`: `run1`, `run2`, or `run3` — up to 3 runs per reference file per team

Example: `myteam_hipe-ocrepair-bench_v0.9_impresso-snippets_dev_de_run1.jsonl`

Place submission files in `evaluation/system-responses/submitted/`.

### Dry-run with dummy data

Before real submissions arrive, you can test the full pipeline end-to-end using synthetic baselines generated from the reference files in `data/reference-dummy/`.

The dummy pipeline is **fully isolated** from the real pipeline: it reads from `data/reference-dummy/` and writes to `results-dummy/` and `HIPE_OCRepair_2026_evaluation_results_dummy.md`. Running it never touches `results/` or the real results file.

```bash
make eval-full-dummy   # clean → generate baselines → score → rankings → MD
```

Step by step:

```bash
make baselines-dummy   # Generate same/random baselines in evaluation/system-responses-dummy/submitted/
make score-dummy       # Score all files in evaluation/system-responses-dummy/submitted/
make rankings-dummy    # Build per-cell and overall ranking TSVs in results-dummy/system-rankings/
make results-md-dummy  # Render HIPE_OCRepair_2026_evaluation_results_dummy.md
make clean-dummy       # Remove all dummy-pipeline outputs and generated baselines
```

To test against a different set of reference files:

```bash
make eval-full-dummy REFERENCE_DIR_DUMMY=path/to/your/references
```

**Two baseline strategies** are generated automatically:

- `same_*_run1.jsonl` — identity baseline (copies OCR input unchanged; expected cMER ≈ raw OCR error rate)
- `random_*_run1.jsonl` — word-shuffle baseline (random word order; expected cMER ≈ 1)

These sanity-check that the scorer is working: `same` should score better than `random` on every cell.

### Metrics and rankings

All metrics are based on **Match Error Rate (MER)**:

$$\text{MER} = \frac{S + D + I}{H + S + D + I}$$

where H = hits, S = substitutions, D = deletions, I = insertions. Unlike standard CER/WER, MER is capped in [0, 1]. Evaluation is **case-insensitive** and **punctuation-insensitive** but sensitive to accented characters.

The **primary metric** is `cmer_micro` — micro-averaged character MER within each test cell (longer documents contribute more). Rankings are sorted by `cmer_micro` ascending (lower is better). The **secondary metric** is `pref_score_cmer_macro` (higher is better), which captures how consistently a system improves over the raw OCR input, unaffected by document length.

The **overall ranking** is a weighted mean of per-cell `cmer_micro` across the 8 official test cells. Design weights ensure equal influence per conceptual dataset unit: each non-DTA cell has weight 1; each of the three DTA cells (`dta19-l0`, `dta19-l1`, `dta19-l2`) has weight 1/3 so that the three together count as one unit.

| Cell | Dataset             | Lang | Weight |
| ---- | ------------------- | ---- | ------ |
| 1    | `icdar2017`         | en   | 1      |
| 2    | `icdar2017`         | fr   | 1      |
| 3    | `dta19-l0`          | de   | 1/3    |
| 4    | `dta19-l1`          | de   | 1/3    |
| 5    | `dta19-l2`          | de   | 1/3    |
| 6    | `impresso-snippets` | de   | 1      |
| 7    | `impresso-snippets` | en   | 1      |
| 8    | `impresso-snippets` | fr   | 1      |

`impresso-nzz` and `overproof-combined` have no competition test sets and do not contribute to the official rankings.

### Results

The evaluation results are available in [HIPE_OCRepair_2026_evaluation_results.md](HIPE_OCRepair_2026_evaluation_results.md) and on the [HIPE-OCRepair-2026 website](https://hipe-eval.github.io/HIPE-OCRepair-2026/results).

Rankings are sorted by `cmer_micro` (character MER, micro-averaged; lower is better). The secondary sort key is `pref_score_cmer_macro` (higher is better).
