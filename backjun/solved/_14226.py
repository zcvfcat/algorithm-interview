# https://www.acmicpc.net/problem/14226
# 5 17


# 영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# d [0,1] [1,0] [-1, 0]

#          [화면, 클립보드]
#           [1, 0]           0

#     [1, 1]  //[1,0]  [1, 0] -1

#  [1, 2] [2, 1] [0, 1]


from collections import deque

S = int(input())

# d = [[0, 1], [1, 0], [-1, 0]]
# vector = ((0,1),(0,-1),(1,0),(-1,0))

visited = [[False] * 1001 for _ in range(1001)]

q = deque([(1, 0, 0)])


def validate(m, c):
    return 0 <= m < 1001 and not visited[m][c]


def bfs():
    while q:
        m, c, cnt = q.popleft()

        if m == S:
            return cnt

        cnt = cnt + 1

        # 복사
        if validate(m, m):
            q.append((m, m, cnt))
            visited[m][m] = True

        # 붙
        if validate(m + c, c):
            q.append((m + c, c, cnt))
            visited[m + c][c] = True

        # 빼
        if validate(m - 1, c):
            q.append((m - 1, c, cnt))
            visited[m - 1][c] = True


print(bfs())
