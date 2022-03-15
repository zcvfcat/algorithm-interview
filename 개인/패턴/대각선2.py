h = 4
w = 5

# q = [(0, n) for n in range(w)]
# for n in range(1, h):
#     q.append((n, w - 1))

q = [(n, 0) for n in range(h)]
for n in range(1, w):
    q.append((h - 1, n))

weight = 0
m = [[False] * w for _ in range(h)]

for y, x in q:
    while y >= 0 and x < w:
        m[y][x] = weight
        y -= 1
        x += 1
        weight += 1

for e in m:
    print(e)
