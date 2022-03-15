# https://programmers.co.kr/learn/courses/30/lessons/49191
# https://dev-note-97.tistory.com/154

def solution(n, results):
    answer = 0
    win = {i: set() for i in range(1, n+1)}
    lose = {i: set() for i in range(1, n+1)}

    for r in results:                     # 1단계
        win[r[0]].add(r[1])
        lose[r[1]].add(r[0])

    for key in win.keys():                # 2단계
        queue = win[key].copy()
        while len(queue) != 0:
            next_key = queue.pop()
            win[key] |= win[next_key]
            queue |= win[next_key]

    for key in lose.keys():
        queue = lose[key].copy()
        while len(queue) != 0:
            next_key = queue.pop()
            lose[key] |= lose[next_key]
            queue |= lose[next_key]

    for i in range(1, n+1):                # 3단계
        if len(win[i] | lose[i]) == n-1:
            answer += 1

    return answer


def test1():
    assert solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2
