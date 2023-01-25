# 문제 설명
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    for i in range(1,n+1):
        print(i)
        if i%2 != 0:
            answer.append(i)
    return answer

def solution2(n):
    return [i for i in range(1, n+1, 2)]

def solution3(n):
    return [x for x in range(n+1) if x%2]

solution3(10)