# HIPE-OCRepair 2026 – Evaluation

This repository contains the official evaluation toolkit for the HIPE-OCRepair 2026 competition, including:
- the [HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) (as a submodule or python package) and the evaluation scripts used to score system outputs;
- the test data used for the evaluation;
- the system submissions;
- the evaluation results;
- a Makefile to run the whole evaluation process.

The repository is designed to ensure transparent and reproducible evaluation of all submitted systems.

**For more information, also have a look at:**

- :checkered_flag: HIPE-OCRepair-2026 results in [HIPE_OCRepair_2026_evaluation_results.md] and on the [website]([https://hipe-eval.github.io/HIPE-2022/results](https://hipe-eval.github.io/HIPE-OCRepair-2026/results)).
- :computer: [HIPE-OCRepair 2026](https://hipe-eval.github.io/HIPE-OCRepair-2026/);
- :open_file_folder: HIPE-OCRepair-2026 [data releases](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases);
- :low_brightness: HIPE-OCRepair-2026 [baseline]([https://github.com/hipe-eval/HIPE-2022-baseline](https://github.com/hipe-eval/HIPE-OCRepair-2026-baseline));
- :books: HIPE evaluation campaigns [zenodo community](https://zenodo.org/communities/hipe-eval/?page=1&size=20).

### Task

The  shared task focuses on OCR post-correction for historical documents. Participants develop systems that automatically correct OCR errors in historical text.

System outputs are evaluated against gold-standard reference data using the official evaluation scripts provided in this repository.

### Repository structure

```bash
evaluation/      # System outputs submitted by participants
data/            # Test datasets used for the evaluation
lib/             # Scripts to evaluate submission and prepare results aggregations
results/         # Evaluation results and rankings
```

### Installation

Clone the repository and install the required dependencies:

```bash
git clone --recurse-submodules git@github.com:impresso/HIPE-OCRepair-2026-eval.git
cd HIPE-OCRepair-2026-eval

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

( cd HIPE-OCRepair-scorer && pip install -r requirements.txt && python setup.py install )

# if submodule HIPE-OCRepair-scorer is updated, the following might be needed

git submodule update 
( cd HIPE-OCRepair-scorer && pip install -r requirements.txt && python setup.py install )
```

#### To run the evaluation

```bash
make eval-full   # Creates all evaluation steps
# in case you want to start from scratch and refresh all derived files
make eval-full-refresh
```





