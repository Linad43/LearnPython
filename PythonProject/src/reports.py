import json
import re
from datetime import datetime, timedelta
from functools import wraps


def decorator_to_file(filename):
    def inner(func):
        @wraps(func)
        def report_to_file(*args, **kwargs):
            """Декоратор для сохранения отчетов в файл"""
            write_to_file = func(*args, **kwargs)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(json.dumps(write_to_file, indent=4, ensure_ascii=False))

        return report_to_file

    return inner
    # TODO


def spending_by_category(transactions, category, date=None):
    """Возвращает траты по категории за 3 месяца"""
    pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")
    if date is None:
        date = datetime.today()
    else:
        day, month, year = map(int, pattern.match(date).groups())
        date = date(year, month, day)
    start_date = date - timedelta(days=90)
    result = []
    for transaction in transactions:
        date_transaction = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S").date()
        if (
            transaction["Категория"] == category
            and transaction["Сумма операции"] < 0
            and start_date <= date_transaction <= date
        ):
            result.append(transaction)
    return result
    # TODO


def spending_by_weekday(transactions, date=None):
    """Показывает средние траты по дням недели"""
    pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")
    if date is None:
        date = datetime.today()
    else:
        day, month, year = map(int, pattern.match(date).groups())
        date = date(year, month, day)
    start_date = date - timedelta(days=90)
    result = [0, 0, 0, 0, 0, 0, 0]
    count = [0, 0, 0, 0, 0, 0, 0]
    for transaction in transactions:
        date_transaction = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S").date()
        if transaction["Сумма операции"] < 0 and start_date <= date_transaction <= date:
            result[date_transaction.weekday()] += abs(transaction["Сумма операции"])
            count[date_transaction.weekday()] += 1
    for index in range(len(result)):
        result[index] = round(result[index] / count[index], 2)
    return {
        "Понедельник": result[0],
        "Вторник": result[1],
        "Среда": result[2],
        "Четверг": result[3],
        "Пятница": result[4],
        "Суббота": result[5],
        "Воскресенье": result[6],
    }


def spending_by_workday(transactions, date=None):
    """Показывает средние траты в рабочие дни и выходные"""
    pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")
    if date is None:
        date = datetime.today()
    else:
        day, month, year = map(int, pattern.match(date).groups())
        date = date(year, month, day)
    start_date = date - timedelta(days=90)
    result_week = [0, 0, 0, 0, 0, 0, 0]
    count = [0, 0, 0, 0, 0, 0, 0]
    for transaction in transactions:
        date_transaction = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S").date()
        if transaction["Сумма операции"] < 0 and start_date <= date_transaction <= date:
            result_week[date_transaction.weekday()] += abs(transaction["Сумма операции"])
            count[date_transaction.weekday()] += 1
    weekdays = 0
    weekends = 0
    for index in range(len(result_week)):
        if index < 5:
            weekdays += result_week[index] / count[index]
        else:
            weekends += result_week[index] / count[index]
    return {
        "Будние": weekdays,
        "Выходные": weekends,
    }
