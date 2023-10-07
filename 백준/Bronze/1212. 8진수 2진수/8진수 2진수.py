import sys
input = sys.stdin.readline
t = int(input(), base=8) 
print(f'{t:b}')

# `base=8`로 8진수 input을 받고, `f'{variable:b}` 형태로 binary 출력