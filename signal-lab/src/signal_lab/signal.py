"""Signal rules for factor-based entries."""

from __future__ import annotations

import pandas as pd


def make_signal(
    df: pd.DataFrame, er_min: float = 0.35, mom_min: float = 0.03, vol_max: float = 0.04
) -> pd.DataFrame:
    """Add a boolean signal column based on factor thresholds.

    A signal is ``True`` only when ``er``, ``mom``, and ``vol`` are not NaN and
    satisfy ``er >= er_min``, ``mom >= mom_min``, and ``vol <= vol_max``.

    Args:
        df: Input DataFrame with ``er``, ``mom``, and ``vol`` columns.
        er_min: Minimum efficiency ratio threshold.
        mom_min: Minimum momentum threshold.
        vol_max: Maximum volatility threshold.

    Returns:
        A copy of ``df`` with a new ``signal`` boolean column.
    """

    df_copy = df.copy()
    er = df_copy["er"]
    mom = df_copy["mom"]
    vol = df_copy["vol"]

    available = er.notna() & mom.notna() & vol.notna()
    thresholds = (er >= er_min) & (mom >= mom_min) & (vol <= vol_max)
    df_copy["signal"] = available & thresholds

    return df_copy
