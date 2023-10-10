# 안전영역의 정의
# 그래프 영역을 분할해서, 분할한 영역 개수가 최대가 되도록하는 로직을 짜야한다.
# 재귀 형으로 ?
# 높이는 1이상 100이하이다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_value = max(map(max, graph))
min_value = min(map(min, graph))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 0

def bfs(y, x, depth):
  q = deque()
  q.append((y,x)) 
  visited[y][x] = True

  while q:
    y, x = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] > depth and not visited[ny][nx]:
        q.append((ny,nx))
        visited[ny][nx] = True

for depth in range(min_value -1, max_value):
  # i까지의 영역을 방문할 수 없게 만들고 남아있는 영역의 개수를 센다. 
  visited = [[False]*n for _ in range(n)]
  sections = 0
  for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] > depth:
          bfs(i, j, depth)
          sections += 1  
  if sections > ans : 
    ans = sections

print(ans)