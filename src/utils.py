from typing import Optional

import pandas as pd
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
apikey = os.getenv("API_KEY")

def select_greeting(hour_of_day: int) -> str:
    """
    принимает текущий час,
    возвращает приветствие
    """
    if 0 <= hour_of_day < 6:
        return "Доброй ночи"
    elif 6 <= hour_of_day < 12:
        return "Доброе утро"
    elif 12 <= hour_of_day < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"


def read_data_from_excel(path: str) -> list:
    """
    принимает путь к файлу Excel,
    выдает список словарей с транзакциями
    """
    data = pd.read_excel(path)
    return data.to_dict(orient="records")


def sort_by_amount(dict_list: list, descending: bool = True) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(dict_list, key=lambda x: abs(x["Сумма платежа"]), reverse=descending)


def get_cards(dict_list: list):
    cards_set = set()
    for transaction in dict_list:
        if str(transaction['Номер карты'])[1:].isdigit():
            cards_set.add(transaction['Номер карты'])
    return cards_set


def get_card_transactions(dict_list: list, cards_set: set):
    total_amount_list = []
    for card in cards_set:
        total_amount = 0
        for transaction in dict_list:
            if transaction['Номер карты'] == card:
                total_amount += transaction['Сумма операции']
        total_amount_list.append(abs(total_amount))
    return total_amount_list


def get_api_convertion_to_rub(transaction: dict) -> float:
    """
    обращается к внешнему API (Exchange Rates Data API) для получения текущего курса валют
    и конвертации суммы операции из USD или EUR в рубли
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": float(transaction["operationAmount"]["amount"]),
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    result = response.json()["result"]
    if status_code == 200:
        return float(result)
    else:
        return 0.0


def load_json(path):
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return []


def sort_by_date(dict_list: list, descending: bool = False) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(dict_list, key=lambda x: x["Дата платежа"], reverse=descending)


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    """

    """
    pass