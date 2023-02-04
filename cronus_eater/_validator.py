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


def is_normal_number(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]+(([.]|[,])[\d]+)?$', value):
        return True

    return False


def is_number_with_comma_sep(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]{1,3}([,][\d]{3})*([.][\d]+)?$', value):
        return True

    return False


def is_number_with_dot_sep(value: str) -> bool:
    if re.match(r'[$]?[\s]?[-]?[\d]{1,3}([.][\d]{3})*([,][\d]+)?$', value):
        return True

    return False


def is_number_with_space_sep(value: str) -> bool:
    if re.match(
        r'[$]?[\s]?[-]?[\d]{1,3}([\s][\d]{3})*(([.]|[,])[\d]+)?$', value
    ):
        return True

    return False


def is_percent_number(value: str) -> bool:
    if re.match(r'[-]?[\d]+(([.]|[,])[\d]+)?[\s]?[%]$', value):
        return True

    return False


def is_financial_number(value: Any) -> bool:
    if is_blank_value(value):
        return False

    text = str(value).strip()

    if (
        is_normal_number(text)
        or is_number_with_dot_sep(text)
        or is_number_with_comma_sep(text)
        or is_number_with_space_sep(text)
        or is_percent_number(text)
    ):
        return True

    return False
