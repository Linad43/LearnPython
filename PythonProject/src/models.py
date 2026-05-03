from dataclasses import dataclass
from typing import Any


@dataclass
class Currency:
    name: str
    code: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Currency":
        if not isinstance(data, dict):
            raise ValueError("Currency must be dict")

        return Currency(
            name=data["name"],
            code=data["code"],
        )


@dataclass
class OperationAmount:
    amount: str
    currency: Currency

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "OperationAmount":
        if not isinstance(data, dict):
            raise ValueError("OperationAmount must be dict")

        return OperationAmount(
            amount=data["amount"],
            currency=Currency.from_dict(data.get("currency", {})),
        )


@dataclass
class Transaction:
    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: str
    from_: str
    to: str

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Transaction":
        if not isinstance(data, dict):
            raise ValueError("Transaction must be dict")

        return Transaction(
            id=data["id"],
            state=data["state"],
            date=data["date"],
            operationAmount=OperationAmount.from_dict(data.get("operationAmount", {})),
            description=data["description"],
            from_=data.get("from", "NONE"),
            to=data.get("to", "NONE"),
        )

    # @staticmethod
    # def from_csv(data: dict[str, Any]) -> "Transaction":
    #     if not isinstance(data, dict):
    #         raise ValueError("Transaction must be dict")
    #
    #     return Transaction(
    #         id=int(data["id"]),
    #         state=data["state"],
    #         date=data["date"],
    #         operationAmount=OperationAmount(
    #             amount=data["amount"],
    #             currency=Currency(
    #                 name=data["currency_name"],
    #                 code=data["currency_code"],
    #             ),
    #         ),
    #         description=data["description"],
    #         from_=data.get("from", "NONE") if data.get("from") != "" else "NONE",
    #         to=data.get("to", "NONE"),
    #     )
    #
    # @staticmethod
    # def from_excel(data: dict[str, Any]) -> "Transaction":
    #     if not isinstance(data, dict):
    #         raise ValueError("Transaction must be dict")
    #
    #     return Transaction(
    #         id=int(data["id"]),
    #         state=data["state"],
    #         date=data["date"],
    #         operationAmount=OperationAmount(
    #             amount=str(round(data["amount"])),
    #             currency=Currency(
    #                 name=data["currency_name"],
    #                 code=data["currency_code"],
    #             ),
    #         ),
    #         description=data["description"],
    #         from_=data.get("from", "NONE") if pd.notna(data.get("from")) else "NONE",
    #         to=data.get("to", "NONE"),
    #     )
