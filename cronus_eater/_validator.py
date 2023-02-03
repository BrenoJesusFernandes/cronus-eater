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
