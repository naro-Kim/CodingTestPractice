import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().strip().split())
balls = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().strip().split()) 
    for idx in range(i-1, j):
        balls[idx] = k

print(' '.join(map(str, balls)).strip())