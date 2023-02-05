from typing import Dict, List, Tuple, Union

import pandas as pd

from cronus_eater import _validator
from cronus_eater.model import TimeSeries, TimeSeriesMetadata


def find_metadata(df: pd.DataFrame, origin: str) -> List[TimeSeriesMetadata]:
    return []


def slice_dataframe(
    df: pd.DataFrame, metadata: List[TimeSeriesMetadata]
) -> List[TimeSeries]:
    return []


def find_start_row_index(df: pd.DataFrame, column_index: int) -> int:
    for row_index, row in df.iloc[:, column_index:].iterrows():
        if not pd.isnull(row.iloc[0]):
            if _validator.is_time_series_row(row):
                return int(str(row_index))

    return -1


def find_start_row_column(df: pd.DataFrame) -> Tuple[int, int]:
    for column_index, column in df.items():
        if len(column.dropna()) > 3:
            start_column = int(str(column_index))
            start_row = find_start_row_index(df, int(str(column_index)))

            if start_row != -1:
                return start_row, start_column

    return -1, -1


def find_end_row_column(
    df: pd.DataFrame, start_row: int, start_column: int
) -> Tuple[int, int]:
    return -1, -1


def clean_df_from_old_ts(
    df: pd.DataFrame, metadata: TimeSeriesMetadata
) -> pd.DataFrame:
    return pd.DataFrame()


def find_time_series(raw_dataframe: pd.DataFrame) -> List[TimeSeries]:

    df = raw_dataframe.copy()
    times_series = []

    while True:
        start_row, start_column = find_start_row_column(df)
        if -1 in (start_row, start_column):
            break

        end_row, end_column = find_end_row_column(df, start_row, start_column)
        if -1 in (end_row, end_column):
            break

        metadata = TimeSeriesMetadata(
            'whatever',
            'whatever',
            start_column,
            end_column,
            start_row,
            end_row,
        )

        time_series_df = df.iloc[
            start_row:end_row, start_column:end_row
        ].copy()

        times_series.append(TimeSeries(metadata, time_series_df))
        df = clean_df_from_old_ts(df, metadata)

    return times_series


def find_all_time_series(
    raw_dataframe: Dict[Union[int, str], pd.DataFrame]
) -> List[TimeSeries]:
    return []
