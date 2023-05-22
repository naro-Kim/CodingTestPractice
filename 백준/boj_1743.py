# BOJ 1743 음식물 피하기
#   1. 입력
#   - n은 세로, m은 가로, k는 음식물 갯수
#   2. 출력
#   - 탐색 후 가장 큰 그래프 (음식물 크기)
#   3. 아이디어
#   - 맵 그래프를 만든 후, 방위를 살펴 가장 큰 음식물을 생성하는 서브 그래프를 탐색한다

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 지도 구현 및 변수 설정
n,m,k = map(int,input().split())
graph = [[False]*m for _ in range(n)] # visited graph와의 구별을 위해 0과 1로 구분하기도 한다.

for i in range(k):
    r,c = map(int, input().split()) 
    graph[r-1][c-1]=True 

# 지도 탐색 코드 
ans = []
def DFS(r,c):
    global size #음식물 크기 초기화
    # 좌표가 지도를 벗어낫는지 체크
    if r < 0 or c < 0 or r > n-1 or c > m-1:
        return False
    #음식이 떨어지지 않은 곳 체크
    if graph[r][c] == False : 
        return False
    # 음식이 떨어져있다면 방문하고, 다시 방문하지 않도록 데이터를 False로 바꿈
    graph[r][c] = False
    size += 1
    ans.append(size)
    #재귀로 인접한 4방위 탐색. direction = [(1,0),(-1,0),(0,1),(0,-1)]
    DFS(r-1,c)
    DFS(r+1,c)
    DFS(r,c-1)
    DFS(r,c+1)

for r in range(n):
    for c in range(m):
        size = 0 #탐색 마다 size 초기화
        if DFS(r,c):
            continue

print(max(ans))


