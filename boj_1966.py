# BOJ 1966 프린터큐
from collections import deque
import sys
input = sys.stdin.readline


T = int(input()) # number of test case 
for i in range(T):
    N, M = map(int, input().split()) # N = number of docs, M = document location  
    for j in range(N):
        p = input().split()
        dq = deque()    
        dq.append(p)
        print(dq)