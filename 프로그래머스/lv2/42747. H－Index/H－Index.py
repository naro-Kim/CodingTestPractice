#1. 각 논문들의 인용 횟수를 조사한다
#2. 연구자의 논문을 인용 횟수를 기준으로 내림차순 정렬한다 
#3. 인용횟수와 논문의 순서(Index)가 같거나 인용횟수가 더 높은 구간까지의 논문 편수를 구한다

def solution(citations):
    ans = 0
    c = sorted(citations, key=lambda x:-x)
    for i in range(len(c)):
        if i+1 > c[i]:
            break
        else:
            ans = i+1
    return ans
        