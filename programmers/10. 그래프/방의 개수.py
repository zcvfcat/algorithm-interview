# https://programmers.co.kr/learn/courses/30/lessons/49190
# https://velog.io/@narastro/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EC%9D%98-%EA%B0%9C%EC%88%98-Python

from collections import defaultdict


def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x, y = 0, 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    for arrow in arrows:
        for _ in range(2):              # 대각선 판별을 위해 2씩
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            elif (nx, ny) not in visit:                  # 방문하지 않았던 경우
                # 경로가 겹치는 경우는 따로 해줄 필요 없음
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            x, y = nx, ny        # 이동
    return answer


def test1():
    assert solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0,
                    0, 0, 1, 6, 5, 5, 3, 6, 0]) == 3
