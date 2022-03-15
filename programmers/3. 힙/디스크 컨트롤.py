# https://programmers.co.kr/learn/courses/30/lessons/42627
# https://dev-note-97.tistory.com/150

import heapq

from py import process


def solution(jobs):
    answer = 0
    time = 0
    length = len(jobs)

    jobs.sort()

    heap = []

    while len(jobs) != 0 or len(heap) != 0:
        while len(jobs) != 0 and jobs[0][0] <= time:
            heapq.heappush(heap, jobs.pop(0)[::-1])

        if len(heap) == 0:
            time = jobs[0][0]
            continue

        process = heapq.heappop(heap)
        time += process[0]
        answer += time - process[1]

    return answer // length


def test1():
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9
