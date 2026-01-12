def mask_account_card(input_account_card: str) -> str:
    """получение из полного наименования  счета или карточки,
    только числа счета или карты
    и передача данных далее get_mask_account или get_mask_card_number
    соответственно, и возврат полного
 имени с маской"""
    list_input_account_card = input_account_card.split(" ")
    for name_card in list_input_account_card:
        if name_card.isdigit():
            if len(name_card) == 16:
                return list_input_account_card(:-1) + get_mask_card_number(name_card)
            elif len(name_card) == 20:
                return list_input_account_card(:-1) + get_mask_account(name_card)
            else:
                return "error input"
    return "error input"


def get_date(date_str:str)->str:
    date_str=date_str.split("T")[0]
    result_date = date_str.split("-")
    return f"{result_date(2)}.{result_date(1)}.{result_date(0)}"