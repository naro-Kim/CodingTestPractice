# BOJ 5397 키로거
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

# left_dq는 커서 좌측 데이터이고 len(left_dq)는 커서 좌측 데이터의 갯수이다
# right_dq는 커서 우측 데이터이고 len(right_dq)는 커서 우측 데이터의 갯수이다
for i in range(t): 
    key = input().strip()
    left_dq = deque()
    right_dq = deque()
    
    for j in key:
        if  j == '<':
            if len(left_dq):
                right_dq.append(left_dq.pop())  
        elif j == '>':
            if len(right_dq):
                left_dq.append(right_dq.pop()) 
        elif j == '-':
            if len(left_dq):
                left_dq.pop() 
        else:
            #char인 경우 append
            left_dq.append(j) 
        
    right_dq.reverse() #deque를 list로 converting 하는 것은 O(n)이 소요되므로 그냥 reverse
    print("".join(left_dq+right_dq))