import os
import time

import requests
from dotenv import load_dotenv

from src.models import Transaction

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv("API_KEY")


def convert_to_rub(transaction: Transaction) -> float:
    """Конвертация валют в рубли использует классы"""
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
    else:
        return float(transaction.operationAmount.amount)


def convert_to_rub_dict(transaction: dict) -> float:
    """Конвертация валют в рубли использует словари"""
    currency_code = (
        transaction["operationAmount"]["currency"]["code"]
        if "operationAmount" in transaction
        else transaction["currency_code"]
    )

    amount = (
        float(transaction["operationAmount"]["amount"])
        if "operationAmount" in transaction
        else float(transaction["amount"])
    )

    if currency_code != "RUB":

        url = "https://api.apilayer.com/exchangerates_data/latest"
        assert api_key is not None
        headers = {"apikey": api_key}
        params = {"base": currency_code, "symbols": "RUB"}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            data = response.json()
            return amount * data["rates"]["RUB"]
        except Exception as e:
            print(f"{time.time()} API error:", e)
            return 0.0
    else:
        return float(amount)
