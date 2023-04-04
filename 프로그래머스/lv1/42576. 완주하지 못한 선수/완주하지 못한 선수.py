from collections import Counter

def solution(participant, completion):
    return "".join([(Counter(participant) - Counter(completion)).keys()][0])
    
    #c = Counter(participant) - Counter(completion) 
    #return "".join(c.elements() 

    # return "".join(c.most_common()[0][0]) 
    #d = {key: 0 for key in participant}