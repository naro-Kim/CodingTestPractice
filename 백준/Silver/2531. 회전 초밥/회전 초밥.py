import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

left, right, ans = 0, 0, 0
sushi_dict = defaultdict(int)
sushi_dict[c] += 1

while right < k:
    sushi_dict[sushi[right]] += 1
    right += 1

while left < N:
    # 한바퀴 돌아야 하므로 <N
    ans = max(ans, len(sushi_dict))
    sushi_dict[sushi[left]] -= 1 # 왼쪽 슬라이드를 오른쪽으로 한 칸 옮기기
    if sushi_dict[sushi[left]] == 0:
        del sushi_dict[sushi[left]]
    sushi_dict[sushi[right%N]] += 1 # 오른쪽으로 옮기고 ++
    left += 1
    right += 1

print(ans)