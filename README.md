# HIPE-OCRepair 2026 – Evaluation

This repository contains the official evaluation toolkit for the HIPE-OCRepair 2026 competition, including:

- the test data used for the evaluation
- the system submissions
- the [HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) (as a Python package) and the evaluation scripts used to score system outputs
- the evaluation results
- a Makefile to run the whole evaluation process

The repository is designed to ensure transparent and reproducible evaluation of all submitted systems.

**For more information, also have a look at:**

- :books: [ HIPE evaluation campaigns](https://hipe-eval.github.io)
- :link: [HIPE-OCRepair 2026 Website](https://hipe-eval.github.io/HIPE-OCRepair-2026/)
- :checkered_flag: HIPE-OCRepair-2026 results on the [website](https://hipe-eval.github.io/HIPE-OCRepair-2026/results)
- :open_file_folder: HIPE-OCRepair-2026 [data set releases](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases)
- :low_brightness: HIPE-OCRepair-2026 [baseline](https://github.com/hipe-eval/HIPE-OCRepair-2026-baseline)

### Task

The shared task focuses on OCR post-correction for historical documents. Participants
develop systems that automatically correct OCR errors in historical text paragraphs. The
correction does not happen on a line-by-line basis but on the whole paragraph, allowing for more global corrections.

System outputs are evaluated against gold-standard reference data using the official
evaluation scorer that includes some normalization to the reference and hypothesis texts.

### Repository structure

```bash
data/
  reference/              # Gold-standard reference JSONL files (one per dataset/split/language)
  reference-dummy/        # Synthetic reference files for dry-run testing
  systems/                # Participant submission JSONL files
  systems-dummy/          # Dummy baseline files (generated; not committed)
lib/
  score_one.py                # Score a single hypothesis against its reference
  build_rankings.py           # Aggregate per-run scores into ranked TSV files
  build_results_md.py         # Render TSV rankings as a Markdown results page
  create_dummy_baselines.py   # Generate dummy baseline hypotheses from reference files
  competition_config.json     # Official competition test sets and design weights
  teams.json                  # Team name → institution mapping
results/                      # Real pipeline output (regenerated)
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

The `requirements.txt` installs the
[HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) during the
development phase of this repository directly from GitHub. To update it to the latest version:

```bash
pip install --upgrade -r requirements.txt
```

#### To run the evaluation

```bash
make eval-full          # Score submissions, build rankings and results MD
make eval-full-refresh  # Remove all derived files and re-run from scratch
```

Run `make` to see all available targets.

### Submission format

Submission files are JSONL files (one JSON object per line). Each record must contain the following fields:

```json
{
  "document_metadata": {
    "document_id": "unique-id",
    "primary_dataset_name": "unversioned dataset name as it appears in the reference file (e.g., icdar2017, impresso-snippets, dta19-l0)",
    "language": "Language code (e.g., en, de, fr)"
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
A submission filename is formed by prepending your team name and appending a run suffix to the reference filename:

```
<teamname>_<reference-stem>_run<N>.jsonl
```

where `<reference-stem>` is the reference file's name without the `.jsonl` extension, and `run<N>` ∈ `{run1, run2, run3}`.

Expanded, this gives:

```
<teamname>_hipe-ocrepair-bench_<bench-version>_<dataset>_<dataset-version>_<split>_<language>_run<N>.jsonl
```

- `<teamname>`: lowercase alphanumeric characters and hyphens only — **no underscores**
- `<bench-version>`: benchmark version, currently `v0.9`
- `<dataset>_<dataset-version>`: exact versioned dataset identifier — see table below
- `<split>`: `test`
- `<language>`: `en`, `de`, or `fr`
- `run<N>`: `run1`, `run2`, or `run3` — up to 3 runs per reference file per team

The exact versioned dataset identifiers are:

| Source dataset    | Versioned dataset identifier | Language(s) |
| ----------------- | ---------------------------- | ----------- |
| icdar2017         | `icdar2017_v1.1`             | en, fr      |
| impresso-snippets | `impresso-snippets_v1.0`     | de, en, fr  |
| impresso-nzz      | `impresso-nzz_v1.1`          | de          |
| dta19 (level 0)   | `dta19-l0_v0.1`              | de          |
| dta19 (level 1)   | `dta19-l1_v0.1`              | de          |
| dta19 (level 2)   | `dta19-l2_v0.1`              | de          |
| overproof         | `overproof-combined_v1.0`    | en          |

Example: `myteam_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_dev_de_run1.jsonl`

All submission files will be placed in `data/systems/`.

### Dry-run with dummy data

Before real submissions arrive, you can test the full pipeline end-to-end using synthetic baselines generated from the reference files in `data/reference-dummy/`.

The dummy pipeline is **fully isolated** from the real pipeline: it reads from `data/reference-dummy/` and writes to `results-dummy/` and `HIPE_OCRepair_2026_evaluation_results_dummy.md`. Running it never touches `results/` or the real results file.

```bash
make eval-full-dummy   # clean → generate baselines → score → rankings → MD
```

Step by step:

```bash
make baselines-dummy   # Generate dummy baselines in data/systems-dummy/
make score-dummy       # Score all files in data/systems-dummy/
make rankings-dummy    # Build per-test-set and overall ranking TSVs in results-dummy/system-rankings/
make results-md-dummy  # Render HIPE_OCRepair_2026_evaluation_results_dummy.md
make clean-dummy       # Remove all dummy-pipeline outputs and generated baselines
```

To test against a different set of reference files:

```bash
make eval-full-dummy REFERENCE_DIR_DUMMY=path/to/your/references
```

**Baseline strategies** are generated automatically, including exact-copy and corruption-based variants. Depending on the command used, these may include:

- `perfect_*_run1.jsonl` — perfect baseline (copies ground truth unchanged; expected cMER = 0)
- `no-correction_*_run1.jsonl` — identity baseline (copies OCR input unchanged; expected cMER ≈ raw OCR error rate)
- `char-swaps-*` — corruption baseline that swaps a specified proportion of adjacent character pairs in the ground truth
- `word-swaps-*` — corruption baseline that swaps a specified proportion of adjacent word pairs in the ground truth

### Metrics and rankings

Primary metrics are based on **character-level Match Error Rate (cMER)**:

$$\text{cMER} = \frac{S + D + I}{H + S + D + I}$$

where \(H\) = hits, \(S\) = substitutions, \(D\) = deletions, and \(I\) = insertions on the level of characters. Unlike standard CER/WER, MER is bounded in \([0,1]\), because insertions are included in the denominator.

Before scoring in normalized setup, texts are normalized as follows:

- lowercased
- punctuation and other non-word characters replaced by spaces
- underscores replaced by spaces
- repeated whitespace collapsed

Evaluation is therefore **case-insensitive** and **punctuation-insensitive**, but still sensitive to accented characters (for example, `é` and `e` remain different).

A cMER of 0.05 means that the hypothesis and reference differ by 5% at the character level.

#### Aggregation levels

Each test dataset consists of a set of **transcription units**. All metrics are first computed at the level of individual transcription units and then aggregated.

For each dataset, the scorer reports:

- **`cmer_micro`**: character-level MER obtained by summing alignment counts across all transcription units in the dataset and computing cMER once from the summed totals within a test set
- **`cmer_macro`**: arithmetic mean of the transcription-unit-level cMER scores within a test set
- **`wmer_micro`** and **`wmer_macro`** are computed in the same way as cmer_micro and cmer_macro, but using word-level alignments produced by jiwer.process_words(...) after normalization. Here, hits, substitutions, deletions, and insertions are counted over aligned word sequences rather than character sequences.

In other words:

- **micro** aggregation gives more weight to longer transcription units in a test set
- **macro** aggregation gives equal weight to each transcription unit in a test set

#### Preference-based secondary metrics

In addition to MER, the scorer reports metrics that compare a system output to the original OCR hypothesis on each transcription unit:

- **`pref_score_cmer_macro`**: mean preference score based on cMER
- **`pref_score_wmer_macro`**: mean preference score based on wMER

For each transcription unit, the preference score is:

- `1` if the system is better than the raw OCR
- `0` if both are equal
- `-1` if the system is worse than the raw OCR

These scores are then averaged across transcription units, so they are **macro** metrics.

#### Metric definitions used in the reports

The evaluation reports show the following metrics:

- **`cmer_micro`**: micro-averaged character-level Match Error Rate
- **`cmer_macro`**: macro-averaged character-level Match Error Rate
- **`wmer_micro`**: micro-averaged word-level Match Error Rate
- **`wmer_macro`**: macro-averaged word-level Match Error Rate
- **`pref_score_cmer_macro`**: macro-averaged preference score comparing system cMER to raw OCR cMER
- **`pref_score_wmer_macro`**: macro-averaged preference score comparing system wMER to raw OCR wMER

At the transcription-unit level, MER is defined as:

$$
\mathrm{MER} = \frac{S + D + I}{H + S + D + I}
$$

where \(H\) = hits, \(S\) = substitutions, \(D\) = deletions, and \(I\) = insertions.

For a dataset with transcription units \(i = 1, \dots, N\):

$$
\mathrm{cMER}_{\mathrm{macro}} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{cMER}_{i}
$$

$$
\mathrm{wMER}_{\mathrm{macro}} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{wMER}_{i}
$$

$$
\mathrm{cMER}_{\mathrm{micro}} = \frac{\sum_{i} S_{i} + \sum_{i} D_{i} + \sum_{i} I_{i}}{\sum_{i} H_{i} + \sum_{i} S_{i} + \sum_{i} D_{i} + \sum_{i} I_{i}}
$$

$$
\mathrm{wMER}_{\mathrm{micro}} = \frac{\sum_{i} S_{i} + \sum_{i} D_{i} + \sum_{i} I_{i}}{\sum_{i} H_{i} + \sum_{i} S_{i} + \sum_{i} D_{i} + \sum_{i} I_{i}}
$$

The preference score for one transcription unit is:

$$
\mathrm{pref}(i) =
\begin{cases}
1 & \text{if the system score is better than the raw OCR score} \\
0 & \text{if both scores are equal} \\
-1 & \text{if the system score is worse than the raw OCR score}
\end{cases}
$$

The reported preference metrics are macro averages over transcription units:

$$
\text{pref\_score\_cmer\_macro} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{pref}_{\text{cmer}}(i)
$$

$$
\text{pref\_score\_wmer\_macro} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{pref}_{\text{wmer}}(i)
$$

#### Per-dataset scores and overall averages

Scoring is performed **per dataset** (using `primary_dataset_name` as the grouping key). In the output of the scorer, these dataset-level results are stored under `fold_scores`.

The overall results in `averaged_scores` are then computed as the **unweighted mean across datasets** of the corresponding dataset-level scores.

This means that:

- `fold_scores[dataset]["cmer_micro"]` is the **micro cMER within that dataset**
- `averaged_scores["cmer_micro"]` is the **mean of the dataset-level micro cMER values**

So the overall average is **not** a single global micro-average over all transcription units from all datasets combined. Instead, it is an equal-weight average over datasets.

#### Primary and secondary ranking criteria

The **primary ranking metric** is **`cmer_micro`**:

- lower is better
- computed separately for each dataset
- longer transcription units contribute more within a dataset

The **secondary ranking metric** is **`pref_score_cmer_macro`**:

- higher is better
- measures how consistently a system improves over the raw OCR input across transcription units
- each transcription unit contributes equally

#### Official competition ranking across test sets

The scorer outputs per-dataset scores, including `cmer_micro` for each dataset.  
The **official competition ranking** is computed separately from these scorer outputs as a **weighted mean of per-test-set `cmer_micro`** across the 8 official test sets.

The weighting scheme is defined by the competition design and is **not** the same as the scorer’s internal `averaged_scores`, which uses an unweighted mean across datasets.

The weights are chosen so that the language-level contributions remain balanced:

- for **English** and **French**, each language score is based on **two test sets**, each with weight **1**
- for **German**, the score is based on **four test sets**: `impresso-snippets` with weight **1**, and the three DTA test sets (`dta19-l0`, `dta19-l1`, `dta19-l2`) with weight **1/3** each

Thus, the three DTA test sets together contribute the same total weight as one other test set. This means that, for each language, the combined contribution is effectively based on **two equally weighted dataset groups**.

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| dta19-l0                       | de   | 1/3    |
| dta19-l1                       | de   | 1/3    |
| dta19-l2                       | de   | 1/3    |
| impresso-snippets              | de   | 1      |

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| `icdar2017`                    | en   | 1      |
| `impresso-snippets`            | en   | 1      |

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| icdar2017                      | fr   | 1      |
| impresso-snippets              | fr   | 1      |

`impresso-nzz` and `overproof-combined` datasets do not contribute to the official rankings because they have been released earlier to the public.

### Results

The evaluation results are available in [HIPE_OCRepair_2026_evaluation_results.md](HIPE_OCRepair_2026_evaluation_results.md) and on the [HIPE-OCRepair-2026 website](https://hipe-eval.github.io/HIPE-OCRepair-2026/results).

The **official competition ranking** is computed separately from the scorer outputs as a
**weighted mean of `cmer_micro`** across the official test sets. The secondary criterion
is the corresponding **weighted mean of `pref_score_cmer_macro`**.
The scorer reports simple averages across datasets. The official competition ranking
applies a separate weighted average across the official test sets, so that the three
German DTA splits do not collectively outweigh the other test sets.

#### Per-language rankings

In addition to the overall competition ranking, we report **per-language rankings** of submitted runs.

For a given language, the ranking is computed as a **weighted mean of per-test-set `cmer_micro`** over the official test sets for that language. The secondary criterion is the corresponding **weighted mean of `pref_score_cmer_macro`**.

This means in terms of unversioned datasets:

- for **English**, the language score is the mean over `icdar2017` and `impresso-snippets`
- for **French**, the language score is the mean over `icdar2017` and `impresso-snippets`
  - for **German**, the language score is computed from `impresso-snippets` with weight `1` and from `dta19-l0`, `dta19-l1`, and `dta19-l2` with weight `1/3` each

As in the overall ranking, these language-level rankings are based on weighted combinations of **per-test-set scores**. They should not be confused with the scorer’s internal notions of **micro** and **macro**, which refer to aggregation over transcription units within a dataset.
