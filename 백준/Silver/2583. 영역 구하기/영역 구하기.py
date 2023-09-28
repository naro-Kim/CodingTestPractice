import sys
from collections import deque
input = sys.stdin.readline

M,N,K = map(int, input().strip().split())
graph = [[0]*N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = [] 

def BFS(i, j):
    q = deque([(i,j)])
    width = 1
    while q:
        y, x = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx] 
            if 0 <= ny < M and 0 <= nx < N and not graph[ny][nx]:
                q.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1
                width += 1
    return width

for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().strip().split())
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if graph[i][j] == 0:
                graph[i][j] = 1 # number 1 of the graph means that we can visit that node
 
for i in range(M):
    for j in range(N):
        if not graph[i][j]: 
            graph[i][j] = 1
            ans.append(BFS(i,j))

print(len(ans)) 
print(*sorted(ans))