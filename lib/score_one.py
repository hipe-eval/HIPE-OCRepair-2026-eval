#!/usr/bin/env python3
"""Score a single hypothesis JSONL file against its reference.

The reference file is derived from the hypothesis filename by:
  1. Stripping the _run<N> suffix
  2. Stripping the <teamname>_ prefix

Example:
    team1_hipe-ocrepair-bench_v0.9_impresso-snippets_masked-test_de_run1.jsonl
    -> hipe-ocrepair-bench_v0.9_impresso-snippets_test_de.jsonl

Usage:
    python lib/score_one.py \\
        --hypothesis evaluation/system-responses/submitted/team1_..._run1.jsonl \\
        --reference-dir data/reference/ \\
        --output results/per-run/team1_..._run1.json
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

from hipe_ocrepair_scorer import Evaluation, align_records


def setup_logging(log_file: Path | None = None) -> None:
    """Configure logging to file and stderr."""
    handlers = []

    # Console handler (stderr)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    handlers.append(console_handler)

    # File handler (if specified)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        )
        handlers.append(file_handler)

    logging.basicConfig(level=logging.DEBUG, handlers=handlers, force=True)


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                logging.error(f"{path} line {i}: {e}")
                sys.exit(1)
    return records


def derive_reference_stem(hypothesis_path: Path) -> str:
    """Derive reference file stem from a hypothesis filename.

    e.g. team1_hipe-ocrepair-bench_v0.9_impresso-snippets_masked-test_de_run1
      -> hipe-ocrepair-bench_v0.9_impresso-snippets_test_de
    """
    stem = hypothesis_path.stem
    stem = re.sub(r"_run\d+$", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"^[^_]+_", "", stem)
    stem = re.sub(r"_masked-test_", "_test_", stem, flags=re.IGNORECASE)
    return stem


def round_scores(obj: object, decimals: int = 4) -> object:
    if isinstance(obj, float):
        return round(obj, decimals)
    if isinstance(obj, (list, tuple)):
        return [round_scores(v, decimals) for v in obj]
    if isinstance(obj, dict):
        return {k: round_scores(v, decimals) for k, v in obj.items()}
    return obj


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Score a single hypothesis JSONL against its reference."
    )
    parser.add_argument("--hypothesis", required=True, help="Path to hypothesis JSONL.")
    parser.add_argument(
        "--reference-dir", required=True, help="Directory with reference JSONL files."
    )
    parser.add_argument("--output", required=True, help="Path to write JSON results.")
    parser.add_argument("--log-file", help="Path to write log output.")
    args = parser.parse_args()

    hyp_path = Path(args.hypothesis)
    ref_dir = Path(args.reference_dir)
    out_path = Path(args.output)
    log_file = Path(args.log_file) if args.log_file else None

    setup_logging(log_file)

    if not hyp_path.is_file():
        logging.error(f"Hypothesis file not found: {hyp_path}")
        sys.exit(1)

    ref_stem = derive_reference_stem(hyp_path)
    ref_path = ref_dir / f"{ref_stem}.jsonl"

    if not ref_path.is_file():
        logging.warning(f"Reference not found: {ref_path} — skipping {hyp_path.name}")
        logging.warning(f"  (derived stem: {ref_stem})")
        sys.exit(0)

    logging.info(f"Scoring: {hyp_path.name} <-> {ref_path.name}")

    ref_records = load_jsonl(ref_path)
    hyp_records = load_jsonl(hyp_path)

    logging.debug(f"Loaded {len(ref_records)} reference records")
    logging.debug(f"Loaded {len(hyp_records)} hypothesis records")

    merged = align_records(ref_records, hyp_records)
    if not merged:
        logging.error(f"No valid records after alignment for {hyp_path.name}")
        sys.exit(1)

    logging.debug(f"Aligned {len(merged)} records")

    results = Evaluation(merged).score_over_datasets(normalize=True)
    results = round_scores(results)
    assert isinstance(results, dict)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    cmer = results["averaged_scores"]["cmer_macro"][0]
    pref = results["averaged_scores"]["pref_score_cmer_macro"][0]
    logging.info(f"  cmer_macro={cmer:.4f}  pref_cmer_macro={pref:.4f}")
    logging.info(f"Results written to: {out_path}")
    if log_file:
        logging.info(f"Log written to: {log_file}")


if __name__ == "__main__":
    main()
