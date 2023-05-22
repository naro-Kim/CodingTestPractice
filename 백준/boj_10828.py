# BOJ 10828 스택
# 주어진 명령어 
# => push, pop, size, empty, top

import sys
input = sys.stdin.readline

s = []
n = int(input())
 
def empty():
    if len(s) == 0:
        print('1')
    else:
        print('0')

def top():
    if len(s) == 0:
        print('-1')
    else:
        print(s[-1]) 

def size():
    print(len(s))

def push(item):
    s.append(item) #list의 append() 메소드 사용

def pop():
    if len(s) == 0:
        print('-1')
    else:
        print(s.pop()) #list의 pop() 메소드 사용


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
    elif cmd[0] == 'top':
        top()