# BOJ 2667 단지번호붙이기
#   1. 입력
#   - n은 지도의 크기, 가로 == 세로, 두번째 줄부터 N줄까지 집 정보가 입력됨
#   2. 출력
#   - 총 단지 수와 단지 별 가구수 출력
#   3. 아이디어
#   - 맵 그래프를 만든 후, 방위를 살펴 서브 그래프를 탐색한다.
#   - 서브 그래프 탐색을 할 때 마다, '총 단지수'를 업데이트한다.
#   - 서브 그래프 탐색을 완료하면 '단지 내 가구 수'를 출력한다.

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 지도 구현 및 변수 설정
N = int(input())
graph = []
ans = [] # 단지 내 가구 수를 기록

for i in range(N):
    list = input().strip()
    tmp = []
    for j in list:
        tmp.append(int(j))
    graph.append(tmp) 

#지도 탐색 코드 
def DFS(x,y):
    global size
    # 좌표가 지도를 벗어낫는지 체크
    if x < 0 or y < 0 or x > N-1 or y > N-1:
        return False
    #집이 없는 곳 체크
    if graph[x][y] == 0 : 
        return False
    # 집이 있으면 방문하고, 다시 방문하지 않도록 데이터를 0으로 바꿈
    graph[x][y] = 0
    size += 1
    #재귀로 인접한 4방위 탐색. direction = [(1,0),(-1,0),(0,1),(0,-1)]
    DFS(x-1,y)
    DFS(x+1,y)
    DFS(x,y-1)
    DFS(x,y+1) 
    return size

for x in range(N):
    size = 0
    for y in range(N):
        if DFS(x,y):
            ans.append(size)
            size = 0

print(len(ans))
ans.sort()
for i in ans:
    print(i)
