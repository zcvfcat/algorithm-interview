# https: // programmers.co.kr/learn/courses/30/lessons/42746?language = python3
# https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98

def solution(numbers):
    # 0. key point
    numbers_str = [str(num) for num in numbers]  # 1. 사전 값으로 정렬하기
    # 2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))
    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.


def test1():
    assert solution([6, 10, 2]) == "6210"


def test2():
    assert solution([3, 30, 34, 5, 9]) == "9534330"
