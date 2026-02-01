"""Command-line interface for Signal Lab."""

from __future__ import annotations

import argparse
from pathlib import Path

from .core import generate_signals


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate sample signal data.")
    parser.add_argument("--rows", type=int, default=100, help="Number of samples.")
    parser.add_argument(
        "--frequency", type=float, default=0.1, help="Frequency of the sine wave."
    )
    parser.add_argument(
        "--noise-scale", type=float, default=0.05, help="Noise standard deviation."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/signal.csv"),
        help="Output CSV file path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = generate_signals(
        rows=args.rows,
        frequency=args.frequency,
        noise_scale=args.noise_scale,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Saved {len(df)} rows to {args.output}")


if __name__ == "__main__":
    main()
