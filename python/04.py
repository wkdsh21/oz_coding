# list = [1,2,3,4] or []
# range() 연속된 숫자열을 생산
# list(range(0,20,2)) => [0,2,4 ~ 18]
# list(range(20,0,-1)) => [20,19,18 ~ 1]
# list(range(20,0)) => []  20 > 0 이기때문에 빈리스트반환
# input().split() 리스트 언패킹, 리스트 패킹
# a,b,c = iterable  ex)list, range(), map()
# 리스트 메소드 append(x),extend(시퀀스),insert(인덱스,x) ,del list[index], reverse(), sort(), pop(), remove()
# del 과 remove() 의 차이점 del 은 list[index:index] 인덱싱 가능 remove는 값으로 제거
# 시퀀스 자료형 모두 index() , count() , split() 등등 사용가능 슬라이싱 대부분됨
# 튜플 a=1,2 or a=(1,2)           a=(1) 일때는 int로 괄호연산으로 처리
# "구분자".join(문자열 시퀀스) 단,딕셔너리는 key에만 연결된다. 문자열 메소드
# 딕셔너리, 조합은 순서가 없다
# 튜플은 불변이다
# 리스트가 있는데 왜 튜플이 존재할까? => 변경이 안되기 때문에 협업중에 실수로 변경하는일들을 예방할수있고(const 느낌)
# 리스트는 동적배열을 사용하기 때문에 무겁다.(메모리 더블링 4 -> 8,  16 -> 32)

a = [1, 2, 3, 4, 5, 6]
b = [8, 9, 10, 11, 12, 13, 14, 15]

print(a[1:3])
print(a[-1])
print(a[::-1])
print(a.count(33))
print(3 in a)
print(a + b)
a.extend(b)
print(a)
c = list(range(0, 10, 2))
print(c)
c = list(map(lambda x: x * 2, c))
print(c * 3)
print(len(c))
print(c[2])
print(c[len(c) - 1])
