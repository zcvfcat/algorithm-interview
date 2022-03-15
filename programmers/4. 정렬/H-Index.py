# https://programmers.co.kr/learn/courses/30/lessons/42747
# https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-H-Index

def solution(citations):
    # 문제의 핵심은 Index를 Return 하는 것이다.
    # 인용된 논문이 논문 수(sort한 citations의 Index값)와 같거나 논문 수보다 작아지기 시작하는 숫자가 바로 H-Index이다.
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    # 같거나 작아지지 않는다면 citations의 길이(=인덱스 마지막) 리턴
    return len(citations)


def test1():
    assert solution([3, 0, 6, 1, 5],) == 3
