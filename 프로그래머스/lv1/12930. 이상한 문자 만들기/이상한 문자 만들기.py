def solution(s):
    ans = ''
    # 공백이 두개인 경우에 주의
    for word in s.split(" "):
        for idx, t in enumerate(word):
            if idx % 2 == 0:
                # 짝수 자리에 소문자가 오는 경우, 대문자로 출력해야 한다.
                ans += t.upper()
            else:
                # 홀수 자리에 대문자가 오는 경우, 소문자로 출력해야 한다.
                ans += t.lower()
        ans += ' '

    return ans[:-1]