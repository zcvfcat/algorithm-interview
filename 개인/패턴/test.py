width = 4
height = 3

arr = [[-1] * width for _ in range(height)]

cnt = 0
for i in range(width + height - 1):
    if i < width:
        x, y = (i, 0)
    else:
        x, y = (width - 1, i - (width - 1))

    # x, y = (min(i, width - 1), max(0, i - (width - 1)))

    offset = 0
    while 0 <= x - offset < width and 0 <= y + offset < height:
        arr[y + offset][x - offset] = cnt
        cnt += 1
        offset += 1

for e in arr:
    print(e)

inp = 3

for i in range(inp):
    for j in range(inp - (i + 1)):
        print(' ', end='')
    for j in range((i + 1) * 2 - 1):
        print('*', end='')
    print()
