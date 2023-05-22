import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().split())
g = {}  # empty graph

# graph dictionary implementation
for i in range(N):
    g[i] = (list(map(int, input().rstrip())))


# BFS implementation with adjacency list
def BFS(x,y):
  # 상하좌우
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4): # range becomes types of directions
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < N and 0 <= ny < M and g[nx][ny] == 1:
                queue.append((nx,ny))
                g[nx][ny] = g[x][y] + 1
    return g[N-1][M-1]

print(BFS(0, 0))