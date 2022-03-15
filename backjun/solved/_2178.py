# https://www.acmicpc.net/problem/2178

# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	1	1	1
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# direction  [0, -1] [0 , 1] [1, 0] [-1, 0 ]

#                     [1,1]                0
#                [2,0]    [1, 2]           1

from collections import deque

N, M = map(int, input().split())

positions = [list(map(int, input())) for _ in range(N)]

directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]


def bfs():

    q = deque([(0, 0, 0)])

    while q:
        y, x, cnt = q.popleft()

        cnt = cnt + 1

        if y == N - 1 and x == M - 1:
            return cnt

        for direction in directions:
            dy, dx = direction

            ny = y + dy
            nx = x + dx

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if positions[ny][nx] == 0:
                continue

            if positions[ny][nx] == 1:
                positions[ny][nx] = positions[y][x] + 1
                q.append((ny, nx, cnt))


print(bfs())
