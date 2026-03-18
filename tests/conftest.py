import pytest
import pandas as pd

@pytest.fixture
def sample_df():
    sample_dict = {"id": [1, 2], "state": ["CANCELED", "CANCELED"]}
    return pd.DataFrame(sample_dict)

@pytest.fixture
def dicts():
    return [
    {"id": 41428829, "state": "EXECUTED", "Дата операции": "03.07.2019 18:35:29"},
    {"id": 939719570, "state": "EXECUTED", "Дата операции": "30.06.2018 02:08:58"},
    {"id": 594226727, "state": "CANCELED", "Дата операции": "12.09.2018 21:27:25"},
    {"id": 615064591, "state": "CANCELED", "Дата операции": "14.10.2018 08:21:33"},
]