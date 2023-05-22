# BOJ 11725 트리의 부모 찾기
# 1. 문제 조건
#   - 첫 입력에 노드 개수가 주어진다.
#   - 루트 노드는 1이고, 두번째 줄 입력부터 트리상에서 연결된 두 정점이 주어진다.
#   - 출력은 '2' 노드의 부모부터, 마지막 노드의 부모까지 순차적으로 출력한다.
#
# 2. 문제 해석
#   - 두번째 입력부터 두 노드가 주어지는데, 모든 입력을 받으면 노드간의 관계를 통해 트리를 그릴 수 있다.
#   - 그려진 트리를 Traverse하며 2번 노드부터 마지막 노드까지 부모 노드를 판별해 출력한다.
#
# 3. 알고리즘
#   - 한줄요약) 트리를 먼저 그린 후에, 그려진 트리를 DFS 혹은 BFS로 순회하며 parent를 출력한다

#   [DFS 알고리즘]
#   - 1번 노드부터 시작해서, 마지막 leaf까지 탐색을 진행한다. 즉, 탐색의 순서는 부모 -> 자식 노드 순이다.
#   - 1번과 연결되어 있으면서 아직 방문하지 않은 노드들을 방문한다.
#   - 탐색 중인 노드에 child가 있다면 탐색중인 노드는 해당 child의 parent가 되고 이를 visited 배열에 탐색중인 노드 index의 parent로 저장한다.
#   - visited 배열에, n번째 index에 parent를 입력했으므로 visited 정보가 False가 아닌 n번 노드는 다시 방문하지 않는다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# number of nodes
n = int(input())
# init tree(graph)
tree = [[]for _ in range(n+1)] #index번째 노드의 연결 관계를 기록한다
visited = [False for _ in range(n+1)] # 탐색 여부를 ㅁ ㅁ 기록하고, True이면 해당 노드의 탐색이 끝나 다시 방문하지 않는다
ans = [1 for _ in range(n+1)] # parent를 기록한다. 초기값은 1로 초기화한다

# 1번 노드를 제외한 노드 입력으로 트리 생성
for i in range(n-1):
    j, k = map(int,input().split())
    tree[j].append(k)
    tree[k].append(j)

# DFS의 정의
def dfs(val):
    for i in tree[val]:
        if visited[i] == False:
            visited[i] = val
            dfs(i) #재귀적으로 DFS

dfs(1) #1번 노드부터 n번 노드까지 탐색을 진행한다.
for i in range(2, n+1):
    print(visited[i]) # 2번노드부터 시작하여 마지막 노드까지 부모를 출력한다.
