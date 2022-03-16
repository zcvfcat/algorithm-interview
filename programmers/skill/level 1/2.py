def solution(a, b):
    answer = 0
    start, end = min(a, b), max(a, b)
    for e in range(start, end + 1):
        answer += e
    return answer


print(solution(3, 5))
