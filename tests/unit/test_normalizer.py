from typing import List

import numpy as np
import pandas as pd
import pytest

from cronus_eater import _normalizer




def test_norm_header():
    # Get Source test
    source_dataframe = pd.read_excel(
        'tests/data/source_norm_nubank_0.xlsx',
        header=None,
    )
    source_dataframe = source_dataframe.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    source_header = source_dataframe.iloc[0, :]

    # Get Target test
    target_dataframe = pd.read_excel(
        'tests/data/target_norm_nubank_0.xlsx',
        header=None,
    )
    target_dataframe = target_dataframe.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    target_header = target_dataframe.iloc[0, :]

    source_header = source_header.apply(
        lambda value: _normalizer.norm_header(value)
    )

    assert source_header.equals(target_header)
