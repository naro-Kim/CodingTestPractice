'''
title: 지도자동구축
풀이:
# [4, 9, 25 ... ] = [2*2, 3*3, 5*5]..
# 내부로 쪼개 들어간다(재귀)의 아이디어가 아니라, 좌표 시뮬레이션으로 생각해보자.
# 좌표 하나 당 하나의 하나의 점이 존재하고, 사각형 지도 생성에 너비는 각 변의 곱인 것과 같다
# 그렇다면, 각 변의 길이에 대한 식을 아래처럼 나타낼 수 있다. 변 길이를 구하는 로직을 수학에 대입해 생각해야 한다. dp를 풀고싶다면 점화식 규칙 찾기에 익숙해지자
# dp = [2, 3, 5, ...] = 
# 0이면 2
# 1이면 3 == 2 + 1 == dp[i-1] + 1 == dp[0] + 2**0
# 2이면 5 == 3 + 2 == dp[i-1] + 2 = dp[1] + 2**1
'''
import sys
input = sys.stdin.readline


dp = [0] * 16
dp[0], dp[1], dp[2] = 2, 3, 5

n = int(input())
for i in range(2, n+1):
  dp[i] = dp[i-1] + 2**(i-1)

print(dp[n]**2) # 변길이 제곱