# https://programmers.co.kr/learn/courses/30/lessons/42627
# https://dev-note-97.tistory.com/151

def solution(operations):
    heap = []

    for ope in operations:
        command, value = ope.split()[0], int(ope.split()[1])
        if command == 'I':
            heap.append(value)
        elif command == 'D' and len(heap) != 0:
            if value < 0:
                heap.pop(heap.index(min(heap)))
            else:
                heap.pop(heap.index(max(heap)))

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]


def test1():
    assert solution(["I 16", "D 1"]) == [0, 0]


def test2():
    assert solution(["I 7", "I 5", "I -5", "D -1"]) == [7, 5]
