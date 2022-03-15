#              [10 15 35]
# [20 15 25]   [10 30 20]   [20 5 35]
# [A*2 B C-A]  [A B*2 C-B]  [A*2 B-A C]

from collections import deque

# 경우의 수 6가지 - 조건절
#    A < C       A < B       B < C       C < A       B < A        C < B
# [A*2 B C-A] [A*2 B-A C] [A B*2 C-B] [A-C B C*2] [A-B B*2 C] [A B-C C*2]

# A = B = C 같을 경우 종료


def bfs(A, B, total) -> int:
    q = deque([(A, B)])

    while q:
        a, b = q.popleft()
        c = total - (a + b)
        # A = B = C 같을 경우 종료
        if a == b == c:
            return 1

        # if      A < C       A < B       B < C       C < A       B < A       C < B
        # push [A*2 B C-A] [A*2 B-A C] [A B*2 C-B] [A-C B C*2] [A-B B*2 C] [A B-C C*2]

        for i, j in ((a, b), (b, c), (a, c)):
            if i < j:
                j -= i
                i += i
            elif j < i:
                i -= j
                j += j
            else:
                continue

            k = total - (i + j)
            y = max(i, j, k)
            x = min(i, j, k)

            if not visited[y][x]:
                q.append((y, x))
                visited[y][x] = True

    return 0


A, B, C = map(int, input().split())
total = A + B + C

visited = [[False] * (total + 1) for _ in range(total + 1)]

if total % 3 != 0:
    print(0)
else:
    print(bfs(A, B, total))
