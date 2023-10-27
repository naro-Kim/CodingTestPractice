import sys
input = sys.stdin.readline

rest = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
ans = 0
for charge in rest: 
    if n <= 0:
        break
    ans += n // charge 
    n %= charge

print(ans)