# d = [-1,+1,*2]
#            [5 17]
#     [4 17] [6 17] [10 17]

from collections import deque

N, K = map(int, input().split())

l: int = 10000 * 2 + 1

visited = [False] * l

q = deque([(N, 0)])


def validate(x):
    return 0 <= x <= l and not visited[x]


def bfs():
    while q:
        n, cnt = q.popleft()

        if n == K:
            return cnt

        cnt = cnt + 1

        if validate(n - 1):
            visited[n - 1] = True
            q.append([n - 1, cnt])

        if validate(n + 1):
            visited[n + 1] = True
            q.append([n + 1, cnt])

        if validate(n * 2):
            visited[n * 2] = True
            q.append([n * 2, cnt])


print(bfs())
