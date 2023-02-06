import numpy as np

from cronus_eater import _normalizer


def test_norm_blank_value():
    assert _normalizer.norm_blank_value(np.nan) is np.nan
    assert _normalizer.norm_blank_value(None) is np.nan

    assert _normalizer.norm_blank_value('') is np.nan
    assert _normalizer.norm_blank_value('    ') is np.nan
    assert _normalizer.norm_blank_value(' -   ') is np.nan
    assert _normalizer.norm_blank_value('NaN  ') is np.nan
