from datetime import datetime
from typing import Any, List

import numpy as np
import pandas as pd

from cronus_eater import _validator
from cronus_eater.model import TimeSeries


def norm_blank_value(value: Any) -> Any:
    if _validator.is_blank_value(value):
        return pd.NA

    return value


def norm_header(value: Any) -> Any:
    if isinstance(value, datetime):
        value = f'{pd.Timestamp(value).quarter}T{str(value.year)[2:]}'
        return value

    return value


def norm_index_column(time_series: TimeSeries) -> TimeSeries:
    ...


def norm_numeric_values(time_series: TimeSeries) -> TimeSeries:
    ...


def norm_numerical_values(time_series: TimeSeries) -> TimeSeries:
    ...


def norm_time_series(time_series: TimeSeries) -> TimeSeries:
    # Drop linhas totalmente vazias na vertical e horizontal
    time_series.dataframe.dropna(how='all', axis=0, inplace=True)
    time_series.dataframe.dropna(how='all', axis=1, inplace=True)

    # Normaliza Cabeçalho, Coluna de Indexes e Valores Numericos
    time_series.dataframe.iloc[0, :] = norm_header(
        time_series.dataframe.iloc[0, :]
    )
    time_series = norm_index_column(time_series)
    time_series = norm_numeric_values(time_series)

    return time_series


def norm_all_time_series(
    all_time_series: List[TimeSeries],
) -> List[TimeSeries]:
    for time_series in all_time_series:
        time_series = norm_time_series(time_series)

    return all_time_series
