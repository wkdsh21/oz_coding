# set은 중복x 순서x
# a={} 딕셔너리와 비슷 or a=set()
# add() 1개, update() iterable, remove() 에러발생, discard() 에러무시, pop() 제거하고 요소리턴
# 합집합 : a | b , set.union(a,b)  , 교집합 : a & b , set.intersection(a,b) , 차집합 : a - b , set.difference(a,b)
# 가독성문제로 축약 고민해봐야함

# Iterable이 sequence보다 더 큰 범위이다 Iterable은 객체의 원소를 하나씩 반환할수있으면되고.
# sequence는 순서대로나열 즉,인덱싱과 슬라이싱이 되는것을 뜻함 그래서 Iterable 하면서 sequence 하지않은 dict, set 있음

a = {5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1}
for i in range(10):
    print(a.pop())
