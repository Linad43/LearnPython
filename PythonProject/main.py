import src.processing
from src.widget import get_date, mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

list_test: list_test[dict[str, int | str]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(src.processing.filter_by_state(list_test))
print(src.processing.filter_by_state(list_test, "CANCELED"))
print(src.processing.sort_by_date(list_test))
print(src.processing.sort_by_date(list_test, False))
