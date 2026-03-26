#!/usr/bin/env python3
"""Build a HIPE-2022-style Markdown results document from TSV ranking files.

Reads results/system-rankings/ranking-*-cmer-micro.tsv and produces
HIPE_OCRepair_2026_evaluation_results.md.

TSV filename convention: ranking-<dataset>-<split>-<language>-cmer-micro.tsv
"""

import argparse
import csv
import json
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

LANGUAGE_NAMES = {
    "de": "German",
    "fr": "French",
    "en": "English",
    "nl": "Dutch",
    "fi": "Finnish",
    "sv": "Swedish",
    "it": "Italian",
}


def load_teams(teams_json: Path) -> dict[str, str]:
    if teams_json.exists():
        with open(teams_json, encoding="utf-8") as f:
            return json.load(f)
    return {}


def fmt(val, precision: int = 4) -> str:
    if val is None or val == "":
        return "—"
    try:
        return f"{float(val):.{precision}f}"
    except (ValueError, TypeError):
        return str(val)


def parse_tsv_filename(name: str) -> dict | None:
    """Parse ranking-<dataset>-<split>-<language>-cmer-micro.tsv.

    Handles datasets with hyphens (e.g. impresso-snippets) by splitting
    from the right: last two hyphen-separated tokens are language and split.
    """
    m = re.match(r"^ranking-(.+)-cmer-micro$", Path(name).stem)
    if not m:
        return None
    inner = m.group(1)
    parts = inner.rsplit("-", 2)
    if len(parts) != 3:
        return None
    dataset, split, language = parts
    return {"dataset": dataset, "split": split, "language": language}


def parse_overall_tsv_filename(name: str) -> dict | None:
    """Parse ranking-overall-<split>-weighted.tsv."""
    m = re.match(r"^ranking-overall-(?P<split>[^-]+)-weighted$", Path(name).stem)
    if not m:
        return None
    return {"split": m.group("split")}


def parse_language_tsv_filename(name: str) -> dict | None:
    """Parse ranking-language-<lang>-<split>-weighted.tsv."""
    m = re.match(
        r"^ranking-language-(?P<language>[^-]+)-(?P<split>[^-]+)-weighted$",
        Path(name).stem,
    )
    if not m:
        return None
    return {"language": m.group("language"), "split": m.group("split")}


def build_team_key_table(teams: dict) -> list[str]:
    lines = [
        "## Team key\n",
        "| Team ID | Affiliation |",
        "|---------|-------------|",
    ]
    for team_id, affiliation in sorted(teams.items()):
        lines.append(f"| {team_id} | {affiliation} |")
    return lines


def build_ranking_table(rows: list[dict]) -> list[str]:
    header = (
        "| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI |"
        " cMER macro | wMER macro |"
    )
    sep = (
        "|------|--------|--------------|--------|---------------|--------|"
        "------------|------------|"
    )
    lines = [header, sep]
    for row in rows:
        rank = row.get("rank", "")
        system = row.get("system", "")
        cmer_micro = fmt(row.get("cmer_micro"))
        ci = f"[{fmt(row.get('cmer_micro_lo'))}, {fmt(row.get('cmer_micro_hi'))}]"
        pref = fmt(row.get("pref_score_cmer_macro"))
        pref_ci = (
            f"[{fmt(row.get('pref_score_cmer_macro_lo'))},"
            f" {fmt(row.get('pref_score_cmer_macro_hi'))}]"
        )
        cmer_macro = fmt(row.get("cmer_macro"))
        wmer_macro = fmt(row.get("wmer_macro"))
        lines.append(
            f"| {rank} | {system} | {cmer_micro} | {ci} | {pref} | {pref_ci}"
            f" | {cmer_macro} | {wmer_macro} |"
        )
    return lines


def build_overall_ranking_table(rows: list[dict]) -> list[str]:
    header = (
        "| Rank | System | Overall cMER ↓ | 95% CI\u00b9 | Overall Pref. ↑ |"
        " 95% CI\u00b9 | Test sets |"
    )
    sep = "|------|--------|----------------|---------|-----------------|---------|----------|"
    lines = [header, sep]
    for row in rows:
        rank = row.get("rank", "")
        system = row.get("system", "")
        cmer = fmt(row.get("overall_cmer"))
        ci = f"[{fmt(row.get('overall_cmer_lo'))}, {fmt(row.get('overall_cmer_hi'))}]"
        pref = fmt(row.get("overall_pref"))
        pref_ci = (
            f"[{fmt(row.get('overall_pref_lo'))}, {fmt(row.get('overall_pref_hi'))}]"
        )
        n = row.get("n_test_sets", "")
        n_total = row.get("n_total_test_sets", "")
        lines.append(
            f"| {rank} | {system} | {cmer} | {ci} | {pref} | {pref_ci} |"
            f" {n}/{n_total} |"
        )
    return lines


def build_language_ranking_table(rows: list[dict]) -> list[str]:
    header = (
        "| Rank | System | Language cMER ↓ | 95% CI\u00b9 | Language Pref. ↑ |"
        " 95% CI\u00b9 | Test sets |"
    )
    sep = "|------|--------|-----------------|---------|------------------|---------|----------|"
    lines = [header, sep]
    for row in rows:
        rank = row.get("rank", "")
        system = row.get("system", "")
        cmer = fmt(row.get("language_cmer"))
        ci = f"[{fmt(row.get('language_cmer_lo'))}, {fmt(row.get('language_cmer_hi'))}]"
        pref = fmt(row.get("language_pref"))
        pref_ci = (
            f"[{fmt(row.get('language_pref_lo'))}, {fmt(row.get('language_pref_hi'))}]"
        )
        n = row.get("n_test_sets", "")
        n_total = row.get("n_total_test_sets", "")
        lines.append(
            f"| {rank} | {system} | {cmer} | {ci} | {pref} | {pref_ci} |"
            f" {n}/{n_total} |"
        )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Markdown results document from TSV ranking files."
    )
    parser.add_argument(
        "--rankings-dir", required=True, help="Directory with ranking TSV files."
    )
    parser.add_argument(
        "--teams-json", default="lib/teams.json", help="Path to teams JSON file."
    )
    parser.add_argument(
        "--output", required=True, help="Path to write Markdown results file."
    )
    parser.add_argument(
        "--scorer-version", default="0.9.0", help="Scorer version string."
    )
    parser.add_argument(
        "--data-version", default="v0.9", help="Benchmark version string."
    )
    parser.add_argument(
        "--date",
        default=str(date.today()),
        help="Evaluation date (YYYY-MM-DD).",
    )
    args = parser.parse_args()

    rankings_dir = Path(args.rankings_dir)
    output_path = Path(args.output)
    teams = load_teams(Path(args.teams_json))

    all_tsv_files = sorted(rankings_dir.glob("ranking-*.tsv"))
    if not all_tsv_files:
        print(f"[ERROR] No ranking TSV files found in {rankings_dir}")
        return

    # Separate overall-weighted, language-weighted, and per-test-set TSVs
    overall_tsvs: list[tuple] = []  # (tsv_path, meta)
    language_tsvs: list[tuple] = []  # (tsv_path, meta)
    dataset_groups: dict[str, list] = defaultdict(list)
    for tsv_path in all_tsv_files:
        overall_meta = parse_overall_tsv_filename(tsv_path.name)
        if overall_meta is not None:
            overall_tsvs.append((tsv_path, overall_meta))
            continue
        lang_meta = parse_language_tsv_filename(tsv_path.name)
        if lang_meta is not None:
            language_tsvs.append((tsv_path, lang_meta))
            continue
        meta = parse_tsv_filename(tsv_path.name)
        if meta is None:
            print(f"[WARNING] Cannot parse TSV filename: {tsv_path.name}, skipping.")
            continue
        dataset_groups[meta["dataset"]].append((tsv_path, meta))

    lines: list[str] = [
        "# HIPE-OCRepair 2026 – Evaluation Results\n",
        f"- **Date**: {args.date}",
        f"- **Scorer**: hipe-ocrepair-scorer v{args.scorer_version}",
        f"- **Benchmark**: hipe-ocrepair-bench {args.data_version}",
        "",
        "System names follow the pattern:  ",
        "`<teamname>_hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>_run<N>`",
        "",
        (
            "**Primary metric**: overall micro-cMER — weighted mean of per-test-set"
            " cMER micro (`cmer_micro`) — **lower is better**  "
        ),
        (
            "**Secondary metric**: overall macro-preference — weighted mean of"
            " per-test-set preference score (`pref_score_cmer_macro`) —"
            " **higher is better**"
        ),
        "",
        (
            "**Weighting**: each non-DTA test set has weight\u00a01; each of the three"
            " DTA test sets (dta19-l0, dta19-l1, dta19-l2) has weight\u00a01/3,"
            " so that together they contribute as one dataset to the overall score."
            " These are design weights, not corpus-size weights."
        ),
        "",
    ]

    if teams:
        lines.extend(build_team_key_table(teams))
        lines.append("")

    # --- Overall weighted rankings ---
    if overall_tsvs:
        lines.append("## Overall rankings\n")
        lines.append(
            "Scores are computed separately for each official test set. Overall"
            " benchmark scores are weighted averages over test sets, using the"
            " design weights described above."
        )
        lines.append("")
        lines.append(
            "\u00b9\u00a0CIs for overall scores are approximate (weighted average of"
            " per-test-set bootstrap CIs)."
        )
        lines.append("")
        for tsv_path, meta in sorted(overall_tsvs, key=lambda x: x[1]["split"]):
            split = meta["split"]
            lines.append(f"### Overall — {split} split\n")
            with open(tsv_path, encoding="utf-8") as f:
                rows = list(csv.DictReader(f, delimiter="\t"))
            if rows:
                lines.extend(build_overall_ranking_table(rows))
                lines.append("")
                tsv_rel = os.path.relpath(tsv_path, output_path.parent)
                lines.append(f"See [{tsv_path.name}]({tsv_rel}) for full details.\n")
            else:
                lines.append("_No results available._\n")

    # --- Per-language weighted rankings ---
    if language_tsvs:
        lines.append("## Per-language rankings\n")
        lines.append(
            "Per-language rankings are computed in the same way as the overall"
            " ranking, but restricted to the official test sets of the respective"
            " language."
        )
        lines.append("")
        lines.append(
            "\u00b9\u00a0CIs for language scores are approximate (weighted average of"
            " per-test-set bootstrap CIs)."
        )
        lines.append("")
        for tsv_path, meta in sorted(
            language_tsvs, key=lambda x: (x[1]["split"], x[1]["language"])
        ):
            split = meta["split"]
            lang = meta["language"]
            lang_name = LANGUAGE_NAMES.get(lang, lang.upper())
            lines.append(f"### Language: {lang} ({lang_name}) — {split} split\n")
            with open(tsv_path, encoding="utf-8") as f:
                rows = list(csv.DictReader(f, delimiter="\t"))
            if rows:
                lines.extend(build_language_ranking_table(rows))
                lines.append("")
                tsv_rel = os.path.relpath(tsv_path, output_path.parent)
                lines.append(f"See [{tsv_path.name}]({tsv_rel}) for full details.\n")
            else:
                lines.append("_No results available._\n")

    lines.append("## Results by dataset\n")

    for dataset in sorted(dataset_groups.keys()):
        lines.append(f"### Dataset: {dataset}\n")
        for tsv_path, meta in sorted(
            dataset_groups[dataset], key=lambda x: x[1]["language"]
        ):
            lang = meta["language"]
            split = meta["split"]
            lang_name = LANGUAGE_NAMES.get(lang, lang.upper())
            lines.append(f"#### Language: {lang} ({lang_name}) — {split} split\n")
            lines.append(
                "cMER micro [`cmer_micro`] — ordered ascending (lower is better)\n"
            )

            with open(tsv_path, encoding="utf-8") as f:
                rows = list(csv.DictReader(f, delimiter="\t"))

            if rows:
                lines.extend(build_ranking_table(rows))
                lines.append("")
                tsv_rel = os.path.relpath(tsv_path, output_path.parent)
                lines.append(f"See [{tsv_path.name}]({tsv_rel}) for full details.\n")
            else:
                lines.append("_No results available._\n")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {output_path}")


if __name__ == "__main__":
    main()
