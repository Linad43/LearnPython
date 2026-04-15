from typing import Any, Generator


def filter_by_currency(
        transactions: list[dict[str, int | str | dict[str, str | dict[str, str]]]],
        filter_currency_code: str
) -> Generator[dict[str, int | str | dict[str, str | dict[str, str]]], Any, None]:
    """
    Функция должна возвращать итератор,
    который поочередно выдает транзакции,
    где валюта операции соответствует заданной
    """
    # result = filter(lambda x: x["operationAmount"]["currency"]["code"] == filter_currency_code, transactions)
    for iter in filter(lambda x: x["operationAmount"]["currency"]["code"] == filter_currency_code, transactions):
        yield iter
    return


def transaction_descriptions(
        transactions: list[dict[str, int | str | dict[str, str | dict[str, str]]]]
) -> Generator[int | str | dict[str, str | dict[str, str]], None, None]:
    for iter in transactions:
        yield iter["description"]
    return


def card_number_generator(num_begin, num_end) -> Generator[str, Any, None]:
    for iter in range(num_begin, num_end+1):
        str_iter = str(iter)
        while len(str_iter) < 16:
            str_iter = f"0{str_iter}"
        str_iter = f"{str_iter[:4]} {str_iter[4:8]} {str_iter[8:12]} {str_iter[12:]}"
        yield str_iter
    return
