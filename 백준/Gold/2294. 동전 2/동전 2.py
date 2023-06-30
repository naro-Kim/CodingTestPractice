import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# memoization
memo = [10001] * (k + 1)
memo[0] = 0
ans = [] # min을 출력하기 위한 배열

for _ in range(n):
    coin = int(input())
    for i in range(coin, k + 1):
            memo[i] = min(memo[i-coin]+1, memo[i])

print(-1 if memo[k] == 10001 else memo[k])