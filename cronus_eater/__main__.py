from typing import Dict, Union

import pandas as pd
from loguru import logger

from cronus_eater import _extractor, _normalizer


def main():
    logger.info('Reading File ...')
    raw_dataframes = pd.read_excel(
        'tests/data/nubank_3Q22.xlsx', header=None, sheet_name=None
    )

    logger.info('Processing Time Series ...')
    times_series_df = _extractor.find_all_time_series(raw_dataframes)

    logger.info('Saving Data ...')
    times_series_df.to_excel('xablau.xlsx')


if __name__ == '__main__':
    main()
