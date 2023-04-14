def solution(s):
    ans = 0
    # ")"로 시작하는 문자열을 사전 차단
    if s[0] == ")":
        return False
    
    for c in s:
        if c == "(":
            ans += 1
        elif c == ")":
            ans -= 1 
        if ans < 0 :
            return False    
    return True if ans == 0 else False