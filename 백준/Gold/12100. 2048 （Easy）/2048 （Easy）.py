import sys, copy

input = sys.stdin.readline

def left(board):
    for i in range(n):
        cur = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][cur] == 0:
                    board[i][cur] = tmp
                elif board[i][cur] == tmp:
                    board[i][cur] = tmp << 1
                    cur += 1
                else:
                    cur += 1
                    board[i][cur] = tmp
    return board

def right(board):
    for i in range(n):
        cur = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][cur] == 0:
                    board[i][cur] = tmp
                elif board[i][cur] == tmp:
                    board[i][cur] = tmp << 1
                    cur -= 1
                else:
                    cur -= 1
                    board[i][cur] = tmp
    return board

def up(board):
    for j in range(n):  # y축부터 옮김
        cur = 0
        for i in range(n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[cur][j] == 0:
                    board[cur][j] = tmp
                elif board[cur][j] == tmp:
                    board[cur][j] = tmp << 1
                    cur += 1
                else:
                    cur += 1
                    board[cur][j] = tmp
    return board

def down(board):
    for j in range(n):  # y축부터 옮김
        cur = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[cur][j] == 0:
                    board[cur][j] = tmp
                elif board[cur][j] == tmp:
                    board[cur][j] = tmp << 1
                    cur -= 1
                else:
                    cur -= 1
                    board[cur][j] = tmp
    return board

def DFS(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        board_copied = copy.deepcopy(board)
        if i == 0:
            DFS(left(board_copied), cnt + 1)
        elif i == 1:
            DFS(right(board_copied), cnt + 1)
        elif i == 2:
            DFS(up(board_copied), cnt + 1)
        elif i == 3:
            DFS(down(board_copied), cnt + 1)


n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

DFS(board, 0) 
print(ans)