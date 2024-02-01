import pandas as pd
from loguru import logger

import cronus_eater
from cronus_eater import _converter


def main():
    logger.info('Reading File ...')
    raw_dataframes = pd.read_excel(
        'tests/integration/data/nubank_3Q22.xlsx', header=None, sheet_name=None
    )

    logger.info('Processing Time Series ...')
    times_series_df = cronus_eater.extract_many(raw_dataframes, mode='tidy')

    logger.info(times_series_df)


if __name__ == '__main__':
    main()
