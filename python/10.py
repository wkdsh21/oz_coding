# 예외코드 작성
try:
    x = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError 예외 발생.")
except IndexError:
    print("IndexError 예외 발생")
else:  # try문이 예외,에러없이 정상 실행시
    print("성공")
finally:  # 에러가 발생해도 무조건 실행
    print("코드실행 종료")

# 예외 객체 찾아보기 ZeroDivisionError, IndexError
