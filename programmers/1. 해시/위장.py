import collections
from functools import reduce


def solution(clothes):
    answer = 1

    clothes = dict(clothes)  # clothes dictionary화
    val = list(clothes.values())  # 옷 종류만 꺼내오고
    counter = collections.Counter(val)  # 옷 종류별 갯수 계산

    print('clothes')
    print(clothes)
    print('val')
    print(val)
    print('counter')
    print(counter)

    answer = reduce(lambda x, y: x*(y+1), counter.values(), 1) - 1

    return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], [
    "green_turban", "headgear"]])


def test1():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], [
                    "green_turban", "headgear"]]) == 5


def test2():
    assert solution([["crowmask", "face"], ["bluesunglasses",
                    "face"], ["smoky_makeup", "face"]]) == 3
