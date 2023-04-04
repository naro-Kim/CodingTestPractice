from collections import Counter

def solution(participant, completion):
    c = Counter(participant)
    for item in completion:
        c[item] -= 1
    return "".join(c.elements())

    
    #d = {key: 0 for key in participant}