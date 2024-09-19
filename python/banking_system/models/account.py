from utils.decorators import *
from utils.exceptions import *
from models.transaction import *


class Account:
    bankName = "a은행"

    def __init__(self):
        self.__balance = 0
        self.transaction = []

    @validateTransaction
    def deposit(self, amount: int) -> None:
        self.__balance += amount
        self.transaction.append(Transaction("입금", amount, self.__balance))

    @validateTransaction
    def withdraw(self, amount: int) -> None:
        try:
            if amount > self.__balance:
                raise InsufficientFundsError(self.__balance)
        except InsufficientFundsError as e:
            print(e)
        else:
            self.__balance -= amount
            self.transaction.append(Transaction("출금", amount, self.__balance))

    def getBalance(self) -> int:
        return self.__balance

    def getTransaction(self) -> list:
        return self.transaction

    @classmethod
    def getBankName(cls) -> str:
        return cls.bankName

    @classmethod
    def setBankName(cls, name: str) -> None:
        cls.bankName = name
