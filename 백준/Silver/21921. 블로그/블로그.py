import sys
input = sys.stdin.readline

# sliding window
n, x = map(int, input().split())
visits = list(map(int, input().split()))
if max(visits) == 0:
    print('SAD')
else:
    value = sum(visits[:x]) # x칸까지 미리 세고 저장
    max_value = value
    cnt = 1

    # 한칸씩 이동하면서 체크
    for i in range(x, n): 
        value -= visits[i-x] # 윈도우의 왼편은 비우고
        value += visits[i] # 윈도우의 오른편은 더한다
        if value == max_value : cnt += 1 # 최대 방문자수 갱신않고 구간 갯수 증가
        elif value > max_value :
            max_value = value # 최대 방문자수 갱신
            cnt = 1 # 구간 갯수 초기화

    print(max_value)
    print(cnt)