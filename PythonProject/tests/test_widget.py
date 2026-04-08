import pytest

from PythonProject.src import widget


@pytest.mark.parametrize("input_account_card, expected",
                         [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** ****6361"),
                          ("Maestro 7000792289606361", "Maestro 7000 79** ****6361"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(input_account_card, expected):
    assert widget.mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** ****6361"


def test_get_date():
    assert widget.get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
