from typing import Any

from cronus_eater import _validator


def blank_to_zero(value: Any) -> Any:
    if _validator.is_blank_value(value):
        return 0

    return value
