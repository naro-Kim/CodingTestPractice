# BOJ 2840 행운의 바퀴
#
# 문제 조건
#   1. 같은 글자는 두 번 등장하지 않는다.
#   2. 바퀴는 시계 방향으로만 돌아간다.
#   3. 화살표는 항상 한 곳에 위치한다.
# 
# 바퀴와 글자 조건
#   1. 바퀴를 돌릴 때마다, 멈춘 글자를 적는다
#   2. 적힌 글자를 토대로 바퀴에 쓰인 글자를 추론한다.
#
# 프로그램 동작
#   1. n칸의 바퀴를 k회 돌린다
#   2. 화살표가 가리키는 글자가 바뀐 횟수는 dq.rotate()의 실행 횟수이다.
#   3. 멈춘 글자를 배열에 기록한다
# 
# 예외 처리
#   1. 한 인덱스에 다른 글자가 존재하면 안된다. -> 멈춘 위치에 다른 글자가 적혀있다면 에러
#   2. 행운의 바퀴를 돌렸을 때 전부 같은 위치에 멈추면 단어를 알아낼 수 없다.
#
# 출력
#   1. 1번 예외에 대해서 '!' 출력
#   2. 아는 알파벳 제외 모두 '?' 출력


from collections import deque
from itertools import count
import sys
input = sys.stdin.readline
 
n,k = map(int, input().split()) 
dq = deque(['?' for i in range(n)])

for i in range(k):
    roll, char = input().split()
    roll = int(roll)
    dq.rotate(roll)
    if dq[0] == '?' and dq.count(char) < 1:
        dq[0] = char
    elif dq[0] == char and dq.count(char) == 1:
        continue        
    else:
        print('!')
        break

for j in range(n):
    print(dq[j], end= "")
 
