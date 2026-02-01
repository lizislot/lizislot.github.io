import numpy as np
import pandas as pd

from signal_lab.factors import add_factors


def test_add_factors_er_and_mom():
    df = pd.DataFrame({"close": [10, 11, 12, 11, 13]})

    result = add_factors(df, er_n=3, mom_n=2, vol_n=3)

    expected_er = [np.nan, np.nan, np.nan, 1 / 3, 0.5]
    expected_mom = [np.nan, np.nan, 0.2, 0.0, 13 / 12 - 1]

    assert np.isnan(result.loc[0, "er"])
    assert np.isnan(result.loc[1, "er"])
    assert np.isnan(result.loc[2, "er"])
    assert np.isclose(result.loc[3, "er"], expected_er[3])
    assert np.isclose(result.loc[4, "er"], expected_er[4])

    assert np.isnan(result.loc[0, "mom2"])
    assert np.isnan(result.loc[1, "mom2"])
    assert np.isclose(result.loc[2, "mom2"], expected_mom[2])
    assert np.isclose(result.loc[3, "mom2"], expected_mom[3])
    assert np.isclose(result.loc[4, "mom2"], expected_mom[4])
