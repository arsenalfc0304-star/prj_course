def select_greeting(hour_of_day: int):
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
