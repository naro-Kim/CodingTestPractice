# BOJ 11715 트리의 부모 찾기
from collections import deque
from operator import itemgetter
import sys
sys.setrecursionlimit(10**8) # 재귀횟수 제한
input = sys.stdin.readline

class sw():
    def __init__(self, sw, item, head):
        self.sw = sw
        self.item = item 
        self.head = head
        self.next = None 
        #다음으로 입력받은 섬의 head가 self의 idx와 일치하면 next 연결시킴

"""
구출의 조건 ?
양 : n번 섬에서 1번섬으로 이동
늑대 : 이동 x

[예제1]
2 -> 3 연결되어있음
2번섬 (양 100), 3번섬과 연결됨
3번섬 (늑대 50), 1번섬과 연결됨
4번섬 (양 10), 1번섬과 연결

즉, 4번섬은 바로 탈출
2번섬은 3번섬을 거치므로 양의 값을 줄임 

-----------
[구현]
n까지 반복문 내에서 입력받고, 섬의 순서는 enumerator 사용?
입력받으면 늑대와 양의 판별을 true / fallse 판별?
1. 입력받아서 str[0] == s면 sw.sw = true  / w면 sw.sw = false
    sw.sw = t면 그냥 무사 통과, f면 수를 줄임

2. sw.item = str[1] 저장
3. sw.head = str[2] 저장

모두 다 입력받은 후에, 가장 마지막 섬에서부터 루트로 접근함
"""

n = int(input())

for i in range(n):
    str = int(input().split())
    if str[0] == 'S':
        num_s = str[1]
    elif str[0] == 'W':
        num_w = str[1]