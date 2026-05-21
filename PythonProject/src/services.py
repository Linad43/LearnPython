import re

from src import reports, utils


@reports.decorator_to_file("reports_category_cashback.json")
def category_cashback(data, year, month):
    """Какие категории были наиболее выгодными для выбора
    в качестве категорий повышенного кешбека"""
    data_inner = []
    # фильтр
    for item in data:
        year_item = int(item["Дата операции"].split(".")[2][:4])
        month_item = int(item["Дата операции"].split(".")[1])
        amount_item = item["Сумма операции"]
        if year_item == year and month_item == month and amount_item < 0:
            data_inner.append(
                {
                    "category": item["Категория"],
                    "cashback": utils.calculate_cashback(abs(amount_item)),
                }
            )
    # группировка
    grouping = []
    for item in data_inner:
        if item["category"] in grouping:
            grouping[item["category"]] += item["cashback"]
        else:
            grouping.append(
                {
                    "category": item["category"],
                    "cashback": item["cashback"],
                }
            )
    grouping = sorted(grouping, key=lambda k: k["cashback"], reverse=True)
    return grouping


@reports.decorator_to_file("reports_simple_search.json")
def simple_search(data, query):
    """Ищет транзакции по описанию или категории"""
    filtered = []
    pattern = re.compile(query, re.IGNORECASE)
    for item in data:
        if pattern.search(item["Категория"]) or pattern.search(item["Описание"]):
            filtered.append(item)
    return filtered


@reports.decorator_to_file("reports_search_phone_numbers.json")
def search_phone_numbers(data):
    """Находит транзакции с телефонами через regex"""
    pattern = re.compile(r"\+\d \d{3} \d{2}-\d{2}-\d{2}")
    filtered = []
    for item in data:
        if pattern.findall(item["Описание"]):
            filtered.append(item)
    return filtered


@reports.decorator_to_file("reports_search_person_transfers.json")
def search_person_transfers(data):
    """Находит переводы физлицам"""
    pattern = re.compile(r"\w+ \w\.")
    filtered = []
    for item in data:
        if item["Категория"] == "Переводы" and pattern.search(item["Описание"]):
            filtered.append(item)
    return filtered
