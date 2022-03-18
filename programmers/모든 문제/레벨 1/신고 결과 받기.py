# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    count = defaultdict(int)
    user = defaultdict(set)

    for r in report:
        a, b = r.split()
        if b not in user[a]:
            user[a].add(b)
            count[b] += 1

    for id in id_list:
        result = 0

        for u in user[id]:
            if count[u] >= k:
                result += 1

        answer.append(result)

    return answer


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2))

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


def test1():
    assert solution(["muzi", "frodo", "apeach", "neo"], [
                    "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2) == [2, 1, 1, 0]


def test2():
    assert solution(["con", "ryan"], ["ryan con", "ryan con",
                    "ryan con", "ryan con"], 3) == [0, 0]
