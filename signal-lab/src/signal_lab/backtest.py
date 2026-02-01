"""Backtesting utilities."""

from __future__ import annotations

import pandas as pd


def backtest_one(
    df: pd.DataFrame,
    hold_days: int = 5,
    price_col: str = "close",
    signal_col: str = "signal",
    allow_overlap: bool = False,
) -> pd.DataFrame:
    """Run a simple backtest on a single ticker.

    Args:
        df: Input price and signal data.
        hold_days: Number of days to hold each trade.
        price_col: Column name for prices.
        signal_col: Column name for entry signals.
        allow_overlap: Whether to allow overlapping trades.

    Returns:
        DataFrame of trades with entry/exit details and returns.
    """

    columns = [
        "entry_date",
        "entry_price",
        "exit_date",
        "exit_price",
        "ret",
        "hold_days",
    ]
    if df.empty:
        return pd.DataFrame(columns=columns)

    trades = []
    row_count = len(df)
    i = 0

    while i < row_count:
        signal = df.iloc[i][signal_col]
        if pd.notna(signal) and bool(signal):
            exit_i = i + hold_days
            if exit_i < row_count:
                entry_price = df.iloc[i][price_col]
                exit_price = df.iloc[exit_i][price_col]
                if pd.notna(entry_price) and pd.notna(exit_price):
                    entry_date = df.index[i]
                    exit_date = df.index[exit_i]
                    trades.append(
                        {
                            "entry_date": entry_date,
                            "entry_price": entry_price,
                            "exit_date": exit_date,
                            "exit_price": exit_price,
                            "ret": exit_price / entry_price - 1,
                            "hold_days": hold_days,
                        }
                    )
                    if not allow_overlap:
                        i = exit_i + 1
                        continue
        i += 1

    return pd.DataFrame(trades, columns=columns)
