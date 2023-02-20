# Cronus Eater: A simple tool to get time series from spreadsheets

<div align="center">
  <img width="450" height="278" src="https://github.com/BrenoJesusFernandes/cronus-eater/blob/5e3a88709eeb845fa24b1dff5b9d3039a88c3d9c/docs/img/cronus-eater-logo.png"><br>
</div>

[![Test](https://github.com/BrenoJesusFernandes/cronus-eater/actions/workflows/test.yaml/badge.svg)](https://github.com/BrenoJesusFernandes/cronus-eater/actions/workflows/test.yaml) [![Python: 3.7 | 3.8 | 3.9 | 3.10 | 3.11](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://pypi.org/project/cronus-eater/)  [![Code style: blue](https://img.shields.io/badge/code%20style-blue-blue.svg)](https://github.com/grantjenks/blue) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/BrenoJesusFernandes/cronus-eater/blob/main/LICENSE)

Extract and normalize time series from any spreadsheet with differents patterns.


### Where is the data I want?

```python

import pandas as pd

raw_dataframe = pd.read_excel(
        'tests/data/nubank_3Q22.xlsx', sheet_name='Credit Oper. (Op. De Crédito)', header=None 
)

raw_dataframe.head()

```

|   | 0	| 1 |	2 |	3 |	4 |	5 |	6 |	7 |	8 |
|---|---|---|---|---|---|---|---|---|---|
 | 0 | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	
 | 1 | 	NaN | 	Nu Holdings Ltd. | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	
 | 2 | 	NaN | 	Credit Operations | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	
 | 3 | 	NaN | 	Amounts in thousands of US$ | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	
 | 4 | 	NaN | 	Back to Contents | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	NaN | 	

### Let's devours this times series  

```python

import cronus_eater
times_series_df = cronus_eater.find_time_series(raw_dataframe)
times_series_df.head()

```


|	   |Numeric Index |	Index |	Order |	Time |	Value |
|----|--------------|-------|-------|------|---------|
| 0	 | 12 |	Receivables - current |	1 |	3T22 |	3509311 |
| 1	 | 13 |	Receivables - installments |	1 |	3T22 |	3598374 |
| 2	 | 14 |	Receivables - revolving |	1 |	3T22 |	691915 |
| 3	 | 15 |	Total receivables |	1 |	3T22 |	7799600 |
| 4	 | 16 |	Fair value adjustment - portfolio hedge |	1 |	3T22 |	-61 |

## Where to get it

The source code is currently hosted on GitHub at: <https://github.com/BrenoJesusFernandes/cronus-eater>

Binary installers for the latest released version is going to available at the [Python Package Index (PyPI)](https://pypi.org/project/cronus-eater).


```sh
pip install cronus-eater
# or through poetry
poetry add cronus-eater@latest
```

## License

[MIT](LICENSE)

## Documentation

You can find [here](docs/)


 