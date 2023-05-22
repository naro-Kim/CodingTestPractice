# BOJ 11279 최소힙
# 1. 문제 조건
#   - 배열에 자연수 x를 넣는다.
#   - 입력이 '0'이면 배열에서 가장 작은 값을 출력한다. 배열이 비었으면 '0' 출력
#   - 입력이 자연수 'x'이면 배열에 'x'를 추가한다.
#
# 2. 최대힙 개념
#   - root에 가장 작은 수를 갖는 이진 트리
#   - k번 인덱스의 left child는 2*k에 위치하고, right child는 2*k+1에 위치한다.
#   - 임의의 subtree에서 root는 항상 그 subtree 내의 최소값이다
#
# 3. 파이썬의 Heapq module
#   -
#   -

import heapq
import sys
input = sys.stdin.readline 

heap = []
n = int(input())

for i in range(n):
    num = int(input())
    if num > 0 :
        heap.heappush(heap,num)
    else:
        try: 
            print(heap.heappop(heap))
        except:
            print('0') # heappop은 배열이 비어있으면 Outofrange error를 띄우는데, except를 통해 print문이 작동하게 만들 수 있다.