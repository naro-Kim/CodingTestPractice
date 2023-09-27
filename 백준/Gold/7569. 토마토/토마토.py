import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().strip().split())
# Create a 3D array (H x N x M)
graph = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]  
dz = [0, 0, 0, 0, 1, -1]
q = deque()

def find_tomato(graph): 
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 1:
                    q.append((h, n, m)) 

def BFS():
    ans = 0
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H  and graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                ans = graph[nz][nx][ny] - 1
    
    return ans

find_tomato(graph)
start = BFS()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                start = -1

print(start)