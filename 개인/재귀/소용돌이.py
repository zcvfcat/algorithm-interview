h = 4
w = 5

visited = [[False] * w for _ in range(h)]

vetors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cnt = 0


def isValidate(y, x):
    return 0 <= y < h and 0 <= x < w


def recur(y, x, v):
    global cnt
    if cnt == h * w:
        return

    visited[y][x] = cnt

    cnt += 1

    if v == (0, 1):
        if isValidate(y, x + 1) and visited[y][x + 1] is False:
            return recur(y, x + 1, (0, 1))
        else:
            return recur(y + 1, x, (1, 0))

    elif v == (1, 0):
        if isValidate(y + 1, x) and visited[y + 1][x] is False:
            return recur(y + 1, x, (1, 0))
        else:
            return recur(y, x - 1, (0, -1))

    elif v == (0, -1):
        if isValidate(y, x - 1) and visited[y][x - 1] is False:
            return recur(y, x - 1, (0, -1))
        else:
            return recur(y - 1, x, (-1, 0))

    elif v == (-1, 0):
        if isValidate(y - 1, x) and visited[y - 1][x] is False:
            return recur(y - 1, x, (-1, 0))
        else:
            return recur(y, x + 1, (0, 1))


recur(0, 0, (0, 1))
for e in visited:
    print(e)
