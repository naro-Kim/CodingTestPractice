# BOJ 2075 N번째 수
# 1. 문제 조건
#   - N*N표에 숫자가 주어졌을 때, N번째로 큰 숫자를 찾아 출력한다. 
#   - 입력은 한번에 N개의 숫자가 주어진다. 따라서 heap에 넣기 전에, 저장 형식을 다듬어야 한다.
#   - 메모리 제한이 12MB이므로, 튜플 혹은 2차원 배열을 사용하지 않는다.
# 
# 2. 해결 아이디어
#   - n번째로 큰 숫자는 최소힙의 0번째 인덱스에 남아있는 숫자다.


import heapq as hq # 힙큐를 hq로 쓰기
import sys
input = sys.stdin.readline

n = int(input())
heap = []

init_numbers = list(map(int,input().split())) 
for num in init_numbers:
            hq.heappush(heap,num) #list 객체를 풀어서 원소를 heap에 넣어준다.

for i in range(n-1):  
    numbers = list(map(int,input().split())) 
        # heap의 0번째 원소는 해당 입력까지, 모든 수 들 중 n번째 큰 수
        # 입력 한줄 마다 힙 원소를 뒤바꾼다.
    for num in numbers:
        if heap[0] < num :
            hq.heappush(heap,num)
            hq.heappop(heap)

print(heap[0])