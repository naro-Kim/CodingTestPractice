# BOJ 1012 유기농 배추
#   1. 입력
#   - M: 가로길이, N: 세로길이, K: 배추 수, (X,Y): 배추 좌표
#   2. 출력
#   - 테케별 최수 배추 흰 지렁이 마리수 출력
#   3. 아이디어 (테케별)
#   - M,N,X,Y를 이용해 케이스별로 맵 그래프를 만든 후, 방위를 살펴 서브 그래프를 탐색한다.
#   - 서브 그래프 탐색을 할 때 마다, 총 서브 그래프 개수를 업데이트한다.
#   - 테케별로 그래프 탐색을 마치면 총 서브 그래프 개수를 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

#지도 탐색 코드 
def DFS(y,x):
    global num # 배추 흰지렁이 수
    # 좌표가 지도를 벗어낫는지 체크
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    #집이 없는 곳 체크
    if graph[y][x] == False: 
        return False
    # 집이 있으면 방문하고, 다시 방문하지 않도록 데이터를 False으로 바꿈
    graph[y][x] = False
    num += 1
    #재귀로 인접한 4방위 탐색. direction = [(1,0),(-1,0),(0,1),(0,-1)]
    DFS(y-1,x)
    DFS(y+1,x)
    DFS(y,x-1)
    DFS(y,x+1) 
    return num

# 지도 구현 및 변수 설정
T = int(input()) # number of test case

for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[False]*(M) for _ in range(N)]
    ans = []
    for i in range(K):
        x,y = map(int, input().split()) 
        graph[y][x]=True 
    for y in range(N):
        num = 0
        for x in range(M):
            if DFS(y,x):
                ans.append(num)
                num = 0 
    print(len(ans))