import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input()) # number of coins
    coins = list(map(int, input().split())) 
    m = int(input()) # cost

    # memoization
    memo = [0] * (m + 1)
    memo[0] = 1 # 금액 범위 1~10000 초기화

    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                memo[i] += memo[i - coin]

    print(memo[m])