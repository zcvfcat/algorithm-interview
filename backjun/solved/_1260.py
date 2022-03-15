# https://iancoding.tistory.com/326
from collections import deque
from tkinter import E
from typing import List

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

stack: List = []
linkQueue: List = []


def dfs(graph, node, visited: List):
    visited[node] = True
    stack.append(node)
    for edge in graph[node]:
        if not visited[edge]:
            dfs(graph, edge, visited)


def bfs(graph, node, visited: List):
    queue = deque([node])
    visited[node] = True
    linkQueue.append(node)
    while queue:
        node = queue.popleft()
        for edge in graph[node]:
            if not visited[edge]:
                queue.append(edge)
                linkQueue.append(edge)
                visited[edge] = True


visited = [False] * (n + 1)
dfs(graph, v, visited)

visited = [False] * (n + 1)
bfs(graph, v, visited)

print("".join(map(str, stack)))
print()
print("".join(map(str, linkQueue)))
