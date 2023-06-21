def DFS_ST(d, st): 
    path = []
    while st:
        dep = st[-1]
        if dep not in d or len(d[dep]) == 0:
            path.append(st.pop())
        else:
            st.append(d[dep].pop(0))
    return path[::-1]

def solution(tickets):
    d = {} 
    for dep,arr in tickets:
        d.setdefault(dep, set()).add(arr) 

    for key in d:
        d[key] = sorted(d[key]) 
    
    return DFS_ST(d, st=["ICN"])