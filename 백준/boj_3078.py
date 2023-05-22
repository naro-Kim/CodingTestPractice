# BOJ 3078 좋은친구
# 1. 문제조건
#   - 좋은 친구의 조건은 아래와 같다.
#   - 1) 등수 차이가 K를 넘지 않는다
#   - 2) 이름의 길이가 자신과 같아야 한다. 
#
# 2. 아이디어
#   - 좋은 친구의 탐색범위는 자기 자신으로 부터 +K까지이다.
#   - 어차피 필요한건 이름 길이고 친구의 이름이 아니니까 input도 len() method로 저장해, 나중에 len() 연산을 하지 않는다. (그럼 그냥 길이 대조만 하면 되니까 -1 연산도 줄여도 되지않나?)
#   - 배열의 j는 i번째 학생의 다음 성적순 학생이다. 
#       -> 반복문에서 j는 i+1부터 시작해 i+K까지 진행하고, i는 i+K가 학생수보다 작을 때 까지만 증가한다.

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
list = [len(input()) for i in range(N)]
cnt = 0 

for i in range(N):
    for j in range(i+1, min(i+K+1,N)): #이때 index가 넘어가면 안됨
        if list[i] == list[j]:
            cnt +=1  
print(cnt)