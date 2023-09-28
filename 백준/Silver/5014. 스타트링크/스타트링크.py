import sys
from collections import deque
input = sys.stdin.readline
 
F, S, G, U, D = map(int, input().strip().split()) 
count = [0 for _ in range(F+1)] 

def BFS(S):
    q = deque([S])
    count[S] = 1 # 덧뺄셈에 따라 방문층인지 아닌지 확인하기 위해 visited list를 만든다.
    while q:
        cur = q.popleft()
        if cur == G: 
            return count[cur]-1  
        for i in (cur+U, cur-D):
            if 0 < i <= F and not count[i]:
                count[i] = count[cur] + 1 # add button count 
                q.append(i) # append next floor into queue 

    if count[G] == False:
        return 'use the stairs'

result = BFS(S)
print(result)