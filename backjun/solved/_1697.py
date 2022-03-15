# https://www.acmicpc.net/problem/1697
# 5 17

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 5 10 9 18 17
#                 5                  -0

#             4 6 10                 -1

#     3  8    7 12   9 11 20         -2

# 2  6  7 9 16        18             -3

#                    17              -4

# 1. 지금의상태로 다음의상태를 감
# 2. 진행방식이 가장 짧은 방법을 찾음

from collections import deque

n, k = map(int, input().split())

visited = [False] * 200001
visited[n] = True


def validate(x):
    return 0 <= x <= 200001 and not visited[x]


def bfs():
    q = deque([(n, 0)])

    while q:
        num, cnt = q.popleft()

        if num == k:
            return cnt  # bfs 니까

        cnt = cnt + 1

        if validate(num - 1):
            q.append([num - 1, cnt])
            visited[num - 1] = True

        if validate(num + 1):
            q.append([num + 1, cnt])
            visited[num + 1] = True

        if validate(num * 2):
            q.append([num * 2, cnt])
            visited[num * 2] = True


print(bfs())
