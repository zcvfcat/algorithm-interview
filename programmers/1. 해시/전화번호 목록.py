# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True  # 디폴트 True
    phone_book.sort()  # 정렬을 통해 연속된 인덱스만 비교
    for i in range(len(phone_book)-1):  # 반복문을 통해 비교
        if phone_book[i] in phone_book[i+1]:  # 접두어가 되는 번호가 있으면,
            answer = False  # False
    return answer


def test1():
    assert solution(["119", "97674223", "1195524421"]) == False


def test2():
    assert solution(["123", "456", "789"]) == True


def test3():
    assert solution(["12", "123", "1235", "567", "88"]) == False
