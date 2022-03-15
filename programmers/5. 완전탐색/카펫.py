# https://programmers.co.kr/learn/courses/30/lessons/42842
# https://dev-note-97.tistory.com/87

def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    for b in range(1, total+1):
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer


def test1():
    assert solution(10, 2) == [4, 3]


def test2():
    assert solution(8, 1) == [3, 3]


def test3():
    assert solution(24, 24) == [8, 6]
