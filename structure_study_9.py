"""
9강, Linked List, 연결 리스트의 응용
----------------------------
빈번하게 리스트의 노드 삽입과 삭제가 일어나는 경우
유연하게 작동할 수 있다.

다만, 지금까지 구현한 연결리스트 자료구조에서는 삽입과 삭제가 선형 탐색을 통해 이루어지기 때문에,
더 나은 효율성을 위해 변형된 연결리스트 메소드를 구현하고자 한다.

그 메소드는 아래와 같다.
    - insertAfter(prev, newNode) : 이전 노드가 주어졌을 때 다음 노드로 newNode를 삽입한다.
    - popAfter(prev) : 이전 노드가 주어졌을 때 다음 노드를 삭제한다.
위 두가지 메소드를 구상할 때 고려해야할 점은, 이전 노드가 주어지지 않은 경우 - 즉, 맨 첫 노드를 삽입하거나 삭제하는 경우에
어떻게 대처할 것인가에 대한 점이다.

이에 대처하기 위해, 연결 리스트의 맨 앞, index "0"에 "None / Null"의 Dummy node를 추가한다.
이렇게 Dummy node가 Head가 되면서 

"""


class Node:

	def __init__(self, item):
		self.data = item
		self.next = None


class LinkedList:

	def __init__(self):
		self.nodeCount = 0
		self.head = Node(None) # Dummy node init
		self.tail = None
		self.head.next = self.tail


	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s


	def getLength(self):
		return self.nodeCount


	def traverse(self):
		result = []
		curr = self.head
		while curr.next: # curr.next 링크가 있다면 반복
			curr = curr.next
			result.append(curr.data)
		return result


	def getAt(self, pos):
		if pos < 0 or pos > self.nodeCount: # 인덱스 0이 생기면서 pos 대조 조건이 바뀜
			return None

		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1

		return curr # pos ==0 이면 self[0]번째 노드 리턴

    # prevNode 다음에 노드 삽입 메소드
	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
		if prev.next is None: # 마지막 노드 삽입의 경우
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True

    # 지정한 pos에 노드 삽입 메소드
	def insertAt(self, pos, newNode):
		if pos < 1 or pos > self.nodeCount + 1:
			return False

		if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail 
            # pos=1이면서 pos== nCnt+1이면 빈 리스트에 삽입하는 것이되어 tail을 설정하면 안됨
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode) 

	def concat(self, L):
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount
    