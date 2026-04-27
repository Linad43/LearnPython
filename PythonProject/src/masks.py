import logging

logger = logging.getLogger(__name__)


def get_list_card_numbers(input_number_card: str) -> list[str]:
    """получение листа номеров карточки по четыре"""
    logger.debug(f"Start get_list_card_numbers(input_number_card:'{input_number_card}')")
    list_card = input_number_card.split(" ")
    logger.debug(f"len(list_card):{len(list_card)}")
    if len(list_card) == 1:
        logger.debug(f"list_card[0]: {list_card[0]}")
        if len(list_card[0]) != 16:
            logger.critical(f"len(list_card[0]):{len(list_card[0])}!=16")
            return ["error input"]
        list_card = [
            list_card[0][:4],
            list_card[0][4:8],
            list_card[0][8:12],
            list_card[0][12:],
        ]
        logger.debug(f"get_list_card_numbers(input_number_card:'{input_number_card}') done")
    return list_card


def get_mask_card_number(input_number_card: str) -> str:
    """получение маски карточки"""
    logger.debug(f"Start get_mask_card_number(input_number_card:'{input_number_card}')")
    list_card = get_list_card_numbers(input_number_card)
    logger.debug(f"get_mask_card_number(input_number_card:'{input_number_card}') done")
    return list_card[0] + " " + list_card[1][:2] + "** ****" + list_card[3]


def get_mask_account(input_number_card: str) -> str:
    """получение маски номера счета"""
    logger.debug("Start get_mask_account(input_number_card:'{input_number_card}')")
    if len(input_number_card) != 20:
        logger.critical(f"len(input_number_card):{len(input_number_card)}!=20")
        return "error input"
    logger.debug(f"get_mask_account(input_number_card:'{input_number_card}') done")
    return "**" + input_number_card[-4:]
