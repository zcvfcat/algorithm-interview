# bfs

## 완전 탐색 문제

```py
# 1697
#                 5                  -0
#            4    6    10                 -1
#     3  8      7 12     9 11 20         -2
```

```py
# 2178
# direction  [0, -1] [0 , 1] [1, 0] [-1, 0 ]
#                     [1,1]                0
#                [2,0]    [1, 2]           1
```

0. 모든 경우의 수 구하기
1. 다음 상태에서 추적이 가능할 경우 사용
2. 진행시 가장 짧은 방법을 찾음
