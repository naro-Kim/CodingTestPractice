import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M, V = map(int, input().split())
g = {}  # empty graph

# cheking nodes
for i in range(1, N+1):
    g[i] = []

# graph dictionary implementation
for i in range(M):
    x, y = map(int, input().strip().split())  # 연결된 노드는 서로를 idx로 추가해줘야 한다.
    g[x].append(y)
    g[y].append(x)

for key in g:
    g[key] = sorted(g[key])

# DFS implementation with adjacency list
def DFS(graph, root, visited = None):
    if not graph:
        return
    if visited is None:
        visited = []
    visited.append(root)
    for next_node in graph[root]:
        if next_node not in visited:
            DFS(graph, next_node, visited) 

    return visited

# BFS implementation with adjacency list
def BFS(graph, root):
    if not graph:
        return
    visited = []
    queue = deque([root])
    visited.append(root)

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print(*DFS(g, V))
print(*BFS(g, V))
