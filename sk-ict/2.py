# 재귀

def solution(n, clockwise):
    answer = [[False] * n for _ in range(n)]
    vectors = ((1, 0), (0, 1), (0, -1), (-1, 0))

    if clockwise:
        vectors = ((0, 1), (-1, 0), (1, 0), (0, -1))

    def isValidate(x, y):
        return 0 <= x < n and 0 <= y < n and answer[y][x] is False

    def toNext(param):
        x, y, vi = param

        for i in range(4):
            vx, vy = vectors[(vi + i) % 4]
            nx, ny = (x + vx, y + vy)

            if isValidate(nx, ny):
                return (nx, ny, vi + i)
        return False

    now = 1

    def recursive(starts, now):

        for x, y, _ in starts:
            answer[y][x] = now

        now += 1
        nextStarts = list(
            filter(lambda a: a is not False, map(toNext, starts)))

        if len(nextStarts):
            return recursive(nextStarts, now)

    recursive([(0, 0, 0), (n - 1, 0, 1), (0, n - 1, 2), (n - 1, n - 1, 3)], now)

    return answer


print(solution(5, True))
print(solution(6, False))
print(solution(9, False))
