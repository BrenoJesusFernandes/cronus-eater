from typing import Dict, Union

import pandas as pd
from loguru import logger

from cronus_eater import _extractor, _normalizer


def main():
    logger.info('Reading File ...')
    raw_dataframes = pd.read_excel(
        'tests/data/test.xlsx', header=None, sheet_name=None
    )

    logger.info('Processing Time Series ...')
    times_series = _extractor.find_all_time_series(raw_dataframes)

    logger.info('Normalizing Time Series ...')
    _normalizer.norm_time_series(times_series)

    logger.info('Consolidating Data ...')
    times_series_df = pd.concat([serie.dataframe for serie in times_series])

    logger.info('Saving Data ...')
    times_series_df.to_excel('xablau.xlsx')


if __name__ == '__main__':
    main()
