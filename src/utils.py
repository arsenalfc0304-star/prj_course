import pandas as pd


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
            cards_set.add(str(transaction['Номер карты'])[1:])
    return cards_set


def get_card_transactions(dict_list: list, cards_set: set):
    total_amount_set = set()
    for card in cards_set:
        total_amount = 0
        for transaction in dict_list:
            if transaction['Номер карты'] == card:
                total_amount += transaction['Сумма операции']
            total_amount_set.add(total_amount)
