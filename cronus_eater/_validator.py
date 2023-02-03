import re
from typing import Any

import numpy as np
import pandas as pd


def is_blank_value(value: Any) -> bool:

    if pd.isnull(value):
        return True

    if len(str(value).strip()) == 0:
        return True

    if str(value).strip().lower() in ('-', 'none', 'null', 'nan'):
        return True

    return False


def __is_normal_float(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]+(([.]|[,])[\d]+)?$', value):
        return True

    return False


def __is_float_with_comma_sep(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]{1,3}([,][\d]{3})*([.][\d]+)?$', value):
        return True

    return False


def __is_float_with_dot_sep(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]{1,3}([.][\d]{3})*([,][\d]+)?$', value):
        return True

    return False


def __is_float_with_space_sep(value: str) -> bool:
    if re.match(
        r'[$]?[\s]?[-]?[\d]{1,3}([\s][\d]{3})*(([.]|[,])[\d]+)?$', value
    ):
        return True

    return False


def __is_percent(value: str) -> bool:
    if re.match(r'[-]?[\d]+(([.]|[,])[\d]+)?[\s]?[%]$', value):
        return True

    return False


def is_financial_number(value: Any) -> bool:
    if is_blank_value(value):
        return False

    text = str(value).strip()

    if (
        __is_normal_float(text)
        or __is_float_with_dot_sep(text)
        or __is_float_with_comma_sep(text)
        or __is_float_with_space_sep(text)
        or __is_percent(text)
    ):
        return True

    return False
