import json
import logging

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
                result.append(Transaction.from_dict(item))

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
