import heapq as hq
import sys
import copy
input = sys.stdin.readline

k, n = map(int,(input().split()))  
nums = list(map(int,(input().split())))
heap = copy.deepcopy(nums)
# heap = nums[:]
hq.heapify(heap)

for i in range(n):
    n_min = hq.heappop(heap)
    for j in nums:
            hq.heappush(heap, n_min*j)
            if n_min % j == 0 :
                break

print(n_min)

 