from pathlib import Path

import pytest
from src.models import Transaction, OperationAmount, Currency

from src import utils


@pytest.fixture
def transactions_test() -> list[Transaction]:
    """Лист для тестов"""
    return [
        Transaction(
            id=441945886,
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            operationAmount=OperationAmount(
                amount="31957.58",
                currency=Currency(
                    name="руб.",
                    code="RUB"
                )
            ),
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589"
        ),
        Transaction(
            id=41428829,
            state="EXECUTED",
            date="2019-07-03T18:35:29.512364",
            operationAmount=OperationAmount(
                amount="8221.37",
                currency=Currency(
                    name="USD",
                    code="USD"
                )
            ),
            description="Перевод организации",
            from_="MasterCard 7158300734726758",
            to="Счет 35383033474447895560"
        ),
        Transaction(
            id=939719570,
            state="EXECUTED",
            date="2018-06-30T02:08:58.425572",
            operationAmount=OperationAmount(
                amount="9824.07",
                currency=Currency(
                    name="USD",
                    code="USD"
                )
            ),
            description="Перевод организации",
            from_="Счет 75106830613657916952",
            to="Счет 11776614605963066702"
        ),
        Transaction(
            id=587085106,
            state='EXECUTED',
            date='2018-03-23T10:45:06.972075',
            operationAmount=OperationAmount(
                amount='48223.05',
                currency=Currency(
                    name='руб.',
                    code='RUB'
                )
            ),
            description='Открытие вклада',
            from_='NONE',
            to='Счет 41421565395219882431'
        ),
        Transaction(
            id=142264268,
            state="EXECUTED",
            date="2019-04-04T23:20:05.206878",
            operationAmount=OperationAmount(
                amount="79114.93",
                currency=Currency(
                    name="USD",
                    code="USD"
                )
            ),
            description="Перевод со счета на счет",
            from_="Счет 19708645243227258542",
            to="Счет 75651667383060284188"
        ),
        Transaction(
            id=873106923,
            state="EXECUTED",
            date="2019-03-23T01:09:46.296404",
            operationAmount=OperationAmount(
                amount="43318.34",
                currency=Currency(
                    name="руб.",
                    code="RUB"
                )
            ),
            description="Перевод со счета на счет",
            from_="Счет 44812258784861134719",
            to="Счет 74489636417521191160"
        ),
    ]


@pytest.fixture
def path_to_json() -> Path:
    path = Path(__file__).resolve().parents[1]
    json_path = path / "data" / "operations.json"
    return json_path


def test_read_json_file(path_to_json: Path, transactions_test: list[Transaction]) -> None:
    transactions: list[Transaction] = utils.read_json(path_to_json)
    for index in range(len(transactions_test)):
        assert transactions[index] == transactions_test[index]
    assert utils.read_json(Path(__file__).resolve().parent) == []
