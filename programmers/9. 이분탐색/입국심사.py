# https: // programmers.co.kr/learn/courses/30/lessons/43238


def solution(n, times):
    answer = max(times) * n
    left = 1
    right = answer

    while left < right:
        mid = (left + right) // 2
        capability = 0
        for t in times:
            capability += mid // t
        if capability >= n:
            right = mid
            if mid < answer:
                answer = mid
        else:
            left = mid + 1
    return answer


def test1():
    assert solution(6, [7, 10]) == 28
