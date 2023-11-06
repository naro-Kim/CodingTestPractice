'''
x[i]는 퀸이 해당 행에서 몇 열에 위치하는가 이다.
ex/ x[1:n+1] = [2,4,1,3]이라면 첫번째 행의 퀸은 2열에, 두번째 행의 퀸은 4열에, 세번째 퀸의 행은 1열, 마지막 퀸은 3열에 위치하는 것이다.

'''
import sys
input = sys.stdin.readline

def n_queen(i): # row[i] is the position of the queen in columns
    global ans
    if i == n:
        ans += 1
        return 
    else:
        for column in range(n):
            row[i] = column # put queen on the column of row in a board
            if is_promising(i): 
                n_queen(i+1) # traverse next row of the board

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i]-row[x]) == abs(x-i): #같은 열에 위치하거나, 대각선에 위치한다면
            return False
    return True

n = int(input())
row = [0]*n
ans = 0
n_queen(0)

print(ans)
