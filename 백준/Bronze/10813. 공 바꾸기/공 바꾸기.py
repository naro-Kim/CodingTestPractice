import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().strip().split())
balls = [x for x in range(1,N+1)]

for _ in range(M):
    i, j = map(int, input().strip().split()) 
    tmp = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = tmp

print(' '.join(map(str, balls)).strip())