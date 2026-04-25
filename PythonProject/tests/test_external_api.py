from unittest.mock import patch, Mock

import pytest

from src import external_api
from src.models import Transaction, OperationAmount, Currency


@pytest.fixture
def data_response():
    return [{
        "success": True,
        "timestamp": 1777025236,
        "base": "USD",
        "date": "2026-04-24",
        "rates": {
            "RUB": 75
        }
    }, {
        "success": True,
        "timestamp": 1777025297,
        "base": "EUR",
        "date": "2026-04-24",
        "rates": {
            "RUB": 88
        }
    }, {
        "success": True,
        "timestamp": 1777025236,
        "base": "USD",
        "date": "2026-04-24",
        "rates": {
            "RUB": 75
        }
    }]


@pytest.fixture
def transactions_test() -> list[Transaction]:
    """Лист для тестов"""
    return [
        Transaction(
            id=41428829,
            state="EXECUTED",
            date="2019-07-03T18:35:29.512364",
            operationAmount=OperationAmount(
                amount="8221",
                currency=Currency(
                    name="USD",
                    code="USD",
                ),
            ),
            description="Перевод организации",
            from_="Maestro 1596837868705199",
            to="Счет 64686473678894779589",
        ),
        Transaction(
            id=441945886,
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            operationAmount=OperationAmount(
                amount="31957",
                currency=Currency(
                    name="EUR",
                    code="EUR",
                ),
            ),
            description="Перевод организации",
            from_="MasterCard 7158300734726758",
            to="Счет 35383033474447895560",
        ),
        Transaction(
            id=587085106,
            state="EXECUTED",
            date="2018-03-23T10:45:06.972075",
            operationAmount=OperationAmount(
                amount="48223",
                currency=Currency(
                    name="руб.",
                    code="RUB",
                ),
            ),
            description="Открытие вклада",
            from_="NONE",
            to="Счет 41421565395219882431",
        )
    ]


@patch("requests.get")
def test_convert_to_rub(mock_request, data_response, transactions_test) -> None:
    for index in range(len(data_response)):
        mock_response = Mock()
        mock_response.json.return_value = data_response[index]
        mock_request.return_value = mock_response
        result_fun = external_api.convert_to_rub(transactions_test[index])
        amount = float(transactions_test[index].operationAmount.amount)
        if transactions_test[index].operationAmount.currency.code == "RUB":
            check_result_fun = amount
        else:
            check_result_fun = data_response[index]["rates"]["RUB"] * amount
        assert result_fun == check_result_fun
