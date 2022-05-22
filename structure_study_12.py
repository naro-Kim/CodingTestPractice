"""
12강, 스택의 응용 - 수식의 후위 표기법
----------------------------------
Postfix -> 스택에 연산자를 저장해두었다가, 
우선순위를 파악하여 연산자의 pop과 push 연산을 진행

"""
from gettext import find

class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        self.data.pop()
    
    def peek(self):
        return self.data[-1]   

prec = {
    '*' : 3, '/' : 3,
    '+' : 2, '-' : 2,
    '(' : 1
} 

def solution(S):
    #init stack obj
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if c.isalpha():
            # 피연산자인 경우 그대로 표기
            answer += c 
        elif c in '({[':
            #여는 괄호인 경우 
            opStack.push(c)
        elif c in ')}]':
            #닫는 괄호인 경우
            while opStack.peek() != '(':
                answer += opStack.pop() # 여는 괄호 이전까지 answer에 표기
            opStack.pop() # 여는 괄호도 스택에서 제거
        else: 
            #연산자인 경우 
            while(not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]):
                answer += opStack.pop()
            opStack.push(c)
    
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

str = input()   

print(solution(str))