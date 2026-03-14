import json
import datetime
from utils import (
    select_greeting,
    read_data_from_excel,
    sort_by_amount,
    get_cards,
    get_card_transactions,
    load_json,
    sort_by_date,
    format_transaction
)


def main_func(date_time: str) -> json:
    raw_data = read_data_from_excel("data/operations.xlsx")
    sorted_data = sort_by_date(raw_data)
    selected_data = []
    for transaction in sorted_data:
        if datetime.datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S") >= datetime.datetime.strptime(
            date_time.strip(), "%Y-%m-%d %H:%M:%S"
        ):
            selected_data.append(transaction)
    cards = get_cards(selected_data)
    total_amount = get_card_transactions(selected_data, cards)
    most_valuable_transactions = sort_by_amount(selected_data)[0:5]
    most_valuable_transactions_formatted = []
    for transaction in most_valuable_transactions:
        most_valuable_transactions_formatted.append(format_transaction(transaction))
    message = {
        "greeting": select_greeting(int(date_time.strip()[11:13])),
        "cards": [
            {"last_digits": "5814", "total_spent": 1262.00, "cashback": 12.62},
            {"last_digits": "7512", "total_spent": 7.94, "cashback": 0.08},
        ],
        "top_transactions": most_valuable_transactions_formatted,
        "currency_rates": load_json("data/user_settings.json"),
        #    [{"currency": "USD", "rate": 73.21}, {"currency": "EUR", "rate": 87.08}],
        # "stock_prices": [
        #     {"stock": "AAPL", "price": 150.12},
        #     {"stock": "AMZN", "price": 3173.18},
        #     {"stock": "GOOGL", "price": 2742.39},
        #     {"stock": "MSFT", "price": 296.71},
        #     {"stock": "TSLA", "price": 1007.08},
        # ],
    }
    print(json.dumps(message, ensure_ascii=False))
    print(cards)
    print(total_amount)


main_func("2021-11-28 01:02:02")
