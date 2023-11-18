def do_dump(n):
    for _ in range(n):
        if dumps[0] == dumps[-1]:
            continue
        else:
            dumps[0] += 1
            dumps[-1] -= 1
            dumps.sort()


for t in range(1, 11):
    N = int(input())
    dumps = sorted(list(map(int, input().split())))
    do_dump(N)
    res = dumps[-1] - dumps[0]
    print(f'#{t} {res}')