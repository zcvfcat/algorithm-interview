# half                  f = x * 2 + 1                   space s = half - x
# threshold - half      f = (threshold - x - 1) * 2 + 1 s = x - half
# 0  *                  f(0) = 1                        s(0) = 2
# 1 ***                 f(1) = 3                        s(1) = 1
# 2*****                f(2) = 5                        s(2) = 0
# 3 ***                 f(3) = 3                        s(3) = 1
# 4  *                  f(4) = 1                        s(4) = 2

threshold = 5
half = threshold // 2

print(half)


def f(x, threshold, half):
    if x < half:
        return x * 2 + 1
    else:
        return (threshold - x - 1) * 2 + 1


def s(x, threshold, half):
    if x < half:
        return half - x
    else:
        return x - half


for x in range(threshold):

    for i in range(s(x, threshold, half)):
        print(" ", end="")

    for i in range(f(x, threshold, half)):
        print("*", end="")

    print()
