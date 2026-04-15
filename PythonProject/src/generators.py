from typing import Any, Generator


def filter_by_currency(
    transactions: list[dict[str, Any]], filter_currency_code: str
) -> Generator[dict[str, Any], Any, None]:
    """Генератор транзакций с заданной валютой."""
    # result = filter(lambda x: x["operationAmount"]["currency"]["code"] == filter_currency_code, transactions)
    for iter in filter(lambda x: x["operationAmount"]["currency"]["code"] == filter_currency_code, transactions):
        yield iter
    return


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """Генератор описаний транзакций."""
    for iter in transactions:
        yield iter["description"]
    return


def card_number_generator(num_begin: int, num_end: int) -> Generator[str, Any, None]:
    """Генератор номеров банковских карт."""
    for iter in range(num_begin, num_end + 1):
        str_iter = str(iter)
        while len(str_iter) < 16:
            str_iter = f"0{str_iter}"
        str_iter = f"{str_iter[:4]} {str_iter[4:8]} {str_iter[8:12]} {str_iter[12:]}"
        yield str_iter
    return
