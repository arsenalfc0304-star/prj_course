import datetime
from typing import Optional

import pandas as pd

from src.loggers import reports_logger


def save_report_to_excel(file_name=None):
    """
    принимает необязательный аргумент - путь к файлу,
    сохраняет результат работы вложенной функции по вышеуказанному пути
    (если путь не задан, выбирается путь по умолчанию)
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if file_name is None:
                result.to_excel("data/report.xlsx")
            else:
                result.to_excel(file_name)
            return result

        return wrapper

    return decorator


@save_report_to_excel()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    принимает: датафрейм с транзакциями, название категории, опциональную дату
    (если дата не передана, то берется текущая дата),
    возвращает траты по заданной категории за последние три месяца (от переданной даты).
    """
    if date is None:
        end_date = datetime.datetime.now()
    else:
        end_date = pd.to_datetime(date)

    start_date = end_date - datetime.timedelta(days=90)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"])

    mask = (
        (transactions.Категория == category)
        & (transactions["Дата операции"] >= start_date)
        & (transactions["Дата операции"] <= end_date)
    )
    reports_logger.info(f"возвращаем траты по категории {category} за последние три месяца")
    return transactions.loc[mask]
