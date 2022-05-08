"""
Linked List, 연결 리스트
-----------------------

추상적 자료구조 (Abstract Data Structure)
- Data
    ex. 정수, 문자열, 레코드 ..

- A set if operations
    - 데이터에 대해 추상적으로 작동하는 연산
    ex. 삽입, 삭제, 순회, 정렬, 탐색 ...

연결 리스트의 기본 추상적 자료 구조
- Node
    - Data + Link(next)
    - 아래와 같은 구조를 자료 구조로 정의해야한다.
        - Head : 맨 앞 노드
        - Tail : 맨 끝 노드
        - N : 총 노드 갯수

배열과 비교한 연결리스트의 단점

                      배열        연결 리스트
---------------------------------------------
저장공간        |  연속한 위치     임의의 위치
특정 원소 지칭  |   매우 간편   선형탐색과 유사
                      O(1)           O(n)    
---------------------------------------------                      

"""

#노드 클래스 생성자 
class Node:
    def __init__(self,item):
            self.data = item
            self.next = None    

#연결 리스트 생성자
class LinkedList:
    def __init__(self):
            self.nodeCnt = 0
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