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
    return sorted(dict_list, key=lambda x: x["Сумма платежа"], reverse=descending)