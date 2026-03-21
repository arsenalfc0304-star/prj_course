from reports import spending_by_category
from services import search_transactions
from utils import read_data_from_excel
from views import main_func

main_func("2021-10-28 01:02:02")
search_transactions(read_data_from_excel("data/operations.xlsx").to_dict(orient="records"), "Перевод")
spending_by_category(read_data_from_excel("data/operations.xlsx"), "Супермаркеты", "2021-11-28 01:02:02")
