# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

array = [1,1,2,2]

def solution(array):
    while array:
        for key,val in enumerate(set(array)):
            print(key, ':', val)
            array.remove(val)
        if key == 0:
            return val
    return -1

def solution2(array):
    frq = {}
    cnt = 0 
    for i in array:
        frq[i] = frq.get(i, 0) + 1 # counting value 빈도
    max_num = max(frq, key=frq.get) 
    for j in frq:
        if frq[j] == frq.get(max_num):
            cnt += 1
    if cnt > 1:
        return -1
    else:
        return max_num


solution(array)
