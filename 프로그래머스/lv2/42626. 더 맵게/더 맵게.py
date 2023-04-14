import heapq as hq

# minheap, soville의 두 리프 원소를 상위 스코빌로 만든다.
# minheap에서 heappop으로 뽑은 두 원소의 합을 다시 heappush

def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)
    while 1:
        try:
            f = hq.heappop(scoville)
            if f >= K:
                break
            s = hq.heappop(scoville)
            hq.heappush(scoville, f + s*2)
            cnt += 1 
        except:
            return -1
    return cnt