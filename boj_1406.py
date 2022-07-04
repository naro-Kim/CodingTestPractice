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
#   2. 커서를 할당하기 보다, 덱의 저장과 입출력을 잘 살펴보자.
#   3. 출력 시, deque는 스택처럼 출력할 것임 FIFO


from collections import deque
import sys
input = sys.stdin.readline


dq = deque(input().strip())
r_dq = deque()
m = int(input())  

# len(dq)는 커서 좌측 데이터의 갯수이다
# len(tmp_dq)는 커서 우측 데이터의 갯수이다

for i in range(m):
    cmd = input().strip()
    if cmd[0] == 'L':
        if len(dq) > 0:
            r_dq.append(dq.pop()) 
    elif cmd[0] == 'D':
        if len(r_dq) > 0:
            dq.append(r_dq.pop()) 
    elif cmd[0] == 'B':
        if len(dq)>0:
            dq.pop() 
    elif cmd[0] == 'P':
        dq.append(cmd[2])  

r_dq.reverse()
dq += r_dq
# dq += r_dq 과같이 concatenation으로도 쓸 수 있지만, splice 사용을 권장하고 있다.

while len(dq):
    print(dq.popleft(), end="")