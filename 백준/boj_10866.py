# BOJ 10828 덱
# 주어진 명령어 
# => push_front(x), push_back(x), pop_front(x), pop_back(x), size, empty, front, back

import sys
input = sys.stdin.readline

dq = []
n = int(input())

def push_front(item):
    dq.insert(0, item)

def push_back(item):
    dq.append(item) #list의 append() 메소드 사용

def pop_front():
    if dq:
        print(dq.pop(0)) #list의 pop() 메소드 사용
    else:
        print('-1')

def pop_back():
    if dq:
        print(dq.pop()) #list의 pop() 메소드 사용
    else:
        print('-1')

def size():
    print(len(dq))

def empty():
    if len(dq) == 0:
        print('1')
    else:
        print('0')

def front():
    if len(dq)>0:
        print(dq[0])
    else:
        print('-1')

def back():
    if len(dq)>0:
        print(dq[-1])
    else:
        print('-1')

for i in range(n):
    cmd = input().split() 
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    elif cmd[0] == 'push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()