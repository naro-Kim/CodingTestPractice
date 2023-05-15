'''
def solution(k, dungeons):
    answer = 0
    now = k
    while now > 0:
        for need, use in dungeons:
            now -= use
            if now < 0:
                break
            else:
                answer += 1
    
    return answer
'''
# dungeon 피로도를 하나의 튜플로 permutation 돌리고 체크함
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    r = len(dungeons)
    for fatigue in permutations(dungeons,r):
        now = k
        cnt = 0
        for need, use in fatigue:
            if now >= need:
                now -= use
                cnt += 1
        answer = max(answer, cnt)

    return answer