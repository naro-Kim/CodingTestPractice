"""
17강, Tree
---
정점(node)과 간선(edge)을 이용하여 자료구조를 추상화한 구조
이진 트리의 구현
[data] 
left, right 

"""

from boj_5430 import R


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0 # left 노드가 있다면 l = self.left.size()이고 없다면 0
        r = self.right.size() if self.right else 0
        return l+r+1

class BinaryTree:
    def __init__(self,r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0