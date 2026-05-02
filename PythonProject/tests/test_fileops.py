from pathlib import Path

import pytest

from src import fileops
from src.models import Currency, OperationAmount, Transaction


@pytest.fixture
def transactions_test() -> list[Transaction]:
    """Лист для тестов"""
    return [
        Transaction(
            id=650703,
            state="EXECUTED",
            date="2023-09-05T11:30:32Z",
            operationAmount=OperationAmount(amount="16210", currency=Currency(name="Sol", code="PEN")),
            description="Перевод организации",
            from_="Счет 58803664561298323391",
            to="Счет 39745660563456619397",
        ),
        Transaction(
            id=3598919,
            state="EXECUTED",
            date="2020-12-06T23:00:58Z",
            operationAmount=OperationAmount(amount="29740", currency=Currency(name="Peso", code="COP")),
            description="Перевод с карты на карту",
            from_="Discover 3172601889670065",
            to="Discover 0720428384694643",
        ),
        Transaction(
            id=593027,
            state="CANCELED",
            date="2023-07-22T05:02:01Z",
            operationAmount=OperationAmount(amount="30368", currency=Currency(name="Shilling", code="TZS")),
            description="Перевод с карты на карту",
            from_="Visa 1959232722494097",
            to="Visa 6804119550473710",
        ),
        Transaction(
            id=366176,
            state="EXECUTED",
            date="2020-08-02T09:35:18Z",
            operationAmount=OperationAmount(amount="29482", currency=Currency(name="Rupiah", code="IDR")),
            description="Перевод с карты на карту",
            from_="Discover 0325955596714937",
            to="Visa 3820488829287420",
        ),
        Transaction(
            id=5380041,
            state="CANCELED",
            date="2021-02-01T11:54:58Z",
            operationAmount=OperationAmount(amount="23789", currency=Currency(name="Peso", code="UYU")),
            description="Открытие вклада",
            from_="NONE",
            to="Счет 23294994494356835683",
        ),
        Transaction(
            id=1962667,
            state="EXECUTED",
            date="2023-10-22T09:43:32Z",
            operationAmount=OperationAmount(amount="18588", currency=Currency(name="Peso", code="COP")),
            description="Перевод организации",
            from_="Mastercard 7286844946221431",
            to="Счет 76145988629288763144",
        ),
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


def test_read_csv_file(path_to_csv: Path, transactions_test: list[Transaction]) -> None:
    transactions: list[Transaction] = fileops.read_csv(path_to_csv, ";")
    for index in range(len(transactions_test)):
        assert transactions[index] == transactions_test[index]
    assert fileops.read_csv(Path(__file__).resolve().parent) == []


def test_read_excel_file(path_to_excel: Path, transactions_test: list[Transaction]) -> None:
    transactions: list[Transaction] = fileops.read_exel(path_to_excel)
    for index in range(len(transactions_test)):
        assert transactions[index] == transactions_test[index]
    assert fileops.read_exel(Path(__file__).resolve().parent) == []
