from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    size = max([num for row in rectangle for num in row]) * 2 + 2 # 테두리의 길이를 재기 위해, 좌표*2 씩 한다
    graph = [[-1]*size for _ in range(size)]
    visited = [[False] * size for i in range(size)]
     
    for pos in rectangle: 
        x1, y1, x2, y2 = map(lambda x: x*2, pos)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0  # 직사각형의 내부
                elif graph[i][j] != 0: # 직사각형 내부가 아닐 때
                    graph[i][j] = 1 # 직사각형 테두리 x1 <= i <= x2+1 && y1 <= j <= y2+1
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited[characterX * 2][characterY * 2] = 0 # 시작 지점은 0으로 초기화
    
    while q:
        x, y = q.popleft() 
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break 
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer