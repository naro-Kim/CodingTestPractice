import sys, copy
from collections import deque
input = sys.stdin.readline

# rotate diraection for each type of cctvs
# 1~5 type of cctvs
rotate = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]], [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n,m = map(int, input().split())
cctv = deque()  
ans = n*m
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append((i, j, graph[i][j]))


def check(copied_graph, rotate, y, x):
    for dir in rotate:
        nx = x
        ny = y
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and copied_graph[ny][nx] != 6:
                if copied_graph[ny][nx] == 0:
                    copied_graph[ny][nx] = '#'
            else:
                break

def DFS(depth, graph):
    global ans
    copied_graph = copy.deepcopy(graph)

    # DFS exit condition
    # cctv는 최대 8개
    if depth == len(cctv): 
        cnt = 0
        for row in graph: # check for y axis
            cnt += row.count(0) # count blind spot
        ans = min(cnt, ans) 
        return
    
    y, x, type = cctv[depth]
    for i in rotate[type]:
        check(copied_graph, i, y, x)
        DFS(depth + 1, copied_graph)
        copied_graph = copy.deepcopy(graph)
 
DFS(0, graph)
print(ans) 