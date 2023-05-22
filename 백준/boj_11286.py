# BOJ 11286 절댓값 힙
# 1. 문제 조건
#   - 배열에 자연수 x를 넣는다.
#   - 입력이 '0'이면 배열에서 절대값이 가장 작은 값을 출력한다. 배열이 비었으면 '0' 출력
#   - 입력이 자연수 'x'이면 배열에 'x'를 추가한다.
#
# 2. 최대힙 개념
#   - root에 가장 큰 수를 갖는 이진 트리
#   - k번 인덱스의 left child는 2*k에 위치하고, right child는 2*k+1에 위치한다.
#   - 임의의 subtree에서 root는 항상 그 subtree 내의 최대값이다
#
# 3. 파이썬의 Heapq module
#   - 파이썬 heapq 모듈에선 최소힙을 기본으로 한다. 
#   - 최소힙의 노드 데이터에 abs()를 사용하면 절댓값 힙 구조가 된다.
#
# 4. 절댓값힙 구현
#   - 1) 파이썬에서 heapq에 (abs(입력값), 입력값)의 튜플 형태로 데이터를 넣는다.  
#   - 2) 노드가 절대값이 작은 입력값을 기준으로 정렬되고, 튜플의 [1]번째 item인 원래 입력값이 노드의 데이터가 된다. 


import heapq as hq # 힙큐를 hq로 쓰기
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
    num = int(input())
    if num != 0 :
        hq.heappush(heap,(abs(num),num))
    else:
        try: 
            print(hq.heappop(heap)[1])
        except:
            print('0')