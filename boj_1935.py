# BOJ 1918 후위표기식 
# 1. 문제조건
#   - 후위 표기식이 주어지고나서 피연산자에 해당하는 값이 주어진다.
#   - 계산 결과를 소숫점 둘째 자리까지 출력한다. 
#
# 2. 스택 동작 구현
#   - num 배열을 통해 txt에서 피연산자를 읽을 경우, 해당 위치에 자리잡은 숫자를 확인한다
#   - numstack안에 연산 결과를 다시 넣어주어 피연산자 갯수를 2개로 유지한다.
#

import sys
input = sys.stdin.readline
n = int(input())
txt = input().strip() 
nums = []

for i in range(n):
    nums.append(int(input())) 
 
numstack = []  
idx = 0
 
for i in txt:
    if i.isalpha():
        numstack.append(nums[ord(i)-65]) 
    else:
        r_num = numstack.pop() #오른쪽 피연산자
        l_num = numstack.pop() #왼쪽 피연산자
        if i == '*':
            numstack.append(l_num * r_num)
        elif i == '/':
            numstack.append(l_num / r_num) 
        elif i == '+':
            numstack.append(l_num + r_num)
        elif i == '-':
            numstack.append(l_num - r_num)

print(format(numstack[0], ".2f"))