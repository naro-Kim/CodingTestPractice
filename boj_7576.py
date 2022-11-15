# BOJ 7576 토마토 
# 1. 문제 조건
#   - 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 2. 출력 조건
#   - 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
# 3. 문제 포인트
#   - BFS로 선택하는 이유는 이동방향 정의와 인접 노드를 방문하고 탐색하는 과정 때문
#   - 나이트가 이동하는 케이스 중에 최단 경로를 출력한다. 

from collections import deque 
import sys
input = sys.stdin.readline 

dx = [0, 0, 1, 1]
dy = [1, 0, 1 ,0]

# BFS function definition
def BFS():
    ans = 0
    q = deque()
    for i in range(M):
        for j in range(N): 
            if graph[j][i] == 1: #이미 토마토가 익어있다면 queue append
                q.append([j,i])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= M-1 or ny >= N-1 or nx < 0 or ny < 0: # length of one side over case
                continue
            # initial visit 
            if graph[ny][nx] == 0: # 만약 방문한 노드가 '0'으로 미방문처리 되어있다면
                graph[ny][nx] = 1 # 경로 처리 대신 방문 처리만 진행
                q.append((ny,nx))
        ans += 1        
    return ans

# 그래프 구현 및 변수 설정
M, N = map(int,input().split()) # test case 
graph = [] 
for i in range(N):
    graph.append(list(map(int,(input().split())))) 

BFS() # bfs 실행
## 여러분들의 도움~ 
