#!/usr/bin/env python3
"""Score a single hypothesis JSONL file against its reference.

The reference file is derived from the hypothesis filename by:
  1. Stripping the _run<N> suffix
  2. Stripping the <teamname>_ prefix

Example:
  team1_hipe-ocrepair-bench_v0.9_impresso-snippets_dev_de_run1.jsonl
  -> hipe-ocrepair-bench_v0.9_impresso-snippets_dev_de.jsonl

Usage:
    python lib/score_one.py \\
        --hypothesis evaluation/system-responses/submitted/team1_..._run1.jsonl \\
        --reference-dir data/reference/ \\
        --output results/per-run/team1_..._run1.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

from hipe_ocrepair_scorer import Evaluation, align_records


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
                print(f"[ERROR] {path} line {i}: {e}", file=sys.stderr)
                sys.exit(1)
    return records


def derive_reference_stem(hypothesis_path: Path) -> str:
    """Derive reference file stem from a hypothesis filename.

    e.g. team1_hipe-ocrepair-bench_v0.9_impresso-snippets_dev_de_run1
      -> hipe-ocrepair-bench_v0.9_impresso-snippets_dev_de
    """
    stem = hypothesis_path.stem
    stem = re.sub(r"_run\d+$", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"^[^_]+_", "", stem)
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
    args = parser.parse_args()

    hyp_path = Path(args.hypothesis)
    ref_dir = Path(args.reference_dir)
    out_path = Path(args.output)

    if not hyp_path.is_file():
        print(f"[ERROR] Hypothesis file not found: {hyp_path}", file=sys.stderr)
        sys.exit(1)

    ref_stem = derive_reference_stem(hyp_path)
    ref_path = ref_dir / f"{ref_stem}.jsonl"

    if not ref_path.is_file():
        print(f"[ERROR] Reference not found: {ref_path}", file=sys.stderr)
        print(f"        (derived from: {hyp_path.name})", file=sys.stderr)
        sys.exit(1)

    print(f"Scoring: {hyp_path.name} <-> {ref_path.name}", file=sys.stderr)

    ref_records = load_jsonl(ref_path)
    hyp_records = load_jsonl(hyp_path)

    merged = align_records(ref_records, hyp_records)
    if not merged:
        print(
            f"[ERROR] No valid records after alignment for {hyp_path.name}",
            file=sys.stderr,
        )
        sys.exit(1)

    results = Evaluation(merged).score_over_datasets(normalize=True)
    results = round_scores(results)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    cmer = results["averaged_scores"]["cmer_macro"][0]
    pref = results["averaged_scores"]["pref_score_cmer_macro"][0]
    print(f"  cmer_macro={cmer:.4f}  pref_score_cmer_macro={pref:.4f}", file=sys.stderr)


if __name__ == "__main__":
    main()
