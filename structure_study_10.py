"""
10강, Doubly Linked Lists, 양방향(이중) 연결 리스트
--------------------------------------------------
연결 리스트를 확장한 형태.
링크를 단방향이 아니라, 양 방향으로 연결하여 이전 노드로도, 다음 노드로도 진행이 가능한 형태이다.
리스트와 처음과 끝 모두 (Head,Tail) Dummy node를 사용한다

"""

class Node:
    def __init__(self,item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,item):
        self.nodeCount = 0 #init Node count
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None # Poiniting None 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        cur = self.head
        while(cur.next.next): #tail.next가 존재하면 순회 진행.
            cur = cur.next
            result.append(cur.data)
        return result
    
    def reverse(self):
        result = []
        cur = self.tail
        while(cur.prev.prev): # head.prev가 존재하면 순회
            cur = cur.prev
            result.append(cur.data)
        return result
    
    # 이중 리스트 원소 삽입
    def insertAfter(self, prev, newNode):
        next = prev.next
        #insert
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        #count
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        #inser node before next
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        #count
        self.nodeCount += 1
        return True

    def insertAt(self,pos,newNode):
        #이게맞나...?
        #head, tail 지정 필요없음
        if pos<0 or pos > self.nodeCount:
            return None
        next = self.getAt(pos)
        return self.insertBefore(next, newNode) 
        
    def getLength(self):
        len = 0
        cur = self.head
        while(cur.next.next):
            cur = cur.next
            len += 1
        return len

    # 효율성을 위하여 이진 탐색처럼 search 범위를 나눔
    def getAt(self, pos):
        if pos<0 or pos > self.nodeCount:
            return None
        i = 0
        if pos > (self.nodeCount//2):
            cur = self.tail
            while i < self.nodeCount - pos + 1:
                cur = cur.prev
                i += 1
        else:
            cur = self.head
            while i < pos:
                cur = cur.next
                i += 1
        return cur

    def concat(self, L):
        if L.nodeCount == 0:
            return True
        
        self_last = self.tail.prev
        L_first = L.head.next

        self_last.next = L_first
        L_first.prev = self_last

        self.tail = L.tail
        self.nodeCount += L.nodeCount


    def popAfter(self, prev):
        cur = prev.next
        prev.next = cur.next
        cur.next.prev = prev # 삭제할 노드의 뒷 노드를 prev와 링크
        self.nodeCount -= 1
        return cur.data

    def popBefore(self, next):
        cur = next.prev
        next.prev = cur.prev
        cur.prev.next = next
        self.nodeCount -= 1
        return cur.data

    # dividing position.. 다른 사람들의 강의 풀이 참고
    def popAt(self, pos):
        if pos<0 or pos > self.nodeCount:
            raise IndexError
        if pos//2 > self.nodeCount: #pop After middle of position
            i = self.nodeCount
            cur = self.tail
            while i >= pos:
                cur = cur.prev
                i -= 1
        else: # pop Before middle of position
            i = 1
            cur = self.head
            while i <= pos:
                cur = cur.next
                i += 1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.nodeCount -= 1
        return cur.data

    # 중복, 불필요한 연산을 줄일 것!

    # def popAfter(self, prev):
    #     cur = prev.next
    #     if(prev.next.next): #다른 노드가 존재하면
    #         next = prev.next.next
    #         prev.next = next
    #         next.prev = prev
    #     else: #다른 노드가 없으면
    #         prev.next = self.tail
    #         self.tail.prev = prev
    #     self.nodeCount -= 1
    #     return cur.data
    
    # def popBefore(self,next):
    #     cur = next.prev
    #     if(next.prev.prev):
    #         prev = next.prev.prev
    #         next.prev = prev
    #         prev.next = next
    #     else:
    #         next.prev = self.head
    #         self.head.next = next
    #     self.nodeCount -= 1
    #     return cur.data

    # def popAt(self, pos):
    #     if pos<1 or pos>self.nodeCount:
    #         raise IndexError
    #     prev = self.getAt(pos-1)
    #     return self.popAfter(prev)