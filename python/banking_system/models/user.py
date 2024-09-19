from models.account import *


class User:
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account()
