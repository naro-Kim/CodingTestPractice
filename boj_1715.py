import heapq as hq
import sys
input = sys.stdin.readline

cards = []
sum = 0
n = int(input())

for i in range(n):
    hq.heappush(cards, int(input()))

while len(cards) > 1 :
    u = hq.heappop(cards)
    v = hq.heappop(cards)
    sum += u + v
    hq.heappush(cards, u+v)

print(sum)