from services.banking_service import *

bankingService = BankingService()
while True:
    select = int(input("1.사용자 추가  2.로그인 3.종료 \n"))
    if select == 1:
        name = input("사용자 이름을 입력해주세요")
        bankingService.addUser(name)
    elif select == 2:
        bankingService.userMenu(input("로그인할 사용자 이름을 적어주세요"))
    elif select == 3:
        break
