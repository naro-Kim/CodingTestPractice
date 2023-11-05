'''
title: 금고털이
'''
import sys
input = sys.stdin.readline

w, n = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1], reverse=True)
result = 0

for m, p in arr:  
  if w > m:
    w -= m
    result += m*p
  else:
    result += w*p
    break 

print(result)