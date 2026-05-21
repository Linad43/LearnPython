from datetime import datetime

from src import external_api, fileops, reports, utils


@reports.decorator_to_file("reports_home_page.json")
def home_page(path_excel, path_settings, date):
    """Создание JSON для страницы <<Главная>>"""
    json_page = {"greeting": utils.get_greeting(date)}
    data = fileops.read_exel(path_excel)
    json_page["cards"] = get_cards_info(data)
    json_page["top_transactions"] = get_top_transactions(data)
    json_page["currency_rates"] = external_api.get_currency_rates(path_settings)
    json_page["stock_prices"] = external_api.get_stock_prices(path_settings)
    return json_page


@reports.decorator_to_file("reports_events_page.json")
def events_page(path_excel, path_settings, date, period="M"):
    """Создание JSON для страницы <<События>>"""
    # start_date = datetime.strptime(date_str, "%d.%m.%Y").date()
    # end_date = datetime.strptime(date_str, "%d.%m.%Y").date()
    start_date = date.date()
    end_date = date.date()
    if period == "W":
        days_to_monday = start_date.weekday()
        start_date = start_date.replace(day=(start_date.day - days_to_monday))
    if period == "M":
        start_date = start_date.replace(day=1)
    if period == "Y":
        start_date = start_date.replace(day=1, month=1)
    if period == "All":
        start_date = None

    json_page = fileops.read_exel(path_excel)
    json_page = utils.filtered_transactions_by_date(json_page, start_date, end_date)
    expenses = group_expenses(json_page)
    income = group_income(json_page)
    currency_rates = external_api.get_currency_rates(path_settings)
    stock_prices = external_api.get_stock_prices(path_settings)
    return {"expenses": expenses, "income": income, "currency_rates": currency_rates, "stock_prices": stock_prices}


def get_cards_info(data: list[dict]) -> list[dict]:
    """Считывает информацию"""
    grouped: dict = {}
    result = []
    expenses = []
    try:
        for element in data:
            if element["Сумма операции"] < 0:
                expenses.append(element)
        for element in expenses:
            card = element["Номер карты"]
            if card in grouped.keys():
                grouped[card]["total_spent"] += abs(element["Сумма операции"])
            else:
                grouped[card] = {
                    "total_spent": abs(float(element["Сумма операции"])),
                }
        for card, info in grouped.items():
            result.append(
                {
                    "last_digits": card[-4:],
                    "total_spent": round(info["total_spent"], 2),
                    "cashback": round(utils.calculate_cashback(info["total_spent"]), 2),
                }
            )

    except KeyError as e:
        print(e)
    return result


def get_top_transactions(transactions, limit=5):
    """Возвращает топ транзакций по сумме"""
    top_transactions = sorted(
        filter(lambda x: x["Сумма операции"] < 0, transactions), key=lambda x: abs(x["Сумма операции"]), reverse=True
    )[:limit]
    top_transactions_clear = []
    for transaction in top_transactions:
        buf = transaction["Дата операции"].split(".")
        date = datetime(year=int(buf[2][:4]), month=int(buf[1]), day=int(buf[0])).strftime("%d.%m.%Y")
        amount = abs(float(transaction["Сумма операции"]))
        category = transaction["Категория"]
        description = transaction["Описание"]
        top_transactions_clear.append(
            {"date": date, "amount": amount, "category": category, "description": description}
        )
    return top_transactions_clear


def group_by_categories(data):
    """Группировка по категориям"""
    grouped = {}
    for element in data:
        category = element["category"]
        amount = abs(float(element["amount"]))
        if category in grouped:
            grouped[category] += amount
        else:
            grouped[category] = amount

    result = []
    for key, value in grouped.items():
        result.append({"category": key, "amount": round(value)})
    result.sort(key=lambda x: x["amount"], reverse=True)
    return result


def group_expenses(data, limit=7):
    """Группировка расходов"""
    expenses = []
    for element in data:
        if element["Сумма операции"] < 0:
            buf_expense = {"category": element["Категория"], "amount": abs(element["Сумма операции"])}
            expenses.append(buf_expense)
    expenses = group_by_categories(expenses)
    main = []
    transfers_and_cash = []
    special_categories = ["Наличные", "Переводы"]
    total_amount = 0
    other_amount = 0
    count = 0
    for element in expenses:
        total_amount += element["amount"]
        # Наличные и переводы
        if element["category"] in special_categories:
            transfers_and_cash.append(element)
        else:
            # Основные категории
            if count < limit:
                main.append(element)
                count += 1
            else:
                other_amount += element["amount"]
    if other_amount > 0:
        main.append({"category": "Остальное", "amount": other_amount})
    return {"total_amount": total_amount, "main": main, "transfers_and_cash": transfers_and_cash}


def group_income(data):
    """Группировка поступлений"""
    income = []
    total_amount = 0
    for element in data:
        if element["Сумма операции"] > 0:
            total_amount += element["Сумма операции"]
            buf_income = {"category": element["Категория"], "amount": element["Сумма операции"]}
            income.append(buf_income)
    income = group_by_categories(income)
    return {"total_amount": total_amount, "main": income}
