"""Factor calculations for price data."""

from __future__ import annotations

import pandas as pd


def add_factors(
    df: pd.DataFrame, er_n: int = 10, mom_n: int = 5, vol_n: int = 20
) -> pd.DataFrame:
    """Add efficiency ratio, momentum, and volatility factors.

    Args:
        df: Input DataFrame with a ``close`` price column.
        er_n: Lookback window for the efficiency ratio.
        mom_n: Lookback window for momentum.
        vol_n: Lookback window for volatility.

    Returns:
        A copy of ``df`` with new columns for ``er``, ``mom{mom_n}``, and
        ``vol{vol_n}`` added.
    """

    df_copy = df.copy()
    close = df_copy["close"]

    absolute_change = (close - close.shift(er_n)).abs()
    path_length = close.diff().abs().rolling(er_n).sum()
    df_copy["er"] = absolute_change / path_length

    df_copy[f"mom{mom_n}"] = close / close.shift(mom_n) - 1

    returns = close.pct_change()
    df_copy[f"vol{vol_n}"] = returns.rolling(vol_n).std()

    return df_copy
