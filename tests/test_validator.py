from datetime import datetime

import numpy as np

from cronus_eater import _validator


def test_is_blank_value():
    assert _validator.is_blank_value(np.nan)
    assert _validator.is_blank_value(None)

    assert not _validator.is_blank_value({})
    assert not _validator.is_blank_value(())
    assert not _validator.is_blank_value(datetime.now())
    assert not _validator.is_blank_value(object)

    assert _validator.is_blank_value('        ')
    assert _validator.is_blank_value('   -    ')
    assert _validator.is_blank_value('  NaN   ')
    assert _validator.is_blank_value('  Null  ')
