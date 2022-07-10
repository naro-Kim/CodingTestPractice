# BOJ 9012 괄호
# 괄호 갯수와 함께, 괄호 짝 순서도 맞아야 한다.

import sys
input = sys.stdin.readline


n = int(input())
for i in range(n):
    s = input().strip()
    left_s =[]
    right_s = [] 
    for j in s:
        if j == '(':
            left_s.append(j)
        elif j == ')':
            right_s.append(j)
    if len(left_s) == len(right_s):
        print("YES")
    else :
        print("NO")