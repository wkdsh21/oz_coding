from models.transaction import *
from models.user import *


class BankingService:
    def __init__(self) -> None:
        self.users = []

    def addUser(self, username: str) -> None:
        self.users.append(User(username))

    def findUser(self, username: str) -> User:
        for i in self.users:
            if i.username == username:
                return i
        raise UserNotFoundError(username)

    def userMenu(self, username: str) -> None:
        try:
            user = self.findUser(username)
        except UserNotFoundError as e:
            print(e)
        else:
            while True:
                select = int(
                    input(
                        "숫자를 입력하세요 1.입금 2.출금 3.잔고확인 4.거래내역 확인 5.종료"
                    )
                )
                if select == 1:
                    user.account.deposit(int(input("입금할 금액을 입력하세요")))
                elif select == 2:
                    user.account.withdraw(int(input("출금할 금액을 입력하세요")))
                elif select == 3:
                    print(f"잔액 : {user.account.getBalance()}")
                elif select == 4:
                    print(list(map(str, user.account.getTransaction())))
                elif select == 5:
                    break
