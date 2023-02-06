import pandas as pd

from cronus_eater import _extractor, _normalizer
from cronus_eater.model import TimeSeriesMetadata


def test_find_header():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    assert _extractor.find_header(df, start_row=24, end_column=11) == 21


def test_clean_time_series_from_raw_df():
    df = pd.read_excel('tests/data/source.xlsx', header=None)

    metadata = TimeSeriesMetadata(
        '', '', start_row=21, end_row=35, start_column=1, end_column=11
    )

    df = _extractor.clean_time_series_from_raw_df(df, metadata)

    tot_not_null = (
        (
            ~df.iloc[
                metadata.start_row : metadata.end_row + 1,
                metadata.start_column : metadata.end_column + 1,
            ].isnull()
        )
        .sum()
        .iloc[0]
    )

    assert tot_not_null == 0


def test_find_end_column():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    valid_row = df.iloc[24, 1:]

    assert _extractor.find_end_column(valid_row) == 11


def test_find_end_row_column():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    end_row, end_column = _extractor.find_end_row_column(
        df, start_row=24, start_column=1
    )

    assert end_row == 35
    assert end_column == 11


def test_find_start_row_index():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    assert _extractor.find_start_row_index(df, 1) == 24


def test_find_start_row_column():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    star_row, start_column = _extractor.find_start_row_column(df)

    assert star_row == 24
    assert start_column == 1


def test_clean_gargabe_table():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    # there's a column valid, but no time series row , clean the garbage!!!
    start_row, start_column, end_row, end_column = 24, 1, 35, 11
    df = _extractor.clean_gargabe_table(
        df, start_row, start_column, end_row, end_column
    )
    tot_null = (
        (
            ~df.iloc[
                start_row : end_row + 1, start_column : end_column + 1
            ].isnull()
        )
        .sum()
        .iloc[0]
    )
    assert tot_null == 0

    df = pd.DataFrame()
    start_row, start_column, end_row, end_column = 2, -1, 3, -1
    assert df.equals(
        _extractor.clean_gargabe_table(
            df, start_row, start_column, end_row, end_column
        )
    )


def test_clean_gargabe_column():
    # There's a column valid, but no time series row , clean the garbage!!!
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    start_row, start_column = -1, 1
    df = _extractor.clean_gargabe_column(df, start_row, start_column)
    tot_null = (~df.iloc[:, start_column].isnull()).sum()
    assert tot_null == 0

    # Empty dataframe, do nothing
    df = pd.DataFrame()
    start_row, start_column = -1, -1
    assert df.equals(
        _extractor.clean_gargabe_column(df, start_row, start_column)
    )

    # There's no way to find a valid row without column, do nothing
    df = pd.DataFrame()
    start_row, start_column = 4, -1
    assert df.equals(
        _extractor.clean_gargabe_column(df, start_row, start_column)
    )

    # There's nothing wrong, do nothing
    df = pd.DataFrame()
    start_row, start_column = 4, 4
    assert df.equals(
        _extractor.clean_gargabe_column(df, start_row, start_column)
    )


def test_find_time_series():
    raw_dataframe = pd.read_excel('tests/data/source.xlsx', header=None)
    time_series = _extractor.find_time_series(raw_dataframe)

    assert len(time_series) == 4

    target_0 = pd.read_excel('tests/data/target_0.xlsx', header=None)
    target_1 = pd.read_excel('tests/data/target_1.xlsx', header=None)
    target_2 = pd.read_excel('tests/data/target_2.xlsx', header=None)
    target_3 = pd.read_excel('tests/data/target_3.xlsx', header=None)

    target_0 = target_0.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    target_1 = target_1.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    target_2 = target_2.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    target_3 = target_3.applymap(
        lambda value: _normalizer.norm_blank_value(value)
    )
    assert time_series[0].dataframe.equals(target_0)
    assert time_series[1].dataframe.equals(target_1)
    assert time_series[2].dataframe.equals(target_2)
    assert time_series[3].dataframe.equals(target_3)
