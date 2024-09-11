# 함수 def name(parameter):
# 파라미터에 *을붙이면 가변 파라미터 (*parameter) 개수를 따로 정하지않아도 입력된 파라미터 갯수만큼 튜플로 저장함
# 가변파라미터 규칙 2개 1.가변 매개변수 뒤에는 일반 매개변수가 올수없다. 2.가변 매개변수는 하나만 사용가능
# 기본매개변수(default값) def name(value, n=2) n이 기본매개변수이다. 규칙 1개 1.기본매개변수뒤에는 일반매개변수가 올수없다.
# 여기서 문제점은 가변매개변수와 기본매개변수를 같이 쓰면 기본매개변수의 의미가 사라진다는것이다
# (기본매개변수가 기본값을가져야할지 인자를 넣어야할지 알수없기때문)
# 가변매개변수와 기본매개변수를 같이 쓰면 둘중 앞에있는 변수를 무조건 채운다
# 쉽게말해서 기본이 앞에있는경우는 기본을쓰는이유가 사라져서 안쓰고, 기본이 뒤에있으면 가변이 인자를 다가져가기때문에 이를 커버할
# 키워드 매개변수라는 개념이 나오게됨
# print(i,end="") 여기서 end="" 이것이 키워드 매개변수 개념이다
# 재귀함수 종료조건과 리턴할 값이 명확하면 사용 메모이제이션,꼬리재귀

print(type("asdqwfews fsd".split(" ")))
