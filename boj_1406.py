# BOJ 1406 에디터
#
# 문제 조건
#   1. 최대 600,000 글자 입력 -> 할당과 시간 제한 관리에 주의
#   2. 길이가 L인 문자열에서 커서의 위치는 L+1가지로 위치할 수 있다.
#
# 시간 제한
#   1. 0.3초의 시간 제한 -> 일반적인 연산은 시간이 너무 오래 걸리게 된다.
#   2. 인덱스를 찾는 연산을 O(log n)의 시간으로 실행하려면, Binary Search처럼 분할하는 방법을 생각하자.
# 
# 아이디어
#   1. 커서의 왼쪽에서 삭제, 추가 연산이 일어난다. -> 커서의 오른쪽과 왼쪽을 분리하여 저장
#   2. dq에서 pop과 popleft, append와 appendleft의 평균 시간복잡도는 O(1)이다.
# 
# 프로그램 동작
#   1. 원래 입력받은 문자열 str과 커서를 대조하여 L과 D의 연산 조건을 비교한다.
#   2. 커서는 dq[-1]로 시작한다
#  
# 출력 
 
import time 

start_time = time.time()

from collections import deque

import sys
input = sys.stdin.readline

n = input()
m = int(input())
print(m)

dq = deque(n)
ans_dq = deque()
cur = dq[-1]

for i in range(m):
    cmd = input().strip()
    if cmd[0] == 'L':
        if cur != dq[0]:
            ans_dq.append(dq.popleft())
            print('L 실행')
            cur = dq[0]
    elif cmd[0] == 'D':
        if cur != dq[-1]:
     
            print('D 실행')
    elif cmd[0] == 'B':
        if len(right_dq) > 1:
            left_dq.pop()
        print('B 실행')
    elif cmd[0] == 'P':
        ans_dq.appendleft()
        print('C 실행, cmd[2] :', cmd[2])
        

for i in range(len(left_dq)-1):
    print(left_dq[i], end="")

end_time = time.time()
print('걸린 시간 : ', end_time - start_time)