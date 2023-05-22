# BOJ 3665 최종순위
#   1. 입력
#   -   n개의 팀은 key가 등수이고 value가 팀 번호이다.
#   2. 출력
#   -   지난 순위 대비 쌍을 토대로 바뀐 올해 순위를 1등팀 부터 순서대로 출력한다
#   -   입력으로 주어진 정보가 올해 최종순위를 만들 수 없는 경우와 일관성없는 잘못된 정보의 경우, 'IMPOSSIBLE'을 출력한다.
#   3. 아이디어
#   -   처음 입력받은 리스트로 graph와 indegree배열을 작성한다.
#   -   이후에 올해 변경된 순위로 입력받은 노드 페어를 가지고 graph 배열의 연결 관계를 재정립한다.
from collections import deque
import sys
input = sys.stdin.readline         

def topology_sort(): 
    res = [] # 정렬 결과를 출력할 리스트
    q = deque()
    # q에 indegree가 0인 노드를 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    if not q: # indegree가 0인 노드가 없는 경우. 즉, 그래프에 사이클이 생긴 경우 
        print("IMPOSSIBLE")
        return
    
    # q가 빌때까지 반복
    while q:
        node = q.popleft() # 정점이 0인 노드
        res.append(node) # 1. 정점이 0인 노드를 정렬 결과에 추가
        for next in graph[node]:
            indegree[next] -= 1 # 그래프에 남아있는 노드들의 indegree -1
            if indegree[next] == 0:
                q.append(next) # 새롭게 indegree == 0이 된 노드를 큐에 추가

    if len(res) >= n:
        print(*res)
    else:
        print("IMPOSSIBLE")
        return

t = int(input()) # number of test cases
for _ in range(t):
    n = int(input()) # number of teams
    if n == 0:
        continue # 0이 입력된 경우, 테케를 입력받지 않고 다음 테케로 진행합니다.
    lank = deque(map(int, input().split())) # team lank of the last year
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    # 작년 랭킹의 관계
    for i in range(0,n):
        for j in range(i+1,n):
            graph[lank[i]].append(lank[j]) # 단방향 그래프이므로 append(b)만 작성
            indegree[lank[j]] += 1 # lank[j]->lank[i] 이기때문에 lank[j]를 index로 진입차수 + 1 

    # 이번 년도에 바뀐 랭킹
    changes = int(input())
    for _ in range(changes):
        up, down = map(int,input().split())
        chk = True
        # 작년의 랭킹 순위를 따져 준다.
        # 그래프는 up <- down 방향임
        if up in graph[down]: 
                graph[up].append(down)
                graph[down].remove(up)
                indegree[up] -= 1
                indegree[down] += 1 
        else :
            graph[up].remove(down)
            graph[down].append(up)
            indegree[up] += 1
            indegree[down] -= 1
    
    topology_sort()
