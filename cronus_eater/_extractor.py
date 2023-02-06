from typing import Dict, List, Tuple, Union

import numpy as np
import pandas as pd

from cronus_eater import _validator
from cronus_eater.model import TimeSeries, TimeSeriesMetadata


def find_metadata(df: pd.DataFrame, origin: str) -> List[TimeSeriesMetadata]:
    return []


def slice_dataframe(
    df: pd.DataFrame, metadata: List[TimeSeriesMetadata]
) -> List[TimeSeries]:
    return []


def find_header(df: pd.DataFrame, start_row: int, end_column: int) -> int:
    for index, value in df.iloc[start_row::-1, end_column].items():
        if _validator.is_text(value):
            return int(str(index))

    return -1


def find_end_column(row: pd.Series) -> int:
    last_text_column = -1
    last_number_column = -1

    # If is a empty sequence return false
    if len(row.dropna()) == 0:
        return False

    # Calcule the right pattern of a time series row
    for index, value in row.items():
        if _validator.is_text(value) and last_number_column == -1:
            last_text_column = int(str(index))
        elif _validator.is_financial_number(value) and last_text_column != -1:
            last_number_column = int(str(index))
        elif _validator.is_text(value) and last_number_column != -1:
            break

    # if a sequence is empty means we do not have a time series pattern
    if -1 in (last_text_column, last_number_column):
        return -1

    return last_number_column


def find_start_row_index(df: pd.DataFrame, column_index: int) -> int:
    for row_index, row in df.iloc[:, column_index:].iterrows():
        if not pd.isnull(row.iloc[0]):
            if _validator.is_time_series_row(row):
                return int(str(row_index))

    return -1


def find_start_row_column(df: pd.DataFrame) -> Tuple[int, int]:
    for column_index, column in df.items():
        start_column = int(str(column_index))
        if len(column.dropna()) >= 2:
            start_row = find_start_row_index(df, int(str(column_index)))

            if start_row != -1:
                return start_row, start_column

    return -1, -1


def find_end_row_column(
    df: pd.DataFrame, start_row: int, start_column: int
) -> Tuple[int, int]:

    end_column = find_end_column(df.iloc[start_row, start_column:])
    df = df.iloc[start_row:, start_column:end_column].copy()

    end_row = -1
    for row_index, row in df.iterrows():
        if _validator.is_time_series_row(row):
            end_row = int(str(row_index))
        elif _validator.is_text_row(row):
            break

    return end_row, end_column


def clean_time_series_from_raw_df(
    df: pd.DataFrame, metadata: TimeSeriesMetadata
) -> pd.DataFrame:
    df.iloc[
        metadata.start_row : metadata.end_row + 1,
        metadata.start_column : metadata.end_column + 1,
    ] = np.nan
    return df.copy()


def find_time_series(raw_dataframe: pd.DataFrame) -> List[TimeSeries]:

    df = raw_dataframe.copy()
    times_series = []

    while True:
        start_row, start_column = find_start_row_column(df)

        if -1 in (start_row, start_column):
            # clean_gargabe()
            continue

        end_row, end_column = find_end_row_column(df, start_row, start_column)
        if -1 in (end_row, end_column):
            # clean_gargabe()
            continue

        start_row = find_header(df, start_row, end_column)
        metadata = TimeSeriesMetadata(
            'whatever',
            'whatever',
            start_column,
            end_column,
            start_row,
            end_row,
        )
        time_series_df = df.iloc[
            start_row : end_row + 1, start_column : end_column + 1
        ].copy()

        times_series.append(TimeSeries(metadata, time_series_df))
        df = clean_time_series_from_raw_df(df, metadata)

        # If there's no more value finish the search
        tot_not_null = df[~df.isnull()].sum().iloc[0]
        if tot_not_null == 0:
            break

    return times_series


def find_all_time_series(
    raw_dataframe: Dict[Union[int, str], pd.DataFrame]
) -> List[TimeSeries]:
    return []
