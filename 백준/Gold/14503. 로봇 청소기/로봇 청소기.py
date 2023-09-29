import sys
input = sys.stdin.readline

#북동남서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
r,c,d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[r][c] = True
cnt = 1

while True:
    flag = False
    for _ in range(4):
        d = (d+3)%4
        nx = c + dx[d] # column index
        ny = r + dy[d] # row index
        if 0 <= ny <= n and  0 <= nx <= m and not map[ny][nx]:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                c = nx
                r = ny
                flag = True
                break
    if not flag:
        if map[r-dy[d]][c-dx[d]]:
            print(cnt)
            break
        else :
            r, c = r-dy[d], c-dx[d] 