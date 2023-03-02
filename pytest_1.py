import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
tmp = 0
t1 = nums[0]
t2 = nums[1]

# 일반적인 풀이
# while 1:
#   for i in range(k):
#     if(m == 0): break
#     tmp += t1
#     m -= 1
#   if(m == 0): break
#   tmp += t2
#   m-=1
count = (m // k+1)* k + (m % (k+1))
tmp = count * t1 + (m-count) * t2

print(tmp)