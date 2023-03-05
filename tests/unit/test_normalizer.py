from typing import List

import numpy as np
import pandas as pd
import pytest

from cronus_eater import _normalizer
from cronus_eater.exceptions import EmptyDataFrame


def test_norm_header():
    # Get Source test
    source_dataframe = pd.read_excel(
        'tests/unit/data/source_norm_nubank_0.xlsx',
        header=None,
    )
    source_dataframe = source_dataframe.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    source_header = source_dataframe.iloc[0, :]

    # Get Target test
    target_dataframe = pd.read_excel(
        'tests/unit/data/target_norm_nubank_0.xlsx',
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


@pytest.mark.xfail(raises=EmptyDataFrame)
def test_norm_df_to_extraction_blank():
    assert _normalizer.norm_df_to_extraction(pd.DataFrame())
    assert _normalizer.norm_df_to_extraction(
        pd.DataFrame(['', pd.NA, np.nan, '-'])
    )


def test_norm_df_to_extraction():
    source_df = pd.DataFrame(
        {
            'First': [' - ', '1', '2', '3', '4'],
            'Second': ['nan', '1', '2', '3', '4'],
            'Third': [None, '1', '2', '3', '4'],
            'Fourth': [np.nan, '1', '2', '3', '4'],
        }
    )

    target_df = pd.DataFrame(
        {
            0: ['First', pd.NA, '1', '2', '3', '4'],
            1: ['Second', pd.NA, '1', '2', '3', '4'],
            2: ['Third', pd.NA, '1', '2', '3', '4'],
            3: ['Fourth', pd.NA, '1', '2', '3', '4'],
        }
    )
    norm_df = _normalizer.norm_df_to_extraction(source_df)
    assert norm_df.equals(target_df)
