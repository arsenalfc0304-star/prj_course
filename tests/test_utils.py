import pytest
from unittest.mock import Mock, patch
from src.utils import load_json, read_data_from_excel, sort_by_date
import pandas as pd

def test_load_json():
    assert load_json("data/operations1.json") == []
    assert load_json("data/user_settings.json") == {
  "user_currencies": ["USD", "EUR"],
  "user_stocks": ["AAPL", "AMZN", "GOOGL"]
}


def test_read_data_from_excel_with_mock(sample_df):
    mock_read_excel = Mock(return_value=sample_df)
    pd.read_excel = mock_read_excel
    result = read_data_from_excel("data/operations_excel.xlsx")
    assert result.to_dict(orient="records") == [{'id': 1, 'state': 'CANCELED'}, {'id': 2, 'state': 'CANCELED'}]


def test_sort_by_date(dicts: list) -> list:
    assert sort_by_date(dicts) == [
    {"id": 939719570, "state": "EXECUTED", "Дата операции": "30.06.2018 02:08:58"},
    {"id": 594226727, "state": "CANCELED", "Дата операции": "12.09.2018 21:27:25"},
    {"id": 615064591, "state": "CANCELED", "Дата операции": "14.10.2018 08:21:33"},
    {"id": 41428829, "state": "EXECUTED", "Дата операции": "03.07.2019 18:35:29"}
]