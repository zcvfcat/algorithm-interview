# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []

    return answer


def test1():
    assert solution(["muzi", "frodo", "apeach", "neo"], [
                    "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2) == [2, 1, 1, 0]


def test2():
    assert solution(["con", "ryan"], ["ryan con", "ryan con",
                    "ryan con", "ryan con"], 3) == [0, 0]
