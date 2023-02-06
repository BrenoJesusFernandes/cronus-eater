import numpy as np
import pandas as pd

from cronus_eater import _normalizer


def test_norm_blank_value():
    assert _normalizer.norm_blank_value(np.nan) is pd.NA
    assert _normalizer.norm_blank_value(None) is pd.NA

    assert _normalizer.norm_blank_value('') is pd.NA
    assert _normalizer.norm_blank_value('    ') is pd.NA
    assert _normalizer.norm_blank_value(' -   ') is pd.NA
    assert _normalizer.norm_blank_value('NaN  ') is pd.NA
