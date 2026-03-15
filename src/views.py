import json
import datetime
from utils import (
    select_greeting,
    read_data_from_excel,
    sort_by_amount,
    get_cards,
    get_card_total_expenses,
    load_json,
    sort_by_date,
    format_transactions,
    get_api_currency_rate,
    get_api_stock_price
)


def main_func(date_time: str) -> json:
    raw_data = (read_data_from_excel("data/operations.xlsx")).to_dict(orient="records")
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
                "total_spent": abs(round(get_card_total_expenses(selected_data, card), 2)),
                "cashback": abs(round(get_card_total_expenses(selected_data, card) / 100, 2))
            }
        )
    user_settings = load_json("data/user_settings.json")
    formatted_currency_data = []
    for currency in user_settings['user_currencies']:
        formatted_currency_data.append({"currency": currency, "rate": round(get_api_currency_rate(currency), 2)})

    formatted_stock_data = []
    for stock in user_settings['user_stocks']:
        formatted_stock_data.append({"stock": stock, "price": get_api_stock_price(stock)})

    message = {
        "greeting": select_greeting(int(date_time.strip()[11:13])),
        "cards": formatted_card_information,
        "top_transactions": format_transactions(most_valuable_transactions),
        "currency_rates": formatted_currency_data,
        "stock_prices": formatted_stock_data
    }
    return json.dumps(message, ensure_ascii=False)


print(main_func("2021-10-28 01:02:02"))
