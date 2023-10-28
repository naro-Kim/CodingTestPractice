import sys
input = sys.stdin.readline

n = int(input()) 
arr = [sorted(list(map(int, input().split()))) for _ in range(2)] 
ans = 0

for i in range(n):
    ans += arr[0][i] * arr[1][n-i-1]

print(ans)