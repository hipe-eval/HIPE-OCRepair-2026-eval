"""Create baseline hypothesis files using dummy correction strategies.

Usage:
    python lib/create_dummy_baselines.py <input_hypothesis.jsonl> <output_dir>
    python lib/create_dummy_baselines.py <input_hypothesis.jsonl> <output_dir> --char-swaps 0.01

Creates one hypothesis file per strategy in the output directory.
Output filenames follow the submission naming convention:
    <strategy>_<benchmark-stem>_run1.jsonl
"""

import sys
import json
import math
import argparse
from pathlib import Path


class DummyCorrectReproduce:
    """Identity baseline: copies the OCR hypothesis unchanged."""

    def __init__(self):
        self.name = "same"

    @staticmethod
    def correct_text(sentence, lang):
        return sentence


class DummyCorrectRandom:
    """Random baseline: shuffles words in the OCR hypothesis."""

    def __init__(self):
        from random import Random

        self.rng = Random(42)
        self.name = "random"

    def correct_text(self, sentence, lang):
        words = sentence.split()
        self.rng.shuffle(words)
        return " ".join(words)


class DummyCorrectCharSwaps:
    """Corruption baseline: swaps a proportion of randomly chosen adjacent character pairs.

    The corrupted text is derived from the ground truth, not from the OCR hypothesis.
    A value of char_swaps=0.01 means that approximately 1% of available adjacent
    non-overlapping character pairs in the text are swapped.

    Swaps are reproducible because a fixed random seed is used.
    """

    def __init__(self, char_swaps: float, seed: int = 42):
        from random import Random

        if not (0.0 <= char_swaps <= 1.0):
            raise ValueError("--char-swaps must be in the range [0, 1].")
        self.char_swaps = char_swaps
        self.rng = Random(seed)
        pct = int(round(char_swaps * 100))
        self.name = f"charswap{pct:02d}"

    def correct_text(self, sentence, lang):
        if len(sentence) < 2 or self.char_swaps <= 0.0:
            return sentence

        chars = list(sentence)

        # Available non-overlapping adjacent pairs: (0,1), (2,3), (4,5), ...
        pair_starts = list(range(0, len(chars) - 1, 2))
        n_pairs = len(pair_starts)
        if n_pairs == 0:
            return sentence

        n_swaps = int(math.floor(n_pairs * self.char_swaps))
        if n_swaps == 0 and self.char_swaps > 0:
            n_swaps = 1
        n_swaps = min(n_swaps, n_pairs)

        chosen_starts = self.rng.sample(pair_starts, n_swaps)
        for i in chosen_starts:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]

        return "".join(chars)


DEFAULT_STRATEGIES = [DummyCorrectReproduce, DummyCorrectRandom]


def create_baseline(input_path, output_path, strategy):
    """Apply a correction strategy to each record and write the result."""
    count = 0
    with open(input_path, "r", encoding="utf-8") as fin, open(
        output_path, "w", encoding="utf-8"
    ) as fout:
        for line in fin:
            if not line.strip():
                continue

            record = json.loads(line)
            lang = record["document_metadata"].get("language", "unknown")

            if isinstance(strategy, DummyCorrectCharSwaps):
                source_text = record["ground_truth"]["transcription_unit"]
            else:
                source_text = record["ocr_hypothesis"]["transcription_unit"]

            record.setdefault("ocr_postcorrection_output", {})["transcription_unit"] = (
                strategy.correct_text(source_text, lang)
            )
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1

    return count


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create dummy baseline hypothesis files."
    )
    parser.add_argument("input_hypothesis", help="Input JSONL file")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument(
        "--char-swaps",
        type=float,
        default=None,
        help=(
            "Optional proportion of adjacent character pairs to swap in the "
            "ground-truth text and use as ocr_postcorrection_output "
            "(e.g. 0.01 for 1%%)."
        ),
    )
    return parser.parse_args()


def main():
    args = parse_args()

    input_path = Path(args.input_hypothesis)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    strategies = [cls() for cls in DEFAULT_STRATEGIES]

    if args.char_swaps is not None:
        strategies.append(DummyCorrectCharSwaps(args.char_swaps))

    for strategy in strategies:
        output_path = output_dir / f"{strategy.name}_{input_path.stem}_run1.jsonl"
        count = create_baseline(input_path, output_path, strategy)
        print(f"[{strategy.name}] Wrote {count} records to {output_path}")


if __name__ == "__main__":
    main()
