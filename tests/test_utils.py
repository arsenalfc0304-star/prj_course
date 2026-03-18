import pytest
from src.utils import load_json

def test_load_json():
    assert load_json("data/operations1.json") == []
    assert load_json("data/user_settings.json") == {
  "user_currencies": ["USD", "EUR"],
  "user_stocks": ["AAPL", "AMZN", "GOOGL"]
}