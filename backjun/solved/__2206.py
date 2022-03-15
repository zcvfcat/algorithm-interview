# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# @ 부순 표식
#                           [0,0]
#                   @[0,1]       @[1,0]
#             [0,2]
#       [0,3]
#  [0,4]
# 부순 시점부터 점화식 다시

# 1. 안뚫려있으면 해당방향, 일회용 망치 사용
# 1 - 2. BFS visited[y][x][망치 사용] = TRUE

# 2. 뚤려 있으면 해당방향, 일회용 망치 미사용
# 2 - 2. BFS visited[y][x][망치 미사용] = TRUE

from collections import deque


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

d = [(0, 1), (-1, 0), (0, -1), (1, 0)]

visited = [[[False] * M for _ in range(N)] for _ in range(2)]


def vaildate(y, x, k):
    return 0 <= y < N and 0 <= x < M and not visited[k][y][x]


def bfs():
    q = deque([(0, 0, 0, 1)])
    while q:
        y, x, c, k = q.popleft()

        if y == N - 1 and x == M - 1:
            return c + 1

        c += 1

        for dy, dx in d:
            ny = dy + y
            nx = dx + x

            if vaildate(ny, nx, k):
                if graph[ny][nx] == 0:
                    q.append((ny, nx, c, k))
                    visited[k][ny][nx] = True

                elif graph[ny][nx] == 1 and k == 1:
                    q.append((ny, nx, c, 0))
                    visited[k][ny][nx] = True

    return -1


print(bfs())
