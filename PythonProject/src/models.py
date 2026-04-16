from typing import TypedDict


class Currency:
    name: str
    code: str


class OperationAmount:
    amount: str
    currency: Currency


Transaction = TypedDict(
    "Transaction",
    {
        "id": int,
        "state": str,
        "date": str,
        "operationAmount": OperationAmount,
        "description": str,
        "from": str,
        "to": str,
    },
)
