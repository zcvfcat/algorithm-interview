def solution(genres, plays):
    answer = []
    z = sorted(list(zip(genres, plays, list(range(len(genres))))),
               key=lambda x: (x[0], -x[1]))
    a = []
    temp = [0]
    for i in range(len(z)):
        temp[0] += z[i][1]
        temp.append(z[i][2])
        if i == len(z)-1 or z[i][0] != z[i+1][0]:
            a.append(temp)
            temp = [0]
    a = sorted(a, key=lambda x: -x[0])
    for i in range(len(a)):
        answer.append(a[i][1])
        if len(a[i]) > 2:
            answer.append(a[i][2])
    return answer


def test1():
    assert solution(["classic", "pop", "classic", "classic", "pop"], [
                    500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
