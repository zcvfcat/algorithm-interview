
1. 시작점 찾기
0 1 3
2 4 6
5 7 8

0 2 5
1 4 7
3 6 8

0 2 5
1 4 6
3 7 8


2. 입력
for w+h-1

while 0 <= x - offset < width and 0 <= y + offset < height:


width = 4
height = 5

q = [(n, 0) for n in range(height)]
q.append([height - 1, n] for n in range(width))
