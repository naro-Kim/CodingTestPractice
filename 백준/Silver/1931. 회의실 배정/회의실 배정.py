import sys
input = sys.stdin.readline

n = int(input())
t = [tuple(map(int,input().split(' '))) for i in range(n)] 
t.sort(key = lambda x:x[0])
t.sort(key = lambda x:x[1])
cnt = 1

end = t[0][1]
for time in t[1:]:
    if time[0] >= end:
        cnt += 1
        end = time[1]

print(cnt) 