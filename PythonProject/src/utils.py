import json
import logging
from datetime import datetime

from src.models import Transaction

logger = logging.getLogger(__name__)


def read_json(path) -> list[Transaction]:
    logger.debug(f"Start read_json(path:'{path}')")
    """Считывание *.json файла с данными транзакций"""
    try:
        # Считываем данные если файл найден
        logger.debug(f"Reading {path}")
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        logger.debug("Reading success")
        logger.info(f"len(json_data): {len(json_data)}")

        # Проверяем является ли считанные данные списком
        #     если нет возвращаем пустой список
        if not isinstance(json_data, list):
            logger.warning("json_data is not a list")
            return []

        # Создаем возвращаемый список
        logger.debug("Create result")
        result = []
        for item in json_data:
            # Пропускаем пустые элементы
            if not item:
                logger.warning("Element json_data is empty")
                continue
            # Если данные корректные, то они добавляются в возвращаемый список
            try:
                result.append(Transaction.from_json(item))

            # Если данные не корректны, возвращаем пустой список
            except Exception:
                logger.error("Element json_data is invalid")
                return []
        logger.info(f"len(result): {len(result)}")
        return result

    # Если файл не найден, возвращаем пустой список
    except Exception:
        logger.error(f"Reading {path} failed")
        return []


def read_json_dict(path) -> list[dict]:
    logger.debug(f"Start read_json(path:'{path}')")
    """Считывание *.json файла с данными транзакций функция возвращает лист словарей"""
    try:
        # Считываем данные если файл найден
        logger.debug(f"Reading {path}")
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        logger.debug("Reading success")
        logger.info(f"len(json_data): {len(json_data)}")

        # Проверяем является ли считанные данные списком
        #     если нет возвращаем пустой список
        if not isinstance(json_data, list):
            logger.warning("json_data is not a list")
            return []

        # Создаем возвращаемый список
        logger.debug("Create result")
        result = []
        for item in json_data:
            # Пропускаем пустые элементы
            if not item:
                logger.warning("Element json_data is empty")
                continue
            # Если данные корректные, то они добавляются в возвращаемый список
            try:
                result.append(item)

            # Если данные не корректны, возвращаем пустой список
            except Exception:
                logger.error("Element json_data is invalid")
                return []
        logger.info(f"len(result): {len(result)}")
        return result

    # Если файл не найден, возвращаем пустой список
    except Exception:
        logger.error(f"Reading {path} failed")
        return []


def filtered_transactions_by_date(data: list[dict], start_date: datetime | None, end_date: datetime) -> list[dict]:
    """ "Фильтрация транзакций, по необходимому диапазону дат"""
    logger.debug(f"Start filtered_transactions_by_date({start_date}, {end_date})")
    result = []
    if start_date is not None:
        for element in data:
            if start_date < str_to_datetime(element["Дата операции"]).date() < end_date:
                result.append(element)
    else:
        for element in data:
            if str_to_datetime(element["Дата платежа"]) < end_date:
                result.append(element)
    return result


def str_to_datetime(date_str: str) -> datetime:
    """Перевод строки даты в datetime"""
    logger.debug(f"Start str_to_datetime({date_str})")
    split_date = date_str.split(".")
    return datetime(year=int(split_date[2][:4]), month=int(split_date[1]), day=int(split_date[0]))


def get_month_start(date) -> datetime:
    """Возвращает первый день месяца"""
    return datetime(date.year, date.month, 1)


def get_greeting(current_time: datetime) -> str:
    """Возвращает приветственное сообщение"""
    if current_time.hour in range(6, 12):
        return "Доброе утро"
    if current_time.hour in range(12, 18):
        return "Добрый день"
    if current_time.hour in range(18, 23):
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def calculate_cashback(amount):
    """Считает кешбек"""
    return round(amount / 100, 2)


def load_user_settings(path) -> list[dict]:
    """Считывание user_settings.json"""
    logger.debug("Start load_user_settings()")
    try:
        logger.debug("Loading user_settings.json")
        with open(path, "r", encoding="utf-8") as f:
            user_settings = json.load(f)
        logger.debug("Loading success")
        logger.info(f"len(user_settings): {len(user_settings)}")
        return user_settings
    except Exception:
        logger.error("Loading user_settings.json failed")
        return []
