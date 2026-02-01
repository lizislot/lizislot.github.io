from __future__ import annotations

import pandas as pd
import pytest

from signal_lab.io import load_price_csv


def _write_csv(path, rows):
    pd.DataFrame(rows).to_csv(path, index=False)


def test_load_price_csv_happy_path(tmp_path):
    csv_path = tmp_path / "AAA.csv"
    _write_csv(
        csv_path,
        [
            {
                "date": "2024-01-01",
                "open": 1,
                "high": 2,
                "low": 0.5,
                "close": 1.5,
                "volume": 100,
            }
        ],
    )

    df = load_price_csv(csv_path)

    assert list(df.columns) == ["date", "open", "high", "low", "close", "volume"]
    assert len(df) == 1
    assert df.loc[0, "date"] == pd.Timestamp("2024-01-01")


def test_load_price_csv_missing_columns(tmp_path):
    csv_path = tmp_path / "BBB.csv"
    _write_csv(
        csv_path,
        [
            {
                "date": "2024-01-01",
                "open": 1,
                "high": 2,
                "low": 0.5,
                "close": 1.5,
            }
        ],
    )

    with pytest.raises(ValueError, match="missing required columns"):
        load_price_csv(csv_path)


def test_load_price_csv_sorts_by_date(tmp_path):
    csv_path = tmp_path / "CCC.csv"
    _write_csv(
        csv_path,
        [
            {
                "date": "2024-01-03",
                "open": 1,
                "high": 2,
                "low": 0.5,
                "close": 1.5,
                "volume": 100,
            },
            {
                "date": "2024-01-01",
                "open": 2,
                "high": 3,
                "low": 1,
                "close": 2.5,
                "volume": 200,
            },
        ],
    )

    df = load_price_csv(csv_path)

    assert df["date"].tolist() == [
        pd.Timestamp("2024-01-01"),
        pd.Timestamp("2024-01-03"),
    ]


def test_load_price_csv_deduplicates_date(tmp_path):
    csv_path = tmp_path / "DDD.csv"
    _write_csv(
        csv_path,
        [
            {
                "date": "2024-01-01",
                "open": 1,
                "high": 2,
                "low": 0.5,
                "close": 1.5,
                "volume": 100,
            },
            {
                "date": "2024-01-01",
                "open": 2,
                "high": 3,
                "low": 1,
                "close": 2.5,
                "volume": 200,
            },
        ],
    )

    df = load_price_csv(csv_path)

    assert len(df) == 1
    assert df.loc[0, "close"] == 2.5
