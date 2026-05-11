import logging
import re
from pathlib import Path

from src import external_api, fileops, processing, utils, widget

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - '%(name)s' - %(levelname)s: %(message)s",
    filemode="w",
    filename="logs/logs.log",
)
#
# print(widget.mask_account_card("Visa Platinum 7000792289606361"))
# print(widget.mask_account_card("Maestro 7000792289606361"))
# print(widget.mask_account_card("Счет 73654108430135874305"))
# print(widget.get_date("2024-03-11T02:26:18.671407"))
#
# list_test: list[dict[str, int | str]] = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# print(processing.filter_by_state(list_test))
# print(processing.filter_by_state(list_test, "CANCELED"))
# print(processing.sort_by_date(list_test))
# print(processing.sort_by_date(list_test, False))
# #
# path = Path(__file__).resolve().parent
# json_path = path / "data" / "operations.json"
# #
# transactions: list[dict] = utils.read_json_dict(json_path)
#
# # gen = generators.filter_by_currency(transactions, "USD")
# # print()
# # for iter in gen:
# #     print(iter)
# #
# # print()
# #
# #
# # @log()
# # def test_fun(x_in: int, y_in: int):
# #     return x_in / y_in
# #
# #
# # test_fun(1, 3)
#
# processing.process_bank_search(transactions, "перевод организации")
# categories = ["Перевод организации", "Открытие вклада"]
# processing.process_bank_operation(transactions, categories)


# Main menu
def main_menu():
    print("Программа: Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла\n")
    print("0. Выход\n")

    while True:
        try:
            case = int(input("Пользователь: "))
            print()
            break
        except ValueError:
            print("Некорректное значение. Повторите ввод (число от 0 до 3).\n")

    path_data = Path(__file__).resolve().parent / "data"
    # transactions: list[dict] = list()

    if case == 0:
        return
    if case == 1:
        print("Программа: Для обработки выбран JSON-файл.")
        json_path = path_data / "operations.json"
        transactions = utils.read_json_dict(json_path)
    if case == 2:
        print("Программа: Для обработки выбран CSV-файл.")
        csv_path = path_data / "transactions.csv"
        transactions = fileops.read_csv(csv_path, ";")
    if case == 3:
        print("Программа: Для обработки выбран XLSX-файл.")
        excel_path = path_data / "transactions_excel.xlsx"
        transactions = fileops.read_exel(excel_path)

    print()
    filters = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
        input_filter = input("Пользователь: ")
        print()
        pattern = re.compile(pattern=input_filter, flags=re.IGNORECASE)
        found = ""
        for filter_ in filters:
            if re.search(pattern, filter_):
                found = filter_
                break
        if found in filters:
            break
        else:
            print(f'Программа: Статус операции "{input_filter}" недоступен.\n')

    filtered_transactions = processing.filter_by_state(transactions, found)
    pattern_answer = ["да", "нет"]
    answer_bool = False

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет\n")
        answer = input("Пользователь: ")
        print()

        if answer.lower() in pattern_answer:
            answer_bool = True if answer.lower() == pattern_answer[0] else False
            break
        else:
            print("Некорректное значение. Повторите ввод (Да/Нет).\n")

    if answer_bool:
        pattern_sort = ["по возрастанию", "по убыванию"]
        while True:
            print("Программа: Отсортировать по возрастанию или по убыванию?\n")
            answer = input("Пользователь: ")
            print()
            if answer.lower() in pattern_sort:
                answer_bool = False if answer.lower() == pattern_sort[0] else True
                filtered_transactions = processing.sort_by_date(filtered_transactions, answer_bool)
                break
            else:
                print("Некорректное значение. Повторите ввод (по возрастанию/по убыванию).\n")

    while True:
        print("Программа: Выводить только рублевые транзакции? Да/Нет\n")
        answer = input("Пользователь: ")
        print()
        if answer.lower() in pattern_answer:
            for index in range(len(filtered_transactions)):
                if case == 1:
                    filtered_transactions[index]["operationAmount"]["amount"] = str(
                        external_api.convert_to_rub_dict(filtered_transactions[index])
                    )
                    filtered_transactions[index]["operationAmount"]["currency"]["code"] = "RUB"
                    filtered_transactions[index]["operationAmount"]["currency"]["name"] = "руб."
                else:
                    filtered_transactions[index]["amount"] = str(
                        external_api.convert_to_rub_dict(filtered_transactions[index])
                    )
                    filtered_transactions[index]["currency_code"] = "RUB"
                    filtered_transactions[index]["currency_name"] = "руб."
            break
        else:
            print("Некорректное значение. Повторите ввод (Да/Нет).\n")

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову")
        print("в описании? Да/Нет\n")
        answer = input("Пользователь: ")
        print()
        if answer.lower() in pattern_answer:
            # answer_bool = True if answer.lower() == pattern_answer[0] else False
            answer = input("По какому слову фильтровать: ")
            print()
            filtered_transactions = processing.process_bank_search(filtered_transactions, answer)
            break
        else:
            print("Некорректное значение. Повторите ввод (Да/Нет).\n")

    if len(filtered_transactions) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши")
        print("условия фильтрации\n")
    else:
        print("Программа: Распечатываю итоговый список транзакций...\n")
        print("Программа:")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
        for transaction in filtered_transactions:
            print(f"{widget.get_date(transaction["date"])} {transaction["description"]}")
            print(f"{widget.mask_account_card(transaction["from"])} -> {widget.mask_account_card(transaction["to"])}")
            amount = (
                transaction["operationAmount"]["amount"] if "operationAmount" in transaction else transaction["amount"]
            )
            currency_name = (
                transaction["operationAmount"]["currency"]["name"]
                if "operationAmount" in transaction
                else transaction["currency_name"]
            )
            print(f"Сумма: {str(round(float(amount), 2))} {currency_name}\n")


main_menu()
