# BOJ 10828 큐
# 주어진 명령어 
# => push, pop, size, empty, front, back

import sys
input = sys.stdin.readline

s = []
n = int(input())

def push(item):
    s.append(item) #list의 append() 메소드 사용

def pop():
    if s:
        print(s.pop(0)) #list의 pop() 메소드 사용
    else:
        print('-1')

def size():
    print(len(s))

def empty():
    if len(s) == 0:
        print('1')
    else:
        print('0')

def front():
    if len(s)>0:
        print(s[0])
    else:
        print('-1')

def back():
    if len(s)>0:
        print(s[-1])
    else:
        print('-1')

for i in range(n):
    cmd = input().split() 
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()