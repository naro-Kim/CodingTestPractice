# BOJ 7562 나이트의 이동
# 1. 문제 조건
#   - 
# 2. 출력 조건
#   - 
# 3. 문제 포인트
#   - BFS로 선택하는 이유는 이동방향 정의와 인접 노드를 방문하고 탐색하는 과정 때문
#   - 나이트가 이동하는 케이스 중에 최단 경로를 출력한다. 

from collections import deque 
import sys
input = sys.stdin.readline 

dx = [1, 2, -1, -2, -1, -2, 1, 2]
dy = [2, 1, -2, -1, 2, 1, -2, -1]

# BFS function definition
def BFS(start_x, start_y):
    q = deque()
    q.append((start_x,start_y))
    while q:
        x, y = q.popleft()
        # exit loop state
        if x == end_x and y == end_y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0: # length of one side over case
                continue
            # initial visit 
            if graph_list[nx][ny] == 0: # 만약 방문한 노드가 '0'으로 미방문처리 되어있다면
                graph_list[nx][ny] = graph_list[x][y] + 1 # 이전 노드까지의 경로 길이에 +1
                q.append((nx,ny))
    return graph_list[end_x][end_y]            

# 맵 구현 및 변수 설정
T = int(input()) # test case
for i in range(T):
    N = int(input()) # length of one side
    graph_dict = {i : 0 for i in range(1, N+1)} # dict로 해볼까하다 안함
    graph_list = [[0]*N for _ in range(N)]
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split()) 
    print(BFS(start_x, start_y))