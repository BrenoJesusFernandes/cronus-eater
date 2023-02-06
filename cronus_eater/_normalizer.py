from typing import Any, List

import numpy as np
import pandas as pd

from cronus_eater import _validator
from cronus_eater.model import TimeSeries


def norm_blank_value(value: Any) -> Any:
    if _validator.is_blank_value(value):
        return np.nan

    return value


def norm_header(time_series: TimeSeries) -> None:
    ...


def norm_index_column(time_series: TimeSeries) -> None:
    ...


def norm_numeric_values(time_series: TimeSeries) -> None:
    ...


def norm_numerical_values(time_series: TimeSeries) -> None:
    ...


def norm_time_series(time_series: List[TimeSeries]) -> None:
    ...
