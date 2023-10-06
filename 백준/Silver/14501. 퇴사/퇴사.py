import sys
input = sys.stdin.readline

n = int(input()) # n일 동안 상담받는다
tp = [tuple(map(int, input().split())) for _ in range(n)] # t와 p를 입력받는다 
dp = [0] *(n+1) # 수익 계산 배열


for i in range(n-1, -1, -1): 
    # i는 상담 일차 
    t = tp[i][0] # 현재까지 상담에 필요한 기간
    p = tp[i][1] # 현재일의 상담 비용
    if t + i > n: # 상담을 퇴사전까지 진행할 수 없다면
        dp[i] = dp[i+1] # 이전 케이스가 최대의 이익
    else:
        # 상담을 퇴사전에 끝내는 경우
        dp[i] = max(dp[i+1], dp[i+t] + p) 

print(dp[0])