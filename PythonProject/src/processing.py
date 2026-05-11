import re
import logging

from pandas.core.computation.common import result_type_many

logger = logging.getLogger(__name__)


def filter_by_state(input_list: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """Фильтр по состоянию, и возврат нового листа"""
    result_list = []
    for element in input_list:
        if element["state"] == state:
            result_list.append(element)
    return result_list


def sort_by_date(input_list: list[dict[str, int | str]], reverse: bool = True) -> list[dict[str, int | str]]:
    """Сортировка по дате, и возврат нового листа"""
    return sorted(input_list, key=lambda p: p["date"], reverse=reverse)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтр словарей, у которых в описании есть данная строка"""
    logger.debug(f"Start process_bank_search(data, search:'{search}'")
    pattern = re.compile(pattern=search, flags=re.IGNORECASE)
    result: list[dict] = []
    for element in data:
        if re.search(pattern, element["description"]):
            result.append(element)
    logger.debug(f"End process_bank_search(data, search:'{search}'")
    return result
