import pandas as pd
from loguru import logger

from cronus_eater import _extractor


def test_find_start_row_index():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    assert _extractor.find_start_row_index(df, 1) == 24


def test_find_start_row_column():
    df = pd.read_excel('tests/data/source_0.xlsx', header=None)
    star_row, start_column = _extractor.find_start_row_column(df)

    assert star_row == 24
    assert start_column == 1
