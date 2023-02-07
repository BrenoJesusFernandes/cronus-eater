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


def test_is_year():
    assert _validator.is_year(1998)
    assert _validator.is_year(2022)
    assert _validator.is_year(2022.1)
    assert _validator.is_year(2022.12)

    assert _validator.is_year(1998.1)
    assert _validator.is_year(1998.12)

    assert _validator.is_year('2022 1')
    assert _validator.is_year('2022,1')
    assert not _validator.is_year('22 1')
    assert not _validator.is_year('22,1')
    assert not _validator.is_year('22 12')
    assert not _validator.is_year('22,12')

    assert not _validator.is_year('22023.14')
    assert not _validator.is_year('2023|0')
    assert not _validator.is_year(1800)
    assert not _validator.is_year(3000)


def test_is_number_type():
    assert _validator.is_number_type(0.0)
    assert _validator.is_number_type(0)
    assert _validator.is_number_type(np.float64(0.0))
    assert _validator.is_number_type(np.int64(0))


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
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    invalid_row = df.iloc[1, 1:]
    valid_row = df.iloc[24, 1:]
    empty_row = df.iloc[3, 1:]

    assert _validator.is_time_series_row(valid_row)
    assert not _validator.is_time_series_row(invalid_row)
    assert not _validator.is_time_series_row(empty_row)


def test_is_text_row():
    df = pd.read_excel('tests/data/source.xlsx', header=None)
    mix_row = df.iloc[24, 1:11]
    text_row = df.iloc[21, 1:11]
    empty_row = df.iloc[3, 1:11]

    assert _validator.is_text_row(text_row)
    assert not _validator.is_text_row(mix_row)
    assert not _validator.is_text_row(empty_row)


def test_is_date_time():
    assert _validator.is_date_time(datetime.now())

    assert _validator.is_date_time(' 31/02/2022 ')
    assert _validator.is_date_time(' 10-10-2022 ')
    assert _validator.is_date_time(' 31/02/2022 8:26:00.39 ')

    assert _validator.is_date_time(' 3Q22 ')
    assert _validator.is_date_time(' 3T22 ')
    assert _validator.is_date_time(' 3Q2022 ')
    assert _validator.is_date_time(' 3T2022 ')
    assert _validator.is_date_time(' 3Q 2022 ')
    assert _validator.is_date_time(' 3T 2022 ')

    assert not _validator.is_date_time(' 5Q22 ')
    assert not _validator.is_date_time(' 5T22 ')
    assert not _validator.is_date_time(' 5Q2022 ')
    assert not _validator.is_date_time(' 5T2022 ')

    assert not _validator.is_date_time(' 0Q22 ')
    assert not _validator.is_date_time(' 0T22 ')
    assert not _validator.is_date_time(' 0Q2022 ')
    assert not _validator.is_date_time(' 0T2022 ')

    assert _validator.is_date_time(' 1M22 ')
    assert _validator.is_date_time(' 1M2022 ')
    assert _validator.is_date_time(' 1M 22 ')
    assert _validator.is_date_time(' 1M 2022 ')

    assert not _validator.is_date_time(' 0M22 ')
    assert not _validator.is_date_time(' 0M2022 ')

    assert not _validator.is_date_time(' 13M22 ')
    assert not _validator.is_date_time(' 13M2022 ')
