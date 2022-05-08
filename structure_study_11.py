"""
11강, 추상적 자료구조 - 스택, Stack
----------------------------------
정의)
    마지막에 넣었던 것부터 넣은 순서의 역순으로 꺼내지는 자료 구조를 스택 (stack) 이라고 부른다.
    이처럼 마지막에 넣은 것이 가장 먼저 꺼내어지는 성질 때문에 스택을 다른 말로는 후입선출 (LIFO; last-in first-out) 자료 구조라고도 한다.

스택에서 발생할 수 있는 오류)
    - 비어있는 스택에서 데이터 원소를 꺼내려 할 때 == 스택 언더플로우
    - 꽉 찬 스택에 데이터 원소를 넣으려 할 때 == 스택 오버플로우

스택의 추상적 자료구조 구현 방법)
    1. 배열, Array를 이용한 구현
        - 파이썬 리스트와 메서드 사용

    2. 연결리스트, Linked List를 이용한 구현
        - 이중 연결 리스트 사용

두 자료구조로 구현한 스택의 차이점)
    // C언어를 기준으로~
    - 배열 스택은 스택의 크기를 처음부터 할당해서 사용한다
    - 연결 리스트는 값을 삽입하거나 삭제할 때마다 동적으로 크기를 조절한다

구현 과정 )
    1. 스택 연산 정의 및 명세
        - size() : 현재 스택에 들어있는 데이터 원소의 수를 구함
        - isEmpty() : 현재 스택이 비어있는지 판단
        - push(x) : 데이터 원소 x를 스택에 추가
        - pop() : 스택의 맨 위 원소를 제거 또는 반환
        - peek() : 스택의 맨 위 원소를 반환 (제거하지 않음)

공부 후기 )
    명세, 정의를 바탕으로 추상 자료구조를 구현하는 걸
    파이썬으로 새롭게 배워서 재밌ㄸr.. Lr, 자신감 생겼을지도?
--------------------------------------------------------------------
"""
# 파이썬 스택 라이브러리와 스택 모듈 
#from pythonds.basic.stack import stack 
from structure_study_10 import Node
from structure_study_10 import DoublyLinkedList

#배열로 구현한 스택
class ArrayStack:
    #초기화
    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data) #list의 len method 사용

    def isEmpty(self):
        return self.size() == 0 # bool type return
    
    def push(self, item):
        self.data.append(item) #list의 append method 사용

    def pop(self):
        return self.data.pop() #list의 pop method 사용

    def peek(self):
        return self.data[-1]

#이중연결리스트로 구현한 스택
class LinkeListStack:
    #init
    def __init__(self):
        self.data = DoublyLinkedList() # 노드와 이중 연결리스트의 메서드, 구조를 참조
    
    def size(self):
        return self.data.getLength()
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size()+1, node) # 현재 사이즈 + 1 의 pos에 노드 추가
    
    def pop(self):
        return self.data.popAt(self.size())
    
    def peek(self):
        return self.data.getAt(self.size()).data

"""
연습문제 - 수식의 괄호 유효성 검사
----------------------------------
설계)
    - 수식은 왼쪽부터 한 글자씩 읽는다
    - 여는 괄호 '(', '{', '['를 만나면 스택에 푸시
    - 닫는 괄호 ')', '}', ']'를 만나면 :
        - 스택이 비어있다면 올바르지 않다
        - 스택에서 pop하여 해당 괄호가 쌍을 이루는 지 검사
            - 쌍이 아니라면 올바르지 않다
----------------------------------
"""
#주어진 문제의 함수는 아래와 같다.

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[': # 입력받은 c가 여는 괄호인 경우
            S.push(c)
        elif c in match: # 입력받은 c가 닫는 괄호인 경우
            if S.isEmpty(): # 스택이 비어있다면 올바르지 않다
                return False
            else:
                t = S.pop() # 스택에서 pop하여 여는 괄호가 쌍인지 확인
                if t != match[c]: # 쌍이 아니라면 올바르지 않다
                    return False

    # 이 부분에서 많이 헷갈렸는데, 스택에서 열린 괄호들을 팝하여 대조 검사를 하므로
    # 이후에도 스택이 남아있다면 이 알고리즘은 False를 반환해야 한다.
    return S.isEmpty()
