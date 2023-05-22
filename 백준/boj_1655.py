# BOJ 1655 가운데를 말해요
# 1. 문제 조건 
#   - 1개~ 100,000개 

import heapq as hq # 힙큐를 hq로 쓰기
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(1, n+1):
    num = int(input())
    hq.heappush(heap,(abs(num),num))
    if i%2 == 0:
        print(heap[i//2-1][1])
    elif i%2 == 1 and i != 1:
        print(heap[i//2][1])
    elif i == 1:
        print(heap[i-1][1])
         