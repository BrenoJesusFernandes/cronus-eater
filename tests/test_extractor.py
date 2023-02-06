import pandas as pd
import pytest
from loguru import logger

from cronus_eater import _extractor, _normalizer
from cronus_eater.model import TimeSeriesMetadata


def test_find_header():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    assert _extractor.find_header(df, start_row=24, end_column=11) == 21


def test_clean_time_series_from_raw_df():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)

    metadata = TimeSeriesMetadata(
        '', '', start_row=21, end_row=35, start_column=1, end_column=11
    )

    df = _extractor.clean_time_series_from_raw_df(df, metadata)

    tot_not_null = (
        df[
            ~df.iloc[
                metadata.start_row : metadata.end_row + 1,
                metadata.start_column : metadata.end_column + 1,
            ].isnull()
        ]
        .sum()
        .iloc[0]
    )

    assert tot_not_null == 0


def test_find_end_column():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    valid_row = df.iloc[24, 1:]

    assert _extractor.find_end_column(valid_row) == 11


def test_find_end_row_column():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    end_row, end_column = _extractor.find_end_row_column(
        df, start_row=24, start_column=1
    )

    assert end_row == 35
    assert end_column == 11


def test_find_start_row_index():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    assert _extractor.find_start_row_index(df, 1) == 24


def test_find_start_row_column():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    star_row, start_column = _extractor.find_start_row_column(df)

    assert star_row == 24
    assert start_column == 1


@pytest.mark.skip(reason='no way of currently testing this')
def test_find_time_series():
    raw_dataframe = pd.read_excel('tests/data/source_0.xlsx', header=None)
    time_series = _extractor.find_time_series(raw_dataframe)

    assert len(time_series) == 4
