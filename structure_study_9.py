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
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        #prev가 마지막 노드인 경우
        if prev.next is None: # prev == self.tail
            return None 

        # prev가 마지막 노드가 아닌경우
        cur = prev.next
        prev.next = cur.next # cur.next가 존재하는 경우와 존재하지 않는 경우 모두를 포함함
        #cur이 마지막 노드인 경우
        if cur.next == None:
            self.tail = prev

        self.nodeCount -= 1
        return cur.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount+1:
            raise IndexError
        else:
            prev = self.getAt(pos-1)
            return self.popAfter(prev)


def solution(x):
    return 0