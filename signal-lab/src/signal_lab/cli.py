"""Command-line interface for running the signal lab workflow."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .backtest import backtest_one
from .factors import add_factors
from .io import load_universe
from .report import write_report
from .signal import make_signal


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run signal generation and backtests.")
    parser.add_argument("--data_dir", type=Path, required=True, help="CSV input folder.")
    parser.add_argument("--out_dir", type=Path, default=Path("outputs"))
    parser.add_argument("--hold_days", type=int, default=5)
    parser.add_argument("--er_n", type=int, default=10)
    parser.add_argument("--er_min", type=float, default=0.35)
    parser.add_argument("--mom_n", type=int, default=5)
    parser.add_argument("--mom_min", type=float, default=0.03)
    parser.add_argument("--vol_n", type=int, default=20)
    parser.add_argument("--vol_max", type=float, default=0.04)
    return parser.parse_args()


def _prepare_signals(
    ticker: str,
    df: pd.DataFrame,
    hold_days: int,
    er_n: int,
    er_min: float,
    mom_n: int,
    mom_min: float,
    vol_n: int,
    vol_max: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    df_factors = add_factors(df, er_n=er_n, mom_n=mom_n, vol_n=vol_n)
    df_factors["mom"] = df_factors[f"mom{mom_n}"]
    df_factors["vol"] = df_factors[f"vol{vol_n}"]
    df_signals = make_signal(df_factors, er_min=er_min, mom_min=mom_min, vol_max=vol_max)

    signal_output = df_signals[["date", "close", "er", "mom", "vol", "signal"]].copy()
    signal_output.insert(0, "ticker", ticker)

    backtest_input = df_signals.set_index("date")
    trades = backtest_one(backtest_input, hold_days=hold_days)
    trades.insert(0, "ticker", ticker)

    return signal_output, trades


def main() -> None:
    args = parse_args()
    universe = load_universe(args.data_dir)

    signals_frames: list[pd.DataFrame] = []
    trades_frames: list[pd.DataFrame] = []

    for ticker, df in universe.items():
        signal_output, trades = _prepare_signals(
            ticker=ticker,
            df=df,
            hold_days=args.hold_days,
            er_n=args.er_n,
            er_min=args.er_min,
            mom_n=args.mom_n,
            mom_min=args.mom_min,
            vol_n=args.vol_n,
            vol_max=args.vol_max,
        )
        signals_frames.append(signal_output)
        trades_frames.append(trades)

    signals_df = (
        pd.concat(signals_frames, ignore_index=True)
        if signals_frames
        else pd.DataFrame(columns=["ticker", "date", "close", "er", "mom", "vol", "signal"])
    )
    trades_df = (
        pd.concat(trades_frames, ignore_index=True)
        if trades_frames
        else pd.DataFrame(
            columns=[
                "ticker",
                "entry_date",
                "exit_date",
                "entry_price",
                "exit_price",
                "ret",
                "hold_days",
            ]
        )
    )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    signals_path = args.out_dir / "signals.csv"
    trades_path = args.out_dir / "trades.csv"
    report_path = args.out_dir / "report.md"

    signals_df.to_csv(signals_path, index=False)
    trades_df.to_csv(trades_path, index=False)
    write_report(trades_df, report_path)

    print(f"Saved signals to {signals_path}")
    print(f"Saved trades to {trades_path}")
    print(f"Saved report to {report_path}")


if __name__ == "__main__":
    main()
