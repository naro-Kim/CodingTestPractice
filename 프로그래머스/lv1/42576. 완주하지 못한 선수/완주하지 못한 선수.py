from collections import Counter

def solution(participant, completion):
    c = Counter(participant)
    for item in completion:
        c[item] -= 1
    return c.most_common(n=1)[0][0]

    
    #d = {key: 0 for key in participant}