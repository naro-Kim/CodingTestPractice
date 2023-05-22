from collections import deque
dq = deque()

def solution(progresses, speeds):
    answer = []
    days = deque()
    tmp = 1
    for i in range(len(progresses)):
        days.append((100 - progresses[i])//speeds[i]+1)
    print('----day : ',days)
    # for i in range(len(days)):
    #     cur = days.popleft()
    #     if cur > tmp:
    #         answer[i] += 1
    #         tmp = cur
    #     else:
    #         answer.append(1)
    
    return answer

        

# i번째 작업보다 i+1번째 작업의 개발시간이 크다면 선행한 작업을 바로 배포한다.
# 만약 i+1번째 작업의 개발시간이 적다면 선행 배포시 함께 배포한다.
# 테케 추가 [90, 90, 90, 90],[30, 1, 1, 1],[1, 3]
# 테케#2 추가 [95, 95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1, 1] [1, 2, 2, 2]