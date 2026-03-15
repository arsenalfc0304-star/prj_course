from typing import Optional
import pandas as pd
import datetime
from utils import read_data_from_excel


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """ """
    pass




spending_by_category(read_data_from_excel("data/operations.xlsx"))