import sys
from collections import deque
input = sys.stdin.readline 

def BFS(): 
    while q:
        row,col = q.popleft()
        for i in range(4): # range becomes types of directions
            ncol = col + dx[i]
            nrow = row + dy[i]
            if  0 <= nrow < N and 0 <= ncol < M and not g[nrow][ncol]:
                q.append((nrow,ncol))
                g[nrow][ncol] = g[row][col] + 1             


M, N = map(int, input().strip().split())
g = [list(map(int, input().strip().split())) for i in range(N)]
ans = 0

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
q = deque()

for row in range(N):
    for col in range(M): 
        if g[row][col] == 1:
            q.append([row, col])

BFS()

for row in g:
    for item in row:
        if item == 0:
            print(-1)
            exit()
    ans = max(ans, max(row))

print(ans-1)