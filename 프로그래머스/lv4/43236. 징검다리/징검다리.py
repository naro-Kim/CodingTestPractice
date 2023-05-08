# 거리의 최소값 = min(items) 이지만 효율을 위해 0
# _high = distance
# rock이 50000개 이하니까 sort해도 괜찮나,,?

def solution(distance, rocks, n):
    rocks.sort(key = lambda x:x)
    low = 0
    high = distance # 모든 바위가 없는 경우
    ans = []
    
    # mid값이 최소값 중 가장 큰 값이 될 것이라 가정
    # 탐색에서 제외할 것은 mid보다 작은 돌들.. 작은 돌들의 개수가 num을 넘겼다면 mid 조정
    
    # 바위사이 거리
    ans.append(rocks[0])
    for i in range(len(rocks)):
        try:
            ans.append(rocks[i+1]-rocks[i])
        except:
            pass
    ans.append(distance-rocks[-1]) 
    #최소값 출력하기 
    while high - low > 1:
        mid = (low+high)//2 
        dis = 0 # 바위 제거 후 거리 계산값
        r = 0 # 뺀 바위 수
        for a in ans:
            #print(a, r, dis, low, mid, high)
            dis += a # 바위 뺌
            if dis < mid: #첫 바위부터 중간값 넘겨버림 -> 탐색 위치 조정
                r += 1
            else:
                dis = 0
        if r > n:
            high = mid
        else:
            low = mid
    return low

        
