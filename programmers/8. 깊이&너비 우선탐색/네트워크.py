def solution(n, computers):
    answer = 0
    visited = [False for n in range(n)]
    queue = [0]
    while True:
        while len(queue) != 0:
            popped = queue.pop(0)
            if not visited[popped]:
                visited[popped] = True
                for i in range(n):
                    if i == popped:
                        continue
                    if computers[popped][i] == 1:
                        queue.append(i)
        if all(visited):
            return answer + 1
        else:
            answer += 1
            queue = [visited.index(False)]


def test1():
    assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2


def test2():
    assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
