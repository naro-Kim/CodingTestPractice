'''
title: 수퍼바이러스
풀이 : 
# f(2,10)은 f(2, 5) * f(2,5)로 나눌 수 있다. 
# n이 비대하게 큰 수이므로, f(2,5) * f(2,5)를 `1000000007` 로 모듈러 연산을 한다.
# 이 때, n이 홀수일 수 도 있으므로 홀수인 경우에 p^n 연산을 위해서 f(p, n-1)을 진행한 뒤에 p를 한 번 더 곱해준 값을 리턴하는 방식으로 돌린다.
'''
m = 1000000007

def virus(p, n):
  # break condition
  if n==1:
    return p
  elif n%2 == 0:
    tmp = virus(p, n / 2)
    return tmp * tmp % m # 큰 지수를 나눴다가 합쳐 줌
  else:
    tmp = virus(p, (n-1)/2)
    return tmp * tmp * p % m