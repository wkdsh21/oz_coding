# 함수의 매개변수로 사용되는 함수를 "콜백함수" 라고함 ex) map(), filter() 제너레이터를 반환한다.
# 람다 == 익명함수
# filter(lambda x : x < 5 , list)
# 람다는 가독성,편리함,간단함 map,filter 같은곳에 콜백 함수로써 선언과 동시에 사용가능
from typing import Callable, Iterable, Any

a = list(range(1, 11))
a = filter(lambda x: x % 2 == 0, a)
print(list(a))


def my_filter(func: Callable[[Any], bool], iterable: Iterable) -> list:
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result


my_filter(lambda x: x % 2 == 0, list(range(1, 11)))
