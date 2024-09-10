# 파일 입출력

# 쓰기
f = open("test.txt", "w", encoding="utf-8")
f.write(" hi")
f.write(
    """띄어쓰기
    엔터
    다됨
"""
)
f.close()

# 추가
f = open("test.txt", "a", encoding="utf-8")
f.write(" 추가")
f.close()

# 읽기
f = open("test.txt", "r", encoding="utf-8")
print(f.read())
f.close()

# 한줄씩 읽기
f = open("test.txt", "r", encoding="utf-8")
print(f.readline())
f.close()

# with 문을 사용하면 마지막에 close를 자동 실행 해준다
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("with문 굿!")

# 리스트 쓰기
list = ["10", "20", "30"]
with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(list)
    f.write(".".join(list))
