from typing import Optional
import pandas as pd
import datetime
from utils import read_data_from_excel


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    :param transactions:
    """
    if datetime.datetime.strptime(transaction["Дата операции"][3:5], "%m) > 11:

    date_filtered_transactions = transactions.loc[transactions['Дата операции']
    return transactions.loc[transactions.Категория.isin([category])]


print(spending_by_category(read_data_from_excel("data/operations.xlsx"), 'Супермаркеты'))