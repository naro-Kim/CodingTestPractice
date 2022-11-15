# BOJ 2637 장난감조립 
# 1. 입력
#   - n : 완제품 번호, m : 노드 관계 입력 수 
#   - 노드 관계가 3개의 자연수 X, Y, K로 주어진다. 
#   - "중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다
# 2. 출력
#   - 기본 부품의 번호와 소요 개수를 일렬로 출력
# 3. 아이디어
#   - tuple 구조를 활용한다. 

from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)] # 연결정보 그래프 
indegree = [0] * (n+1) # 오직 진입 차수만 표기
needs = [[0] * (n + 1) for _ in range(n + 1)]
parts = [] * (n+1)

for _ in range(m):
    x, y, k = map(int,input().split())
    graph[x].append((y,k))  
    if graph[x] != 0:
        for y,k in graph[x]:
            parts[x] += k  
    indegree[x] += 1
 

def topology_sort():
    res = [] # 정렬 결과를 출력할 리스트
    q = deque()
    # q에 indegree가 0인 노드를 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # q가 빌때까지 반복
    while q:
        node = q.popleft() # 정점이 0인 노드
        res.append(node) # 1. 정점이 0인 노드를 정렬 결과에 추가
        for i in graph[node]:
            indegree[i] -= 1 # 그래프에 남아있는 노드들의 indegree -1
            if indegree[i] == 0:
                q.append(i) # 새롭게 indegree == 0이 된 노드를 큐에 추가

    for i in res:
        print(i, indegree[i])


topology_sort()
