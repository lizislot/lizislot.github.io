"""Core signal generation logic."""

from __future__ import annotations

import numpy as np
import pandas as pd


def generate_signals(
    rows: int = 100,
    frequency: float = 0.1,
    noise_scale: float = 0.05,
) -> pd.DataFrame:
    """Generate a simple sine-wave signal with noise.

    Args:
        rows: Number of samples to generate.
        frequency: Frequency multiplier for the sine wave.
        noise_scale: Standard deviation of Gaussian noise.

    Returns:
        DataFrame containing the signal and noise values.
    """

    index = np.arange(rows)
    clean_signal = np.sin(2 * np.pi * frequency * index)
    noise = np.random.normal(loc=0.0, scale=noise_scale, size=rows)
    signal = clean_signal + noise

    return pd.DataFrame(
        {
            "step": index,
            "clean_signal": clean_signal,
            "noise": noise,
            "signal": signal,
        }
    )
