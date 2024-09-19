class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        super().__init__(f"잔고가 부족합니다 잔액 : {balance}")


class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__(f"금액이 음수입니다. 양수로 입력해주세요.")


class UserNotFoundError(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(f"{username}을 찾을수 없습니다.")
