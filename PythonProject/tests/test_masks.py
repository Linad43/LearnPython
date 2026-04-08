import pytest

from src import masks


@pytest.mark.parametrize(
    "input_number_card, expected",
    [("7000792289606361", ["7000", "7922", "8960", "6361"]), ("70007436792289606361", ["error input"])],
)
def test_get_list_card_numbers(input_number_card: str, expected: list[str]) -> None:
    """Тест разделения номера карты на секции по четыре цифры"""
    assert masks.get_list_card_numbers(input_number_card) == expected


def test_get_mask_card_number() -> None:
    """Тест добавления маски к номеру карты"""
    assert masks.get_mask_card_number("7000792289606361") == "7000 79** ****6361"


@pytest.mark.parametrize(
    "input_number_card, expected",
    [("73654108430135874305", "**4305"), ("7000792289606361", "error input")],
)
def test_get_mask_account(input_number_card: str, expected: str) -> None:
    """Тест добавления маски к номеру счета"""
    assert masks.get_mask_account(input_number_card) == expected
