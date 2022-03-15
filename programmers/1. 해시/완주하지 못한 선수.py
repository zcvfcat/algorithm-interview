def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1 or participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer


def test1():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"


def test2():
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], [
                    "josipa", "filipa", "marina", "nikola"]) == "vinko"


def test3():
    assert solution(["mislav", "stanko", "mislav", "ana"], [
                    "stanko", "ana", "mislav"]) == "mislav"
