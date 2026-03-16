from typing import Optional
import pandas as pd
import datetime
from utils import read_data_from_excel


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    :param transactions:
    """
    if date is None:
        date_time = datetime.datetime.now()
    return transactions.loc[
        transactions.Категория.isin([category])
        & (
            (datetime.datetime.strptime(transactions["Дата операции"], "%d.%m.%Y %H:%M:%S").month - 3)
            >= date_time.month
        )
    ]


print(spending_by_category(read_data_from_excel("data/operations.xlsx"), "Супермаркеты"))
