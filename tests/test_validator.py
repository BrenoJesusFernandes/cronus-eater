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
