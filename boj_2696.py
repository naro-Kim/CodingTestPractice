# BOJ 2696 중앙값 구하기
# 1. 문제 조건 
#   - 홀수번째 수를 읽어들일 때 마다, 지금까지 입력받은 값들의 중간값을 출력하기
#   - 테스트케이스 T는 1~1000까지 주어지고, 수열의 크기 M은 1~9999까지 주어진다.
#   

import heapq as hq # 힙큐를 hq로 쓰기
import sys
input = sys.stdin.readline

l_heap = []
r_heap = []
t = int(input())

for i in range(t): 
    n = int(input())
    cnt = 0
    for j in range(n):
        nums = list(map(int, sys.stdin.readline().split()))
        l_heap = [nums[0]]
        r_heap = []
        mid = -l_heap[0]
        for k in nums:
            cnt += 1
            if  cnt % 2 == 1:
                if hq.heappop(r_heap):
                    
            if k <= mid:
                hq.heappush(l_heap,k)
            else :
                hq.heappush(r_heap,k)
        if cnt == 10:
            print('\n')
            cnt = 0