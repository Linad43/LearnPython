from datetime import datetime


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


def mask_account_card(input_account_card: str) -> str:
    """получение из полного наименования  счета или карточки,
    только числа счета или карты
    и передача данных далее get_mask_account или get_mask_card_number
    соответственно"""
    list_input_account_card = input_account_card.split(" ")
    for name_card in list_input_account_card:
        if name_card.isdigit():
            if len(name_card) == 16:
                return get_mask_card_number(name_card)
            elif len(name_card) == 20:
                return get_mask_account(name_card)
            else:
                return "error input"
    return "error input"


def get_date(input_date_str: str) -> str:
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
        "%d %B %Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(input_date_str.strip(), fmt)
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            pass

    raise ValueError(f"Invalid date format: '{input_date_str}'")
