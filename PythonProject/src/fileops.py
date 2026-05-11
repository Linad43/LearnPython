import csv
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def read_csv(path: Path, delimiter: str = ",") -> list[dict]:

    logger.debug(f"Start read_csv({path})")
    try:
        with open(path, "r", encoding="utf-8") as file:
            logger.info("File opened successfully")
            data = csv.DictReader(file, delimiter=delimiter)
            result = []
            for row in data:
                if all(value.strip() == "" for value in row.values()):
                    logger.info("Empty element skipped")
                    continue
                result.append(row)
            return result
    except Exception as e:
        logger.error(f"Catch exception: {e}")
        return []


def read_exel(path: Path) -> list[dict]:
    logger.debug(f"Start read_exel({path})")
    try:
        data = pd.read_excel(path)
        data_clean = data.fillna("")
        logger.debug("File opened successfully")
        result = data_clean.to_dict(orient="records")
        return result

    except Exception as e:
        logger.error(f"Catch exception: {e}")
        return []


# def read_csv(path: Path, delimiter: str = ",") -> list[Transaction]:
#     logger.debug(f"Start read_csv({path})")
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             logger.info("File opened successfully")
#             data = csv.DictReader(file, delimiter=delimiter)
#             result = []
#             for row in data:
#                 if not row:
#                     logger.info("Empty row skipped")
#                     continue
#                 else:
#                     try:
#                         result.append(Transaction.from_csv(row))
#                     except ValueError:
#                         logger.error(f"Catch exception ValueError: {row}")
#                         continue
#             return result
#     except Exception as e:
#         logger.error(f"Catch exception: {e}")
#         return []
#
#
# def read_exel(path: Path) -> list[Transaction]:
#     logger.debug(f"Start read_exel({path})")
#     try:
#         data = pd.read_excel(path)
#         logger.debug("File opened successfully")
#         result = []
#         for index, row in data.iterrows():
#             if row.isna().all():
#                 logger.info(f"Empty row {index} skipped")
#                 continue
#             else:
#                 try:
#                     result.append(Transaction.from_excel(row.to_dict()))
#                 except ValueError:
#                     logger.error(f"Catch exception ValueError: {row}")
#                     continue
#         return result
#
#     except Exception as e:
#         logger.error(f"Catch exception: {e}")
#         return []
