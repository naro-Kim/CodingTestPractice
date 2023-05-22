# BOJ 5430 AC
# 1. 문제 조건
#   - 
# 2. 출력 조건
#   - 
# 3. 문제 포인트
#   - 명령어 p를 읽어들인다. 배열이 비어있는데 들어온 D나 올바르지 않은 명령어 상의 에러를 예외처리한다. 
#   - 빈 배열에 명령어가 들어온 경우 에러를 출력하고, dq는 출력하지 않는다. 

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    p = input().replace('RR','').strip()
    #연속된 RR은 없는거랑 같음
    err = 0
    r_cnt = 0
    num = int(input())
    str = input().strip()[1:-1].split(',') # \n 없애
    dq = deque(filter(None,str))  
    for key in p:
        if key == 'D':
            if dq:  
                if r_cnt % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                err = 1
                break
        elif key == 'R':
            r_cnt += 1
        elif len(dq) == 0 or num == 0:
            err = 1
            break
        
    
    if r_cnt % 2 != 0 :
        dq.reverse()

    if err == 0:
        print('['+ ",".join(dq)+']')
    else:
        print('error') 
