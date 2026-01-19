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
