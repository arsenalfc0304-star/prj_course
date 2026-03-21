from src.reports import spending_by_category
import pandas as pd
from src.utils import read_data_from_excel


def test_spending_by_category(transactions: pd.DataFrame, category: str) -> pd.DataFrame:
    assert spending_by_category(read_data_from_excel("data/operations.xlsx"), category, "2021-12-02 01:02:02").to_dict(orient="records")[0]['Категория'] == 'Супермаркеты'