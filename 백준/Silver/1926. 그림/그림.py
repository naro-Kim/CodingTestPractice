import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(N)]
answer = []

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# BFS implementation with adjacency list
def BFS(x, y):
    q = deque()
    q.append([x,y])
    g[x][y] = 0 # visit graph at start
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4): # range becomes types of directions
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 1:
                g[nx][ny] = -1 # visited graph node
                q.append((nx, ny))
                cnt += 1
    return cnt

# graph dictionary implementation
for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            answer.append(BFS(i, j))

if len(answer) == 0:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))