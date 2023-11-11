T = int(input())

for t in range(1, T + 1):
    N = int(input())

    pascal =[[0]*N for _ in range(N)] 
    pascal[0][0] = 1 # base case

    for i in range(1,N): 
        for j in range(N): 
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j] #dp

    print(f"#{t}")
    for row in pascal: 
        for col in row:
            if col :
                print(col, end=' ')
        print()