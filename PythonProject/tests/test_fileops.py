from pathlib import Path

import pytest

from src import fileops


@pytest.fixture
def transactions_test_csv() -> list[dict]:
    """Лист для тестов"""
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "366176",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": "29482",
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "amount": "18588",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
        {
            "id": "5294458",
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "amount": "16836",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5429839",
            "state": "EXECUTED",
            "date": "2023-06-23T19:46:34Z",
            "amount": "25261",
            "currency_name": "Hryvnia",
            "currency_code": "UAH",
            "from": "",
            "to": "Счет 76768135089446747029",
            "description": "Открытие вклада",
        },
        {
            "id": "3226899",
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "amount": "21680",
            "currency_name": "Koruna",
            "currency_code": "CZK",
            "from": "",
            "to": "Счет 88329674734590848775",
            "description": "Открытие вклада",
        },
        {
            "id": "3176764",
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "amount": "16652",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def transactions_test_excel() -> list[dict]:
    """Лист для тестов"""
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 366176.0,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482.0,
            "currency_name": "Rupiah",
            "currency_code": "IDR",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5380041.0,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789.0,
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
        {
            "id": 1962667.0,
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "amount": 18588.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
            "description": "Перевод организации",
        },
        {
            "id": 5294458.0,
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "amount": 16836.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5429839.0,
            "state": "EXECUTED",
            "date": "2023-06-23T19:46:34Z",
            "amount": 25261.0,
            "currency_name": "Hryvnia",
            "currency_code": "UAH",
            "from": "",
            "to": "Счет 76768135089446747029",
            "description": "Открытие вклада",
        },
        {
            "id": 3226899.0,
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "amount": 21680.0,
            "currency_name": "Koruna",
            "currency_code": "CZK",
            "from": "",
            "to": "Счет 88329674734590848775",
            "description": "Открытие вклада",
        },
        {
            "id": 3176764.0,
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "amount": 16652.0,
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def path_to_csv() -> Path:
    path = Path(__file__).resolve().parents[1]
    csv_path = path / "data" / "transactions.csv"
    return csv_path


@pytest.fixture
def path_to_excel() -> Path:
    path = Path(__file__).resolve().parents[1]
    excel_path = path / "data" / "transactions_excel.xlsx"
    return excel_path


def test_read_csv_file(path_to_csv: Path, transactions_test_csv: list[dict]) -> None:
    transactions: list[dict] = fileops.read_csv(path_to_csv, ";")
    for index in range(len(transactions_test_csv)):
        assert transactions[index] == transactions_test_csv[index]
    assert fileops.read_csv(Path(__file__).resolve().parent) == []


def test_read_excel_file(path_to_excel: Path, transactions_test_excel: list[dict]) -> None:
    transactions: list[dict] = fileops.read_exel(path_to_excel)
    for index in range(len(transactions_test_excel)):
        assert transactions[index] == transactions_test_excel[index]
    assert fileops.read_exel(Path(__file__).resolve().parent) == []
