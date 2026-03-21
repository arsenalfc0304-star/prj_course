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


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]

@pytest.fixture
def category() -> str:
    return "Супермаркеты"
