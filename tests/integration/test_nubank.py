import pandas as pd

import cronus_eater


def test_extract_raw():
    df = pd.read_excel(
        'tests/integration/data/nubank_3Q22.xlsx',
        sheet_name='Credit Oper. (Op. De Crédito)',
    )
    raw_time_series = cronus_eater.extract(df, mode='raw')
    assert len(raw_time_series) == 6


def test_extract_raw_pagseguro():
    df = pd.read_excel(
        'tests/integration/data/btg_3Q22.xlsx',
        sheet_name='InputSite_Highlights',
    )
    raw_time_series = cronus_eater.extract(df, mode='raw')
    assert len(raw_time_series) == 6


def test():
    target_df = pd.DataFrame(
        {
            0: ['First', pd.NA, '1', '2', '3', '4'],
            1: ['Second', pd.NA, '1', '2', '3', '4'],
            2: ['Third', pd.NA, '1', '2', '3', '4'],
            3: ['Fourth', pd.NA, '1', '2', '3', '4'],
        }
    )

    s = target_df.iloc[0].to_dict()
    print(s)
