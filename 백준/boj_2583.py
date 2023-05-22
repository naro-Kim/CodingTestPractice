# BOJ 2583 영역 구하기
#   1. 입력
#   - M: 세로길이, N:가로 길이, K: 직사각형 좌표 개수
#   2. 출력
#   - 직사각형 외부의 각 분할 영역의 크기
#   3. 아이디어
#   - 맵 그래프를 만든 후, 방위를 살펴 서브 그래프를 탐색한다.
#   - 서브 그래프 탐색을 할 때 마다, 0과 1을 뒤집는다.
#   - 뒤집힌 서브 그래프를 탐색해 서브 그래프마다의 너비를 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 지도 및 변수 선언
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
ans = [] # 서브그래프 너비 기록

# 지도 설정
for i in range(K):
    lx, ly, rx, ry = map(int, input().split())
    #항상 rx-lx>0, ry-ly>0을 만족
    for x in range(rx, N):
        for y in range(ry, M): 
            graph[x][y] = 1

print(graph)

#지도 탐색 코드 
# def DFS(x,y):
#     global size
#     # 좌표가 지도를 벗어낫는지 체크
#     if x < 0 or y < 0 or x > N-1 or y > N-1:
#         return False
#     #집이 없는 곳 체크
#     if graph[x][y] == 0 : 
#         graph[x][y] == 1
#     # 집이 있으면 방문하고, 다시 방문하지 않도록 데이터를 0으로 바꿈
#     graph[x][y] = 0
#     size += 1
#     #재귀로 인접한 4방위 탐색. direction = [(1,0),(-1,0),(0,1),(0,-1)]
#     DFS(x-1,y)
#     DFS(x+1,y)
#     DFS(x,y-1)
#     DFS(x,y+1) 
#     return size

# for x in range(N):
#     size = 0
#     for y in range(N):
#         if DFS(x,y):
#             ans.append(size)
#             size = 0
  
# for i in ans:
#     print(i)


# ```
# for i in range(len(arr)-1):
# 	tmp_i = arr[i]
# 	for j in arr:
# 		tmp_j = j
# 		if j != tmp_i:
# 			set1.append((tmp_i,j))
# 		for k in arr:
# 			if k != tmp_i && k != tmp_j:
# 				set2.append(())
	
# def manhattan_distance(pt1, pt2):
#   dist = 0
#   for i in range(len(pt1)):
#     distance += abs(pt1[i] - pt2[i])
#   return distance
# ```