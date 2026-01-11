import src.masks

print(src.masks.mask_account_card("Visa Platinum 7000792289606361"))
print(src.masks.mask_account_card("Maestro 7000792289606361"))
print(src.masks.mask_account_card("Счет 73654108430135874305"))
print(src.masks.get_date("2018-07-11"))
print(src.masks.get_date("11 July 2018"))
print(src.masks.get_date("11/07/2018"))
