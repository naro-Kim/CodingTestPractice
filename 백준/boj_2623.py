# BOJ 2623 음악프로그램 
# 0.위상정렬 문제인 조건
#   1. 상대적인 비교 이후 정렬한다
#   2. 일부만 비교한다 
#   3. 비교 결과 두 원소의 순서가 정해진다
# 1. 입력
#   - 음악프로그램의 순서 관계가 일렬의 리스트로 주어진다. 
#   - 노드 관계는 리스트의 마지막 원소 이전까지만 입력하면 됨 !! 기본 위상정렬 코드에서 달라지는 점임. 

from collections import deque
import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    artist = list(map(int,input().split()))
    for i in range(1, artist[0]): 
        graph[artist[i]].append(artist[i+1]) # i번쨰 artist는 i+1번째 artist와 연결되어 있음.
        indegree[artist[i+1]] += 1

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
        for next in graph[node]:
            indegree[next] -= 1 # 그래프에 남아있는 노드들의 indegree -1
            if indegree[next] == 0:
                q.append(next) # 새롭게 indegree == 0이 된 노드를 큐에 추가

    if len(res) == n:
        for i in res:
            print(i)
    else:
        print(0)

topology_sort()
