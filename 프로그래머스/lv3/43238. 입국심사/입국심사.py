# 무엇이 최소가 되는 케이스고 최대가 되는 케이스일까?
# 각각 심사대 값 sum(times)
# 한곳에 다 뭉치면 최소값이 될 수 없음. 두 심사대 모두 들어갔을 때 최소라고 하자
# 반복문 안에서, 횟수가 n이 될 때까지 심사를 진행
# 심사대에 서는 사람의 수 
# 첫번째 순환 
def solution(n, times):
    _low = 1 # 첫 두 사람이 들어간 최소값
    _high = max(times) * n # 무지성 최대값

    while _low <= _high:
        mid = (_low + _high)//2
        ppl = 0 
        for t in times:
            ppl += mid // t 
        if ppl < n :
            _low = mid + 1
        else : 
            _high = mid -1
    return _low