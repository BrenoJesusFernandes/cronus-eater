from typing import Dict, List, Union, overload

import pandas as pd
from typing_extensions import Literal

@overload
def extract(
    target: Union[pd.DataFrame, Dict[Union[str, int], pd.DataFrame]],
    mode: Literal['tidy'],
) -> pd.DataFrame: ...
@overload
def extract(
    target: Union[pd.DataFrame, Dict[Union[str, int], pd.DataFrame]],
    mode: Literal['tidy'] = 'tidy',
) -> pd.DataFrame: ...
@overload
def extract(
    target: Dict[Union[str, int], pd.DataFrame],
    mode: Literal['raw'] = 'raw',
) -> Dict[Union[str, int], List[pd.DataFrame]]: ...
@overload
def extract(
    target: pd.DataFrame,
    mode: Literal['raw'] = 'raw',
) -> Dict[Union[str, int], List[pd.DataFrame]]: ...
