import json

from src.models import Transaction

def read_json(path) -> list[Transaction]:
    """Считывание .json файла с данными транзакций"""
    try:
        # Считываем данные если файл найден
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        # Проверяем является ли чситанные данные списком
        #     если нет возвращаем пустой список
        if not isinstance(json_data, list):
            return []

        # Создаем возвращаемый список
        result = []
        for item in json_data:
            # Пропускаем пустые элементы
            if not item:
                continue
            # Если данные корректные, то они добавляются в возвращаемый список
            try:
                result.append(Transaction.from_dict(item))

            # Если данные не корректны, возвращаем пустой список
            except ValueError:
                return []
        return result

    # Если файл не найден, возвращаем пустой список
    except FileNotFoundError:
        return []


