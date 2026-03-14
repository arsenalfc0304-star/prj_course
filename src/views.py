import json
from utils import (
    select_greeting,
    read_data_from_excel,
    sort_by_amount,
    get_cards,
    get_card_transactions,
    load_json,
    sort_by_date,
)


def main_func(date_time: str) -> json:
    raw_data = read_data_from_excel("data/operations.xlsx")
    sorted_data = sort_by_date(raw_data)
    cards = get_cards(sorted_data)
    total_amount = get_card_transactions(sorted_data, cards)
    message = {
        "greeting": select_greeting(int(date_time.strip()[11:13])),
        "cards": [
            {"last_digits": "5814", "total_spent": 1262.00, "cashback": 12.62},
            {"last_digits": "7512", "total_spent": 7.94, "cashback": 0.08},
        ],
        "top_transactions": sort_by_amount(sorted_data)[0:5],
        # "top_transactions": [
        #     {
        #         "date": "21.12.2021",
        #         "amount": 1198.23,
        #         "category": "Переводы",
        #         "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        #     },
        #     {"date": "20.12.2021", "amount": 829.00, "category": "Супермаркеты", "description": "Лента"},
        #     {"date": "20.12.2021", "amount": 421.00, "category": "Различные товары", "description": "Ozon.ru"},
        #     {"date": "16.12.2021", "amount": -14216.42, "category": "ЖКХ", "description": "ЖКУ Квартира"},
        #     {"date": "16.12.2021", "amount": 453.00, "category": "Бонусы", "description": "Кешбэк за обычные покупки"},
        # ],
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
    print(type(data[0]["Дата платежа"]))


main_func("2026-02-28 01-02-02")
