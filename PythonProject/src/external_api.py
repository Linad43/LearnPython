import json
import os
import time

import requests
import yfinance as yf
from dotenv import load_dotenv

from src.models import Transaction

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key_rates = os.getenv("API_KEY_RATES")


def convert_to_rub(transaction: Transaction) -> float:
    """Конвертация валют в рубли использует классы"""
    if transaction.operationAmount.currency.code != "RUB":
        amount = float(transaction.operationAmount.amount)
        url = "https://api.apilayer.com/exchangerates_data/latest"
        assert api_key_rates is not None
        headers = {"apikey": api_key_rates}

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


# def get_currency_rates(path, base="USD"):
#     with open(path, "r", encoding="utf-8") as f:
#         data = json.load(f)
#
#     currencies = data.get("user_currencies", [])
#
#     url = "https://api.frankfurter.app/latest"
#
#     params = {
#         "from": base,
#         "to": ",".join(currencies)
#     }
#
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#
#     rates = response.json().get("rates", {})
#
#     return [
#         {"currency": cur, "rate": rates.get(cur)}
#         for cur in currencies
#         if cur in rates
#     ]


def get_currency_rates(path, base="RUB"):
    """Получает курсы валют"""

    url = "https://api.apilayer.com/exchangerates_data/latest"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    currencies = data.get("user_currencies", [])

    headers = {
        "apikey": api_key_rates,
    }

    params = {"base": base, "symbols": ",".join(currencies)}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        rates_data = response.json().get("rates", {})

        currency_rates = [{"currency": cur, "rate": rates_data.get(cur)} for cur in currencies if cur in rates_data]

        return currency_rates
    except Exception:
        return []


def get_stock_prices(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    stocks = data.get("user_stocks", [])

    result = []
    try:
        for symbol in stocks:
            ticker = yf.Ticker(symbol)

            # текущая цена
            price = ticker.fast_info.get("last_price")

            # fallback
            if price is None:
                price = ticker.info.get("regularMarketPrice")

            result.append({"stock": symbol, "price": float(price) if price else None})
    except Exception:
        pass
    return result


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
        assert api_key_rates is not None
        headers = {"apikey": api_key_rates}
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
