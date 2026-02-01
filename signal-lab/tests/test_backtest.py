import pandas as pd

from signal_lab.backtest import backtest_one


def test_backtest_one_simple_case_without_overlap():
    dates = pd.date_range("2024-01-01", periods=6, freq="D")
    df = pd.DataFrame(
        {
            "close": [10, 11, 12, 13, 14, 15],
            "signal": [True, False, True, False, True, False],
        },
        index=dates,
    )

    trades = backtest_one(df, hold_days=2)

    assert len(trades) == 1
    assert trades.loc[0, "entry_date"] == dates[0]
    assert trades.loc[0, "exit_date"] == dates[2]
    assert trades.loc[0, "ret"] == 12 / 10 - 1
