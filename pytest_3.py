# type of calculation
# 1. N -1
# 2. N / K ( only possible if N % K != 0)


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

# while n >= k:
#     if n % k != 0:
#       n -= 1
#     else:
#         n //= k
#     cnt += 1

# while n > 1:
#    n -= 1
#    cnt += 1 

while 1:
    t = (n//k)*k
    cnt += n-t
    n = t
    if n < k :
        break
    cnt += 1
    n //= k

cnt += n-1

print(cnt)
