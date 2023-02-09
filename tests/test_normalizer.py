from typing import List

import numpy as np
import pandas as pd
import pytest

from cronus_eater import _extractor, _normalizer
from cronus_eater.model import TimeSeries, TimeSeriesMetadata


def test_norm_blank_value():
    assert _normalizer.norm_blank_value(np.nan) is pd.NA
    assert _normalizer.norm_blank_value(None) is pd.NA

    assert _normalizer.norm_blank_value('') is pd.NA
    assert _normalizer.norm_blank_value('    ') is pd.NA
    assert _normalizer.norm_blank_value(' -   ') is pd.NA
    assert _normalizer.norm_blank_value('NaN  ') is pd.NA


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


@pytest.mark.skip(reason='In progress ...')
def test_norm_time_series(time_series: List[TimeSeries]):
    # Get Source test
    source_dataframe = pd.read_excel(
        'tests/data/source_norm_nubank_0.xlsx',
        header=None,
    )
    source_dataframe = source_dataframe.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    metadata = TimeSeriesMetadata('', '', 0, 0, 0, 0)
    source_time_series = TimeSeries(
        metadata=metadata, dataframe=source_dataframe
    )

    # Get Target test
    target_dataframe = pd.read_excel(
        'tests/data/target_norm_nubank_0.xlsx',
        header=None,
    )
    target_dataframe = target_dataframe.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )

    assert _normalizer.norm_time_series(source_time_series).dataframe.equals(
        target_dataframe
    )


@pytest.mark.skip(reason='In progress ...')
def test_norm_all_time_series(
    time_series: List[TimeSeries],
) -> List[TimeSeries]:
    ...
