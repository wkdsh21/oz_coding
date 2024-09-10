# for i in iterable:
# reversed(sequence)
# while 문 강점 종료조건이 명확할떄, 무수히 많이 실행해야 할때
# while else 문 while문 안에서 break가 걸리면 else 문은 무시한다 유용하게사용
# continue, break

num = int(input())
count = 0
while num != 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    count += 1
print(count)
