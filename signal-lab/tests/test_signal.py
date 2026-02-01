import numpy as np
import pandas as pd

from signal_lab.signal import make_signal


def test_make_signal_threshold_boundaries_and_nans():
    df = pd.DataFrame(
        {
            "er": [0.35, 0.36, np.nan, 0.36],
            "mom": [0.03, 0.029, 0.03, np.nan],
            "vol": [0.04, 0.05, 0.04, 0.03],
        }
    )

    result = make_signal(df)

    assert result["signal"].tolist() == [True, False, False, False]
