import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
for _ in range(k):
    start, end = map(int, input().split())
    avg = sum(s[start-1:end]) / (end - start + 1)
    print(f"{avg:.2f}")