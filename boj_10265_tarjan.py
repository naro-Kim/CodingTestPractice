# BOJ 10265 엠티
# 1. 문제조건
#   - 각 사람이 원하는 '같이 갈 사람'이 주어졌을 때, 버스에 태울 수 있는 '최대 인원'을 구한다.
#   - 입력은 첫번째 줄에 사람 수 'n'과 태울 수 있는 사람 수 'k'가 주어진다.
#   - 두번째 줄에 n개의 정수가 차례대로 주어진다. 이 정수는 해당 정수 번호의 사람이 버스에 타지 않는다면, n번째 사람도 버스에 타지 않음을 의미한다. 
#   - 단, 위 조건의 역은 성립하지 않는다. n번째 사람이 타지 않는다고, 정수번째 사람이 타지 않는건 아니다.
#
# 2. 아이디어
#   - 서브 그래프가 만들어지고 서브 그래프의 크기가 num 보다 작은 그래프 중, 최대 인원을 수용하는 그래프의 숫자를 출력한다.
#
#
#
 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, k = map(int,input().split()) # n은 사람 수, k는 버스에 태울 수 있는 사람의 수이다.

# init tree(graph)
graph = {i : 0 for i in range(1, n+1)} #index번째 노드의 연결 관계를 기록한다
visited = [-1 for _ in range(n+1)] # 탐색 여부를 기록하고, True이면 해당 노드의 탐색이 끝나 다시 방문하지 않는다
cur = ['' for num in range(n)]
parent = ['' for num in range(n)] 

# make graph
list = input().split()
idx = 1
for n in list: 
    graph[idx]= int(n) # 정방향 그래프   
    idx += 1

def makeSCC(i, cur, parent, visited, st):
    time = 0
    #init discovery order and current values
    cur[i] = time
    parent[i] = time
    time += 1
    visited[i] = True
    st.append(i)

    # Traverse all vertices adjacent to current vertex
    for v in graph:
        if cur[v] == -1:
            makeSCC(v, parent, cur, visited, st)
            # check if the subtree rooted with v has a connection to one of the ancestors of i
            parent[i] = min(parent[i], parent[v])
        elif visited[v] == True:
            # if visited 
            parent[i] = min(parent[i], visited[v])

    # if found a head node, pop the stack and save the node in SCC
    w = -1
    if parent[i] == cur[i]:
        while w != i: 
            w = st.pop()
            print(w, end=' ')
            visited[w] = -1

def SCC(v):
    # Mark all the vertices as not visited
    # and initialize parent and visited
    cur = [ -1 ] * v
    parent = [ -1 ] * v
    visited = [ -1 ] * v
    st = [] 

    # call recursive helper function to find articulation points
    # in DFS tree rooted with vertex 'i'
    for i in range(v):
        if parent[i] == -1:
            makeSCC(i, cur, parent, visited, st)
    
for v in graph:
    time = 0
    print(graph[v])
    SCC(graph[v])