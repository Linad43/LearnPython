import os

import requests
from dotenv import load_dotenv

from src.models import Transaction

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv("API_KEY")


def convert_to_rub(transaction: Transaction) -> float:
    """Конвертация валют в рубли"""
    if transaction.operationAmount.currency.code != "RUB":
        amount = float(transaction.operationAmount.amount)
        url = "https://api.apilayer.com/exchangerates_data/latest"
        assert api_key is not None
        headers = {"apikey": api_key}

        params = {"base": transaction.operationAmount.currency.code, "symbols": "RUB"}
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            data = response.json()
            return amount * data["rates"]["RUB"]
        except requests.exceptions.RequestException as e:
            print("API error:", e)
            return 0.0

        # if response.status_code != 200:
        #     raise Exception(f"{response.status_code}: {response.text}")
        #
        # data = response.json()
        # return amount * data["rates"]["RUB"]
    else:
        return float(transaction.operationAmount.amount)
