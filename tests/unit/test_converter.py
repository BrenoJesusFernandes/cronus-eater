from cronus_eater import _converter

import pandas as pd
import numpy as np


def test_blank_to_zero():
    assert _converter.blank_to_zero('- ') == 0
    assert _converter.blank_to_zero(None) == 0
    assert _converter.blank_to_zero(0.0) == 0


def test_blank_to_na():
    assert _converter.blank_to_na(np.nan) is pd.NA
    assert _converter.blank_to_na(None) is pd.NA

    assert _converter.blank_to_na('') is pd.NA
    assert _converter.blank_to_na('    ') is pd.NA
    assert _converter.blank_to_na(' -   ') is pd.NA
    assert _converter.blank_to_na('NaN  ') is pd.NA
