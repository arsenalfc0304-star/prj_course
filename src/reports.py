from typing import Optional
import pandas as pd
import datetime
from utils import read_data_from_excel


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    :param transactions:
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


    return transactions.loc[mask]


print(spending_by_category(read_data_from_excel("data/operations.xlsx"), "Супермаркеты", "2021-11-28 01:02:02"))


def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if filename == "":
                print(f"{func.__name__} ok")
            else:
                with open(filename, "a") as file:
                    file.write(f"{func.__name__} ok\n")
            return result
        except Exception as e:
            if filename == "":
                print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
            else:
                with open(filename, "a") as file:
                    file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})\n")

    return wrapper


return decorator