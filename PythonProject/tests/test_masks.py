from PythonProject.src import masks


def test_get_list_card_numbers():
    assert (masks.get_list_card_numbers("7000792289606361")
            == ["7000", "7922", "8960", "6361"])


def test_get_mask_card_number():
    assert (masks.get_mask_card_number("7000792289606361")
            == "7000 79** ****6361")


def test_get_mask_account():
    assert (masks.get_mask_account("73654108430135874305")
            == "**4305")
