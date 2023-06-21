def solution(tickets):
    tickets.sort(reverse=True) # 정렬
    path = {}

    for dep, arr in tickets:
        if dep in path:
            path[dep].append(arr)
        else:
            path[dep] = [arr]
    
    st = ['ICN']
    ans = []
    
    while st:
        dep = st[-1]

        if dep not in path or len(path[dep])==0:
            ans.append(st.pop())
        else: 
            st.append(path[dep].pop())

    return ans[::-1]