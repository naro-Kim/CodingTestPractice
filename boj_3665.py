# BOJ 3665 최종순위
#   1. 입력
#   -   n개의 팀은 key가 등수이고 value가 팀 번호이다.
#   - 
#   2. 출력
#   -   지난 순위 대비 쌍을 토대로 바뀐 올해 순위를 1등팀 부터 순서대로 출력한다
#   -   입력으로 주어진 정보가 올해 최종순위를 만들 수 없는 경우와 일관성없는 잘못된 정보의 경우, 'IMPOSSIBLE'을 출력한다.
#   3. 아이디어
#   -   순서가 바뀐 쌍에 대해, 더 낮은 인덱스의 팀의 탐색 포인터를 mid를 기준으로 바꿔준다
#   -   주어진 쌍에 대해 인덱스를 각각 확인하고 두 팀의 순위를 확인한 후에
from collections import deque
import sys
input = sys.stdin.readline 


# return sorted lank
def solve(n,lank):
    if lank == False:
        return
    left = deque()
    right = deque()
    n_lank =  deque()
    m = int(input()) # 상대 등수가 바뀐 쌍의 수 
    for _ in range(m):
        a, b = map(int, input().split()) # 상대 등수가 바뀐 쌍
        try: 
            idx = lank.index(b) 
        except:
            lank = False # index error 발생시 IMPOSSIBLE 출력
            break
        if lank == False:
            break
        if idx != 0:
            for _ in range(idx):
                left.append(lank.popleft())
            for _ in range(idx+1, n):
                right.append(lank.pop())   
        try: 
            right.remove(a)
            n_lank.appendleft(a)
        except:
            return False
    lank = left+n_lank+lank+right
    print(*lank)
        
        

t = int(input()) # number of test cases
for _ in range(t):
    n = int(input()) # number of teams
    lank = deque(map(int, input().split())) # team lank of the last year
    if n == 0:
        continue # 0이 입력된 경우, 테케를 입력받지 않고 다음 테케로 진행합니다.
    if solve(n,lank) == False:
        print("IMPOSSIBLE")
        continue