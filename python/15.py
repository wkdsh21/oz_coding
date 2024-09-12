# 제너레이터(함수)
def gen():
    print()
    yield 1
    print()
    yield 2
    print()
    yield 3


# next(gen) 를 사용해 다음 yield 가있는곳까지 함수가 실행됨(부분실행)
# 메모리 효율성
# 리스트 컴프리헨션은 실행시 메모리에 모두다 올림 제너레이터는 실행되는 부분만 메모리에 올림
