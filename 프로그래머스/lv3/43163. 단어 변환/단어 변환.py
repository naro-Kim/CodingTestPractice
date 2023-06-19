from collections import deque
 
def count_matches(str1, str2):
    count = len(str1)
    for char1, char2 in zip(str1, str2):
        if char1 == char2:
            count -= 1
    return True if count == 1 else False

def solution(begin, target, words): 
    degree = 0
    q = deque()  
    q.append([begin, []])
    
    while q:
        cur, visited = q.popleft()
        if cur == target:
            return len(visited)
        for word in words: 
            if count_matches(cur, word) and word not in visited:
                tmp = visited[0:]
                tmp.append(word)
                q.append([word, tmp])
    return 0