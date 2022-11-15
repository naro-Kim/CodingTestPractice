# BOJ 11724 연결 요소의 개수
# 1. 문제 조건
#   - 첫 입력에 노드 개수 n과 간선의 개수 m가 주어진다.
#   - 루트 노드는 1이고, 두번째 줄 입력부터 트리상에서 연결된 두 정점이 주어진다.
#   - 출력은 '2' 노드의 부모부터, 마지막 노드의 부모까지 순차적으로 출력한다.
#
# 2. 문제 해석
#   연결 요소의 개수를 알아내기 위한 방법은 그래프를 탐색하는 bfs와 dfs에서 시작한다. 
#   위와 같이 입력이 주어지고 그래프가 그려졌을 때, 프로그램은 아직 그래프를 탐색하지 않은 상태이다. 
#   그래프의 탐색 방법인 DFS와 BFS는 연결되어 있는 간선만을 따라 탐색할 수 있고, 
#   하나의 그래프 안에서 탐색 과정 중에 이미 방문한 정점은 모두 visit check 과정을 거쳐 다시 탐색하지 않는다.
#   따라서, 가장 먼저 탐색 전에 count 변수를 만들어 전체 그래프에서 연결된 간선을 탐색하고 나면 
#   count 변수의 값을 1씩 증가시키며 전체 그래프 내의 연결 요소의 개수를 셀 수 있다.
#
#

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# n = number of nodes
# m = number of edges
n, m = map(int, input().split())

cnt = 0 # count connected component 

# init tree(graph)
graph = [[]for _ in range(n+1)] #index번째 노드의 연결 관계를 기록한다
visited = [False for _ in range(n+1)] # 탐색 여부를 기록하고, True이면 해당 노드의 탐색이 끝나 다시 방문하지 않는다

#간선 개수 만큼 그래프 작성
for i in range(m):
    j, k = map(int,input().split())
    graph[j].append(k)
    graph[k].append(j)

# DFS의 정의
def dfs(val):
    # visited check
    visited[val] = True #다시 방문하지 않는다.
    for i in graph[val]:
        if visited[i] == False:
            visited[i] = True # 방문했음을 T/F로 기록한다. 부모 노드가 필요없으므로 i는 저장하지 않는다.
            dfs(i) #재귀적으로 DFS

#1번 노드부터 n번 노드까지 탐색을 진행한다.
for i in range(1, n+1):
    if visited[i] == False:
        cnt+=1
        dfs(i)  

print(cnt)
