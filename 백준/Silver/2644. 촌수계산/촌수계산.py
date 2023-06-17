import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
g = {i: [] for i in range(1, N + 1)}
visited = [0 for _ in range(N+1)]

a, b = map(int, input().strip().split())

M = int(input())
ans = -1

for _ in range(M):
    x, y = map(int, input().strip().split())
    g[x].append(y)
    g[y].append(x)

def BFS(start, end, graph):
    if not graph:
        return -1

    queue = deque([start])
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            return visited[node]
        
        for neighbor in g[node]:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = visited[node] + 1
    return -1

 
print(BFS(a, b, g))