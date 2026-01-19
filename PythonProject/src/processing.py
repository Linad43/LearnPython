def filter_by_state(input_list: list[map], state="EXECUTED") -> list[map]:
    result_list = []
    for element in input_list:
        if element["state"] == state:
            result_list.append(element)
    return result_list


def sort_by_date(input_list: list[map], reverse: bool = True) -> list[map]:
    return sorted(input_list, key=lambda p: p["date"], reverse=reverse)
