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
  reference/     # Gold-standard reference JSONL files (one per dataset/split/language)
evaluation/
  system-responses/
    submitted/   # Participant submission JSONL files
lib/
  score_one.py          # Score a single hypothesis against its reference
  build_rankings.py     # Aggregate per-run scores into ranked TSV files
  build_results_md.py   # Render TSV rankings as a Markdown results page
  teams.json            # Team name → institution mapping
results/
  per-run/              # Per-submission scorer output JSON (regenerated, not committed)
  system-rankings/      # Per-dataset/split/language ranked TSV files
HIPE_OCRepair_2026_evaluation_results.md   # Final results page (generated)
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
make eval-full   # Creates all evaluation steps
# in case you want to start from scratch and refresh all derived files
make eval-full-refresh
```

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

### Results

The evaluation results are available in [HIPE_OCRepair_2026_evaluation_results.md](HIPE_OCRepair_2026_evaluation_results.md) and on the [HIPE-OCRepair-2026 website](https://hipe-eval.github.io/HIPE-OCRepair-2026/results).

Rankings are sorted by `cmer_macro` (Character Match Error Rate, macro-averaged; lower is better). The secondary sort key is `pref_score_cmer_macro` (higher is better).
