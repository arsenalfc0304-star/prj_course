import json
import datetime
from utils import (
    select_greeting,
    read_data_from_excel,
    sort_by_amount,
    get_cards,
    get_card_total_amount,
    load_json,
    sort_by_date,
    format_transactions,
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
    most_valuable_transactions = sort_by_amount(selected_data)[0:5]
    cards = get_cards(selected_data)
    formatted_card_information = []
    for card in cards:
        formatted_card_information.append(
            {
                "last_digits": card[1:],
                "total_spent": get_card_total_amount(selected_data, card),
                "cashback": get_card_total_amount(selected_data, card) / 100,
            }
        )

    message = {
        "greeting": select_greeting(int(date_time.strip()[11:13])),
        "cards": formatted_card_information,
        "top_transactions": format_transactions(most_valuable_transactions),
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
