# https: // www.acmicpc.net/problem/12886

# 오늘 강호는 돌을 이용해 재미있는 게임을 하려고 한다. 먼저, 돌은 세 개의 그룹으로 나누어져 있으며 각각의 그룹에는 돌이 A, B, C개가 있다. 강호는 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.

# 강호는 돌을 단계별로 움직이며, 각 단계는 다음과 같이 이루어져 있다.

# 크기가 같지 않은 두 그룹을 고른다. 그 다음, 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라고 정한다. 그 다음, X에 있는 돌의 개수를 X+X개로, Y에 있는 돌의 개수를 Y-X개로 만든다.

# A, B, C가 주어졌을 때, 강호가 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력하는 프로그램을 작성하시오.


# a = b = c

# x  Y

# x+x y-x


# 10 15 35

# 10 15 = > 20 5 (35)
# 15 35 = > 30 20 (10)
# 10 35 = > 20 25 (15)

# 20 15 25
# 20 30 10
# 20 20 20
# = >
# 20 20 20


#              [10 15 35]               - 0
#    [20 5 35] [10 30 20]   [20 15 25]  - 1

# from collections import deque

# A, B, C = map(int, input().split())
# total = A + B + C

# if total % 3:  # 3으로 나머지 값이 있을경우
#     print(0)

# visited = [[False] * (total+1) for _ in range(total+1)]
# visited[A][B] = True

# q = deque([(A, B, C)])


# def validate(a, b, c):
#     MAX = max(a, b, c)
#     MIN = min(a, b, c)
#     MID = a + b + c - (MAX + MIN)

#     if not visited[MAX][MID]:
#         visited[MAX][MID] = True
#         q.append((a, b, c))
#         return True
#     return False


# def bfs():
#     while q:
#         a, b, c = q.popleft()

#         if a == b == c:
#             return 1

#         a1, b1, c1 = a - b, b + b, c
#         a2, b2, c2 = a - c, b, c + c
#         a3, b3, c3 = a, b - c, c + c

#         if(a1 > 0):
#             validate(a1, b1, c1)
#         if(a2 > 0):
#             validate(a2, b2, c2)
#         if(b3 > 0):
#             validate(a3, b3, c3)

#     return 0


# print(bfs())
