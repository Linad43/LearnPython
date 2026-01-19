def filter_by_state(input_list: list[map], state="EXECUTED") -> list[map]:
    result_list = []
    for element in input_list:
        if element["state"] == state:
            result_list.append(element)
    return result_list
