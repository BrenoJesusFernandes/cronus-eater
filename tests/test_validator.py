from datetime import datetime

import numpy as np
import pandas as pd

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


def test_is_normal_float():
    assert _validator.is_financial_number('0')
    assert _validator.is_financial_number('-1023213')
    assert _validator.is_financial_number('1023213')
    assert _validator.is_financial_number('$ -1023213')
    assert _validator.is_financial_number('$ 1023213')


def test_is_float_with_comma_sep():
    assert _validator.is_financial_number('0.0')
    assert _validator.is_financial_number('0,0')
    assert _validator.is_financial_number('-10000231.132123')
    assert _validator.is_financial_number('-10000231,132123')
    assert _validator.is_financial_number('10000231.132123')
    assert _validator.is_financial_number('10000231,132123')
    assert _validator.is_financial_number('$ 10000231.132123')
    assert _validator.is_financial_number('$ 10000231,132123')


def test_is_float_with_dot_sep():
    assert _validator.is_financial_number('10,000,231')
    assert _validator.is_financial_number('-10,000,231')
    assert _validator.is_financial_number('10,000,231.24')
    assert _validator.is_financial_number('-10,000,231.24')
    assert _validator.is_financial_number('$ 10,000,231.24')
    assert _validator.is_financial_number('$ -10,000,231.24')


def test_is_float_with_space_sep():
    assert _validator.is_financial_number('10.000.231')
    assert _validator.is_financial_number('-10.000.231')
    assert _validator.is_financial_number('10.000.231,24')
    assert _validator.is_financial_number('-10.000.231,24')
    assert _validator.is_financial_number('$ 10.000.231,24')
    assert _validator.is_financial_number('$ -10.000.231,24')


def test_is_percent_number():
    assert _validator.is_financial_number('17.37 %')
    assert _validator.is_financial_number('-1.1 %')
    assert _validator.is_financial_number('-1,1 %')
    assert _validator.is_financial_number('1,1 %')


def test_is_financial_number():
    assert _validator.is_financial_number('  -13,1415 %  ')
    assert _validator.is_financial_number('  $ -353143  ')
    assert _validator.is_financial_number(' $ -10.000.231,244123  ')
    assert _validator.is_financial_number('  $ 10,000,231.244123 ')
    assert _validator.is_financial_number('  $ 10 000 231.244123  ')

    assert not _validator.is_financial_number('V1.2')
    assert not _validator.is_financial_number('1.234.23')
    assert not _validator.is_financial_number('this is a text')
    assert not _validator.is_financial_number('NaN ')


def test_is_time_series_row():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    invalid_row = df.iloc[1, 1:]
    valid_row = df.iloc[24, 1:]
    empty_row = df.iloc[3, 1:]

    assert _validator.is_time_series_row(valid_row)
    assert not _validator.is_time_series_row(invalid_row)
    assert not _validator.is_time_series_row(empty_row)
