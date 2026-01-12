def get_list_card_numbers(input_number_card: str) -> list[str]:
    """получение листа номеров карточки по четыре"""
    list_card = input_number_card.split(" ")
    if len(list_card) == 1:
        if len(list_card[0]) != 16:
            return ["error input"]
        list_card = [
            list_card[0][:4],
            list_card[0][4:8],
            list_card[0][8:12],
            list_card[0][12:],
        ]
    return list_card


def get_mask_card_number(input_number_card: str) -> str:
    """получение маски карточки"""
    list_card = get_list_card_numbers(input_number_card)
    return list_card[0] + " " + list_card[1][:2] + "** ****" + list_card[3]


def get_mask_account(input_number_card: str) -> str:
    """получение маски номера счета"""
    if len(input_number_card) != 20:
        return "error input"
    return "**" + input_number_card[-4:]
