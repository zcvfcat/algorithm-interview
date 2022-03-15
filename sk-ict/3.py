def solution(width, height, diagonals):
    width += 1
    height += 1
    answer = [[0] * width for _ in range(height)]

    for i in range(width):
        answer[0][i] = 1

    for i in range(height):
        answer[i][0] = 1

    for h in range(1, height):
        for w in range(1, width):
            answer[h][w] = (answer[h - 1][w] + answer[h][w - 1]) % 10_000_019

    return (answer[height - 1][width - 1] * len(diagonals)) % 10_000_019


print(solution(2, 2, [[1, 1], [2, 2]]))  # 12
print(solution(51, 37, [[17, 19]]))  # 3225685
