# BOJ 1918 후위표기식 
# 1. 문제조건
#   - 피연산자는 무조건 연산자 앞에 위치한다.
#   - 연산자의 우선순위에 따라 표기식의 오른쪽에 표기한다
#   - 가장 높은 우선순위의 연산자는 가장 오른쪽에 표기한다
#
# 2. 스택 동작 구현
#   - 피연산자는 바로 result에 표기한다
#   - 연산자 혹은 괄호가 나오면 스택에 연산자를 append 한다
#   - 괄호는 생략한다
#   - 연산자를 append한 후에, 또다른 연산자가 주어지면 두 연산자의 우선순위를 비교해서 result에 append 한다.
#       - 이때, 자기 자신의 연산자는 pop하지 않는다.
#   - 연산자를 append한 후에, '('가 주어지면 스택을 전부 pop하고 ')'까지 피연산자는 result에 append 하고 연산자를 스택에 append한다.
#   - 문자열의 마지막에 result에 모든 남아있는 연산자를 pop해서 붙인다. 
#

import sys
input = sys.stdin.readline
order = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '(' : 3,
    ')' : 3,
}  
txt = input().strip() 
opstack = []
result = []
 
for i in txt:
    if i.isalpha():
        result.append(i)
    elif i == '(':
        opstack.append(i)
    elif i == ')':
        while opstack and opstack[-1] != '(':
            result.append(opstack.pop())
        opstack.pop()
    else:
        while opstack and order[i] <= order[opstack[-1]]:
                result.append(opstack.pop())       
        opstack.append(i)

opstack.reverse()
print("".join(result+opstack))