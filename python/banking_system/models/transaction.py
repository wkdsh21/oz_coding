class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        return f"[거래유형]:{self.transaction_type} [거래 금액]:{self.amount} [거래 후 잔금]:{self.balance}"

    def to_tuple(self) -> tuple:
        return (self.transaction_type, self.amount, self.balance)
