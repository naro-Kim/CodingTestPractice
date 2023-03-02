import sys
input = sys.stdin.readline

n, m = map(int,input().split())
max_num = 0
for _ in range(n): 
    arr = min(map(int,input().split()))
    if max_num < arr :
        max_num = arr

print(max_num)