"""
220507
정신차리고 알고리즘과 자료구조 파이썬으로 공부 시작
"""
# def sol(L, x):
#     ans = []
#     for i in range(len(L)):
#         if L[i] == x:
#             ans.append(i) 
#     if(len(ans) == 0) : ans.append(-1)
#     return ans

def binary_search(L, x): 
    lower = 0
    upper = len(L) -1 
    while lower <= upper:
        mid = (lower+upper)//2 #//연산자는 정수형 나눗셈
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            lower = mid + 1 #binary search 진행 시 인덱스를 +1 , -1로 재설정하는 것 잊지 않기!
        elif L[mid] > x:
            upper = mid - 1 
    return -1
            
def sum_numbers(n):
    if(n <= 1) : return n 
    return n*(n+1)//2

def fibo_sum(n):
    if n <= 1 : return n
    return fibo_sum(n-1) + fibo_sum(n-2)

def fibo_dp(n): 
    memo = [0,1]
    if n<2 : 
        return n
    else:
        for i in range(2,n+1): 
            memo.append(memo[i-1]+memo[i-2]) 
    return memo[n]

n = int(input())
#n = map(int, input().split()) 
#a, b = map(int, input().strip().split(' ')) 
print(fibo_sum(n), " ", fibo_dp(n))