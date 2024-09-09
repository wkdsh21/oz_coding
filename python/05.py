# 다른 시퀀스와 달리 dict는 연관성이 존재한다
# a = {1:"1",2:"2"} or a = dict(1="1",2="2") 기호 조심
# zip(리스트,리스트) 두개의 리스트를 같은인덱스끼리 묶어줌/
print(dict(zip([1, 2, 3], [4, 5, 6])))  =>   {1: 4, 2: 5, 3: 6}
# "key" in dict  =>  key가 있는지 확인가능
# dict.values() , dict.keys() , dict.items() 튜플의 리스트 list()로 감싸서 리스트화 시켜서 인덱싱가능
# del dict[key] 삭제
# dict[newkey]="value" 추가 or 변경
# dict.update({"key1":1,"key2":2}) 딕셔너리를 한번에 추가가능 이중리스트 튜플리스트도 인자로 전달가능
