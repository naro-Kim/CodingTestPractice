def solution(n, lost, reserve):
    #n = 학생수, lost = 잃어버린 사람, reserve = 여벌 
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost) 
    for r in _reserve:
        front = r - 1 
        back =  r + 1
        if front in _lost:
            _lost.remove(front)
        elif back in _lost:
            _lost.remove(back)
    return n - len(_lost)