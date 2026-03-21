import datetime
import json
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from pandas.core.interchange.dataframe_protocol import DataFrame
from src.loggers import utils_logger

load_dotenv()
currency_apikey = os.getenv("CURRENCY_API_KEY")
stock_apikey = os.getenv("STOCK_API_KEY")


def select_greeting(hour_of_day: int) -> str:
    """
    принимает текущий час,
    возвращает приветствие соответственно времени суток
    """
    if 0 <= hour_of_day < 6:
        return "Доброй ночи"
    elif 6 <= hour_of_day < 12:
        return "Доброе утро"
    elif 12 <= hour_of_day < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"


def load_json(path) -> list[dict]:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            utils_logger.info(f"возвращаем список словарей с данными о финансовых транзакциях из файла {path}")
            return data
    except Exception as e:
        utils_logger.error(f"произошла ошибка получения данных о транзакции {e}")
        return []


def read_data_from_excel(path: str) -> DataFrame:
    """
    принимает путь к файлу Excel,
    возвращает DataFrame с транзакциями
    """
    data = pd.read_excel(path)
    return data


def sort_by_date(dict_list: list, descending: bool = False) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(
        dict_list,
        key=lambda x: datetime.datetime.strptime(x["Дата операции"], "%d.%m.%Y %H:%M:%S"),
        reverse=descending,
    )


def sort_by_amount(dict_list: list, descending: bool = True) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по Сумме платежа
    """
    return sorted(dict_list, key=lambda x: abs(x["Сумма платежа"]), reverse=descending)


def get_cards(transactions: list) -> set:
    """
    принимает список словарей с транзакциями,
    возвращает DataFrame с транзакциями
    """
    cards_set = set()
    for transaction in transactions:
        if str(transaction["Номер карты"])[1:].isdigit():
            cards_set.add(transaction["Номер карты"])
    return cards_set


def get_card_total_expenses(transactions: list, card: str) -> float:
    """
    принимает список словарей с транзакциями по карте,
    возвращает значение суммарных трат по карте
    """
    total_expenses = 0
    for transaction in transactions:
        if transaction["Номер карты"] == card and transaction["Сумма операции"] < 0:
            total_expenses += transaction["Сумма операции"]
    return total_expenses


def get_api_currency_rate(currency: str) -> float:
    """
    обращается к внешнему API (Exchange Rates Data API) для получения текущего курса валюты
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": 1.0,
        "from": currency,
        "to": "RUB",
    }
    headers = {"apikey": currency_apikey}

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    if status_code == 200:
        result = response.json()["result"]
        return float(result)
    else:
        return 0.0


def get_api_stock_price(stock: str) -> float:
    """
    обращается к внешнему API (www.alphavantage.co) для получения текущего курса акции
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={stock_apikey}"

    response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        result = data["Time Series (Daily)"][last_refreshed]["4. close"]
        return result
    else:
        return 0.0


def format_transactions(transactions: list) -> list[dict]:
    """
    принимает список словарей с транзакциями,
    возвращает отформатированный список словарей с транзакциями
    """
    formatted_transactions = []
    for transaction in transactions:
        formatted_transactions.append(
            {
                "date": transaction["Дата операции"][0:10],
                "amount": transaction["Сумма операции"],
                "category": transaction["Категория"],
                "description": transaction["Описание"],
            }
        )
    return formatted_transactions
