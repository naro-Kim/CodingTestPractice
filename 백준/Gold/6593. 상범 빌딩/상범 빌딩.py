from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(start):
    q = deque([(start[0], start[1], start[2], 0)]) # 4번째는 minutes
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]
    visited[start[0]][start[1]][start[2]] = True
    flag = False
    while q:
        z, y, x, t = q.popleft()
        if graph[z][y][x] == 'E':
            print("Escaped in", t,"minute(s).")
            flag = True
            break
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and not visited[nz][ny][nx]:
                if graph[nz][ny][nx] == '.' or graph[nz][ny][nx] == 'E':
                    q.append((nz, ny, nx, t+1))
                    visited[nz][ny][nx] = True 
    if not flag:
        print("Trapped!")

def make_graph(l, r):
    graph = []    
    for _ in range(l):
        graph.append([list(input().strip()) for _ in range(r)])
        space = input()
    return graph

def find_pos(graph):
    start = (0, 0, 0)

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    start = (i, j, k)
    return start

while True:
    l, r, c = map(int, input().split())
    if not l and not r and not c:
        break
    t = l * r * c
    # 층 별 공백으로 인해 list comprehension을 사용할 수 없음
    # graph = [[list(input().split()) for _ in range(r)] for _ in range(l)]

    graph = make_graph(l, r)
    start = find_pos(graph)
    bfs(start)
 