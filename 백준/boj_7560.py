from collections import deque
import sys
input=sys.stdin.readline

M, N, H = map(int, input().split())

cmd=[]
queue=deque()
for h in range(H):
    for n in range(N):
        cmd.append(list(map(int, input().split())))
        for m in range(M):
            if cmd[n][h]==1:
                queue.append((m,n,h))
print(m,n,h)
print(queue)
#m,n,h -> 가로, 세로, 높이 크기
#M,N,H로 입력받고, cmd[m][n][h]로 저장
#맨처음 list cmd에 저장 > 1인 것들 queue에 저장

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,-1,1]

def bfs():
    while queue:
        # queue에 있는 것(1인 것) pop하고 bfs
        m,n,h=queue.popleft()
        for i in range(6):
            x=m+dx[i]
            y=n+dy[i]
            z=h+dh[i]
            if -1<x<m and -1<y<n and -1<z<h:
            # 그 크기 안에서 돌 수 있도록 범위 설정
                if cmd[x][y][z] == 0:
                    # 1 주변에 0이 있다면, 1로 변경
                    # queue에 append
                    cmd[x][y][z] = cmd[m][n][h]+1
                    # 1 > 2 > 3 해서 date를 증가 시키기 위함
                    queue.append((x,y,z))
                    print(x,y,z)
bfs()
date = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if cmd[k][j][i] == 0:
                print(-1)
                exit(0)
            else:
                date = max(date, cmd[m][n][h])

print(date)
print(date -1)