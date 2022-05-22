"""
12강, 스택의 응용 - 수식의 후위 표기법
----------------------------------
Postfix -> 스택에 연산자를 저장해두었다가, 
우선순위를 파악하여 연산자의 pop과 push 연산을 진행

"""
from gettext import find
from multiprocessing.dummy import Array
from xml.etree.ElementPath import ops

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
    
def splitTokens(expr):
    tokens = []
    val = 0
    valProcessing = False
    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    return tokens


    valStack = ArrayStack()

    for t in tokenList:
        if type(t) is int:
            valStack.push(t)
        elif t == '*':
                val_one = valStack.pop()
                val_two = valStack.pop()
                valStack.push(val_one * val_two)
        elif t == '/':
                val_one = valStack.pop()
                val_two = valStack.pop()
                valStack.push(val_one // val_two)
        elif t == '+':
                val_one = valStack.pop()
                val_two = valStack.pop()
                valStack.push(val_one + val_two)
        elif t == '-':
                val_one = valStack.pop()
                val_two = valStack.pop()
                valStack.push(val_one - val_two)
    return valStack.pop()

def infixToPostfix(tokenList):
    prec = {
        '*' : 3,
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1
    }
    opStack = ArrayStack()
    postfixList =[]

    for t in tokenList:
        if type(t) is int:
            postfixList.append(t)
        elif t == '(':
            opStack.push(t)
        elif t == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            while opStack.size() > 0:
                if prec[opStack.peek()] >= prec[t]:
                    postfixList.append(opStack.pop())
                else:
                    break
            opStack.push(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return postfixList

def postfixEval(tokenList):
    valStack = ArrayStack()

    for t in tokenList:
        if type(t) is int:
            valStack.push(t)
        elif t == '+':
            n = valStack.pop()
            m = valStack.pop()
            valStack.push(n + m)
        elif t == '-':
            n = valStack.pop()
            m = valStack.pop()
            valStack.push(n - m)
        elif t == '*':
            n = valStack.pop()
            m = valStack.pop()
            valStack.push(n * m)
        elif t == '/':
            n = valStack.pop()
            m = valStack.pop()
            valStack.push(n // m)
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution("4+5*(5-1)"))
