"""Report generation for backtest results."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def _format_float(value: float | int | None) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
    return f"{value:.4f}"


def _format_percent(value: float | int | None) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
    return f"{value:.2%}"


def _overall_stats(trades: pd.DataFrame) -> dict[str, str]:
    if trades.empty:
        return {
            "Total Trades": "0",
            "Win Rate": "N/A",
            "Average Return": "N/A",
            "Median Return": "N/A",
            "P10": "N/A",
            "P25": "N/A",
            "P75": "N/A",
            "P90": "N/A",
        }

    returns = trades["ret"]
    win_rate = (returns > 0).mean()
    return {
        "Total Trades": str(len(trades)),
        "Win Rate": _format_percent(win_rate),
        "Average Return": _format_percent(returns.mean()),
        "Median Return": _format_percent(returns.median()),
        "P10": _format_percent(returns.quantile(0.10)),
        "P25": _format_percent(returns.quantile(0.25)),
        "P75": _format_percent(returns.quantile(0.75)),
        "P90": _format_percent(returns.quantile(0.90)),
    }


def _ticker_summary(trades: pd.DataFrame) -> pd.DataFrame:
    grouped = trades.groupby("ticker")["ret"]
    summary = grouped.agg(
        trades="size",
        win_rate=lambda series: (series > 0).mean(),
        avg_ret="mean",
    )
    return summary.reset_index()


def _table_from_stats(title: str, stats: dict[str, str]) -> str:
    lines = [f"## {title}", "", "| Metric | Value |", "| --- | --- |"]
    for key, value in stats.items():
        lines.append(f"| {key} | {value} |")
    return "\n".join(lines)


def _table_from_dataframe(title: str, df: pd.DataFrame) -> str:
    if df.empty:
        return f"## {title}\n\nNo trades available.\n"

    formatted = df.copy()
    for column in formatted.columns:
        if column in {"win_rate", "avg_ret"}:
            formatted[column] = formatted[column].map(_format_percent)
    header = "| " + " | ".join(formatted.columns) + " |"
    separator = "| " + " | ".join(["---"] * len(df.columns)) + " |"
    rows = [
        "| " + " | ".join(map(str, row)) + " |" for row in formatted.to_numpy()
    ]
    return "\n".join([f"## {title}", "", header, separator, *rows, ""])


def write_report(trades: pd.DataFrame, out_path: str | Path) -> None:
    """Write a markdown report summarizing backtest results."""

    out_path = Path(out_path)
    overall = _overall_stats(trades)
    sections = ["# Backtest Report", "", _table_from_stats("Overall", overall), ""]

    if trades.empty:
        sections.append("## Per Ticker Summary\n\nNo trades available.\n")
    else:
        summary = _ticker_summary(trades)
        summary_sorted = summary.sort_values("avg_ret")
        bottom = summary_sorted.head(10)
        top = summary_sorted.tail(10).iloc[::-1]
        sections.append(_table_from_dataframe("Top 10 Tickers (by Avg Return)", top))
        sections.append(_table_from_dataframe("Bottom 10 Tickers (by Avg Return)", bottom))

    out_path.write_text("\n".join(sections), encoding="utf-8")
