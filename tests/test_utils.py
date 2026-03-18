import pytest
from unittest.mock import Mock, patch
from src.utils import load_json, read_data_from_excel
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
