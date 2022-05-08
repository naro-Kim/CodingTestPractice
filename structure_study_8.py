"""
Linked List, 연결 리스트
----------------------------
O(n) 상수 시간을 소요하여 삽입, 삭제를 진행한다.

"""


#노드 클래스 생성자  
class Node:
    def __init__(self,item):
            self.data = item
            self.next = None    

#연결 리스트 생성자
class LinkedList:
    def __init__(self):
            self.nodeCount = 0
            self.head = None
            self.tail = None

    # pos 위치의 노드 인덱스를 찾는 method
    def getAt(self,pos):
        if pos <= 0 or pos > self.nodeCount: # 대소 비교로 선형탐색시간이 걸리지 않도록 변경
            return None
        i = 1
        cur = self.head
        for i in range(pos):
            cur = cur.next
        return cur

    def traverse(self):
        #모든 노드의 데이터를 리턴하는 함수
        ans = []
        cur = self.head #traverse할 노드의 헤드
        while cur is not None: #노드 데이터가 존재하는 경우
            cur = cur.data 
            ans.append(cur) #데이터를 ans list에 append
            cur = cur.next #다음 노드 순회
        return ans

    def getLength(self):
        return self.nodeCount

    # element insertion, 연결리스트 원소 삽입
    # pos가 가리키는 위치에 newNode를 삽입하고 성공과 실패에 따라 T/F 리턴
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount+1:
            return False # node 삽입 위치가 올바른지 판별 

        #맨 앞에 삽입하는 경우
        if pos == 1:
            newNode.next = self.head
            self.head = newNode               
 
        else:
            if pos == self.nodeCount+1: # 맨 끝에 삽입하는 경우
                prevNode = self.tail
            else:
                prevNode = self.getAt(pos-1)
            newNode.next = prevNode.next
            prevNode.next = newNode
           
        
        self.nodeCount += 1 # 정상적으로 노드를 삽입한 경우, 노드 갯수를 하나 증가시킨다
        return True

    # 맨 첫 노드 / 마지막 노드를 삭제하는 경우
    # 노드 갯수가 1인 경우
    # 평범한 노드를 삭제하는 경우 
    # 위 4가지 테스트 케이스 조건을 모두 만족해야함 

    def popAt(self, pos):
        data = 0
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        if self.nodeCount == 1: # 노드 갯수가 1인 경우
            data = self.head.data
            self.head = None # Head와 Tail 삭제
            self.tail = None
        
        else: 
            if pos == 1: # 첫 노드를 삭제하는 경우
                data = self.head.data 
                self.head = self.head.next # 두번째 노드가 Head
                self.nodeCount -= 1
                return data
            #  getAt()을 한 번만 쓰기 위해서 pos==1 조건에 리턴을 달고
            #  pos > 1인 케이스에만 적용되게 만듦    
            #  pos > 1이어서 getAt(pos-1)이 잘 작동함
            prev = self.getAt(pos-1) # 이전 노드를 복사
            if pos == self.nodeCount: # 마지막 노드를 삭제하는 경우
                data = self.tail.data   
                self.tail = prev # Tail을 이전 노드로 조정
                prev.next = None # Tail의 next link 삭제
            else: # 1 < pos < nodeCount
                data = prev.next.data   
                prev.next = prev.next.next # pos 노드를 삭제했으므로 link를 다음다음 노드로 조정

        self.nodeCount -= 1 #전체 노드갯수 -1
        return data 



    def concate(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


L = LinkedList()
a = Node(13)
b = Node(27)
L.head = a
L.tail = b
L.nodeCount = 2
a.next = b

L.popAt(1)
