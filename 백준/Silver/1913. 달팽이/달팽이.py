import sys
input = sys.stdin.readline

N = int(input())
T = int(input())

board = [[0] * N for _ in range(N)]
di = [[0, 1], [1, 0], [0, -1], [-1, 0]]

x, y = 0, 0
cnt = N**2
board[y][x] = cnt
d = 0
ans = []
while True:
    if board[y][x] == 1:
        break
    ny, nx = y + di[d][1], x + di[d][0]
    if 0 <= ny < N and 0 <= nx < N and not board[ny][nx]:
        board[ny][nx] = board[y][x] - 1
        y, x = ny, nx
    else:
        d = (d+1)%4
    cnt -= 1

for y in range(N):
    for x in range(N):
        print(board[y][x], end=' ')
        if board[y][x] == T:
            ans.append(y+1)
            ans.append(x+1)
    print()

print(ans[0], ans[1])