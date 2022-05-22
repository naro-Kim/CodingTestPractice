"""
14강, 큐 (Queue) ~ 환형 큐 (Cicular Queue) ~ 우선순위 큐 (Priority Queue)
----------------------------------
data element를 보관하는 Linear Data Structure
FIFO (First-In-First-Out) 구조.
대기열의 형태

# from pythonds.basic.queue import Queue  라이브러리를 사용할 수 있음.

연산의 종류)
    1. enqueue(x))
    :   Q.enqueue(Argument) 형태로 사용
        - 자료구조의 마지막에 자료를 삽입

    2. dequeue(x)
    :   Q.dequeue(Argument) 형태로 사용
        - 자료구조에 가장 먼저 들어간 자료가 나옴

    3. size() : 현재 큐의 데이터 원소의 수를 구함
    4. isEmpty() : 현재 큐가 비어있는지 판단
    5. peek() : 큐의 맨앞에 저장된 데이터 원소를 반환


Queue의 동작)
    - 추상적 자료구조 형태로 Queue를 정의

큐의 구현)
    1. Array
    : Python List와 Method 사용

    2. Doubly Linked List
    : 양방향 연결 리스트를 계속해서 사용하여 구현함

"""
from structure_study_10 import Node, DoublyLinkedList

class ArrayQueue:

    def __init__(self):
        self.data = [] # array init

    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        self.data.pop[0]
    
    def peek(self):
        return self.data[0]

class LinkedQueue:
    def __init__(self) -> None:
        pass

class CircularQueue:

    #self와 배열크기 n으로 초기화
    def __init__(self, n): 
        self.maxCount = n
        self.data = [None]*n
        self.count = 0
        self.front = self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.maxCount # 큐 데이터 아이템의 갯수와 비교
    
    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue Full')
        self.rear = (self.rear + 1) % self.maxCount # size는 count를 리턴하므로 주의!
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.data.count == 0:
            raise IndexError('Queue Empty')
            # self.isEmpty():
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.data.count == 0:
            raise IndexError('Queue Empty')
        return self.data[(self.front+1) % self.maxCount]

"""
Priority Queue의 구현 시, 방법은 두 가지가 있다.
1. Enqueue시 우선순위 순서를 유지
2. Dequeue시 우선순위 선택

이번 실습에선 Doubly Linked List를 통해 구현

"""
class PriorityQueue:
    def __init__(self,x):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next != self.queue.tail and curr.next.data > newNode.data:
            curr = curr.next
        self.queue.insertAfter(curr,newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength())