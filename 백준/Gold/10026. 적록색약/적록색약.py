import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())  # Corrected to use int() to read the grid size
graph = [list(input().strip()) for _ in range(N)]  # Removed split and added strip
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1] 
ans_rgb = 0
ans_norm = 0

def BFS(x,y,cur):
    q = deque([(x,y)])  

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == cur:
                q.append((nx, ny))
                visited[nx][ny] = True  
 
for i in range(N):
    for j in range(N):
        if not visited[i][j]: 
            BFS(i,j,graph[i][j])
            ans_rgb += 1

# reorganize the graph and visited map
for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j]='G'

visited = [[False for _ in range(N)] for _ in range(N)]

# do BFS again
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j,graph[i][j])
            ans_norm += 1

print(ans_rgb, ans_norm)