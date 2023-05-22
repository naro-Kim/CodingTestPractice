# BOJ 2164 카드2
# 1. 문제조건
#   - 카드 덱의 1번 카드는 pop
#   - 카드 덱의 2번 카드를 n번 카드 앞으로 옮긴다
#   - 숫자가 한장이 남을 때까지 반복하고 마지막에 남는 카드를 출력한다.
from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) 
dq = deque([i for i in range(1, n+1)])

while len(dq) > 1: 
    dq.popleft()
    tmp = dq.popleft()
    dq.append(tmp)

print(*dq)
