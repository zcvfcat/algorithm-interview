# threshold 2 f = x * 2 + 1     space s = threshold - x - 1
# 0  *        f(0) = 1          s(0) = 1
# 1 ***       f(1) = 3          s(1) = 0


threshold = 5


def f(x):
    return x * 2 + 1


def s(x):
    return threshold - x - 1


for x in range(threshold):

    for i in range(s(x)):
        print(" ", end="")

    for i in range(f(x)):
        print("*", end="")

    print()
