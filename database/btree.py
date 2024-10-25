import timeit
from BTrees.IIBTree import IITreeSet

"""
리스트 생성 시작
리스트 생성 소요 시간: 11.353506 sec
트리 생성 시작
트리 생성 소요 시간: 133.497069 sec
리스트 조회 시작
리스트 조회 소요 시간: 0.000638 sec
트리 조회 시작
트리 조회 소요 시간: 0.000007 sec
"""

TABLE_SIZE = 320_000_000

print("리스트 생성 시작")
start_time_list = timeit.default_timer()
data_list = list(range(1, TABLE_SIZE))
end_time_list = timeit.default_timer()
time_setup_list = end_time_list - start_time_list
print(f"리스트 생성 소요 시간: {time_setup_list:.6f} sec")

print("트리 생성 시작")
start_time_tree = timeit.default_timer()
data_tree = IITreeSet(range(1, TABLE_SIZE))
end_time_tree = timeit.default_timer()
time_setup_tree = end_time_tree - start_time_tree
print(f"트리 생성 소요 시간: {time_setup_tree:.6f} sec")


def fetch_from_list(target):
    for data in data_list:
        if data == target:
            return data


def fetch_from_list(target):
    return data_tree.has_key(target)


target = 160_000

print("리스트 조회 시작")
start_time_list = timeit.default_timer()
fetch_from_list(target)
end_time_list = timeit.default_timer()
time_setup_list = end_time_list - start_time_list
print(f"리스트 조회 소요 시간: {time_setup_list:.6f} sec")


print("트리 조회 시작")
start_time_tree = timeit.default_timer()
fetch_from_list(target)
end_time_tree = timeit.default_timer()
time_setup_tree = end_time_tree - start_time_tree
print(f"트리 조회 소요 시간: {time_setup_tree:.6f} sec")
