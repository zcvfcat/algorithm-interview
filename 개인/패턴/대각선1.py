1. 시작점을 찾음
2. 들어오는 패턴을 찾음

h = 4
w = 5

q = [(0, n) for n in range(w)]
for n in range(1, h):
    q.append((n, w - 1))

weight = 0
m = [[False] * w for _ in range(h)]

for y, x in q:
    while y < h and 0 <= x:
        m[y][x] = weight
        y += 1
        x -= 1
        weight += 1

for e in m:
    print(e)
