from utils.exceptions import *


def validateTransaction(func: callable) -> callable:
    def wrapper(self, amount):
        try:
            if amount < 0:
                raise NegativeAmountError()
        except NegativeAmountError as e:
            print(e)
        else:
            func(self, amount)

    return wrapper
