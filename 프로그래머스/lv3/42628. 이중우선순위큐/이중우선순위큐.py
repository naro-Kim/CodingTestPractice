import heapq as hq

def solution(op):
        q = []
        for i in op:
            ins, num = i.strip().split() 
            if ins == 'I':
                hq.heappush(q, int(num))
            elif ins == 'D' and q:
                if num == '-1':
                    hq.heappop(q)
                elif num == '1':
                    q.pop()
        return [max(q), min(q)] if q else [0,0]