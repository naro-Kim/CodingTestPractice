def snail(board, n):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0
    x, y = 0, 0
    board[0][0] = 1
    while True:
        for i in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
                board[ny][nx] = board[y][x] + 1
                if board[ny][nx] == n ** 2:
                    return
                x, y = nx, ny
            else:
                direction = (direction+1) % 4  # 로봇 청소기 참고, 초기 방향은 우측
        if board[y][x] == n ** 2:
            return

def solution():
    t = int(input())
    for testcase in range(1, t+1):
        n = int(input())
        board = [[False]*n for _ in range(n)]
        snail(board, n)
        print(f'#{testcase}')
        for row in board:
            print(*row)


if __name__ == '__main__':
    solution()
