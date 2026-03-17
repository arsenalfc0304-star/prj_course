import json
import re


def search_transactions(transactions: list[dict], search: str) -> json:
    """
    принимает путь к файлу json, содержащему список словарей с данными о банковских операциях, и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка
    """
    filtered_transactions = []
    for transaction in transactions:
        for key in transaction.keys():
            if not re.search(search.lower(), str(transaction[key]).lower()) is None:
                filtered_transactions.append(transaction)
                continue
    return json.dumps(filtered_transactions)
