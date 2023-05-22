import sys
input = sys.stdin.readline

n = int(input()) # 시험장 개수 
a = list(map(int,input().split()))
b, c = map(int, input().split())
cnt = 0

for i in range(n):
  t = (int(a[i])) - b 
  cnt += 1
  if t > c:
    if t % c:
      cnt += (t // c) + 1
    else:
      cnt += (t // c)
  elif t < c and t > 0:
    cnt += 1
    
print(cnt)