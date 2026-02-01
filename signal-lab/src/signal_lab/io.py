"""CSV loading helpers for price data."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["date", "open", "high", "low", "close", "volume"]
REQUIRED_COLUMN_SET = set(REQUIRED_COLUMNS)


def load_price_csv(path: str | Path) -> pd.DataFrame:
    """Load a price CSV file and normalize it.

    Args:
        path: CSV file path.

    Returns:
        Normalized DataFrame with required columns, sorted by date.

    Raises:
        ValueError: If required columns are missing or data is empty/invalid.
    """

    csv_path = Path(path)
    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError(f"CSV file '{csv_path}' contains no data.")

    missing = REQUIRED_COLUMN_SET - set(df.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(
            f"CSV file '{csv_path}' is missing required columns: {missing_list}."
        )

    df = df[REQUIRED_COLUMNS].copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        raise ValueError(f"CSV file '{csv_path}' contains invalid date values.")

    df = df.sort_values("date").drop_duplicates(subset=["date"], keep="last")
    return df.reset_index(drop=True)


def load_universe(data_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Load all price CSV files under a directory.

    Args:
        data_dir: Directory containing CSV files.

    Returns:
        Mapping from ticker (filename without extension) to DataFrame.
    """

    directory = Path(data_dir)
    universe: dict[str, pd.DataFrame] = {}

    for csv_path in sorted(directory.glob("*.csv")):
        ticker = csv_path.stem
        universe[ticker] = load_price_csv(csv_path)

    return universe
