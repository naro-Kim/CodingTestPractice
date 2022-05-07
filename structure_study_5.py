def binary_search(L, x, lower, upper):
    if x < L[lower] or x > L[upper]:
        return -1 
    mid = (lower+upper)//2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binary_search(L, x, lower, mid-1)
    elif x > L[mid]:
        return binary_search(L, x, mid+1, upper)

"""
#학습용 하노이 알고리즘

def draw_hanoi():
    print(col1)
    print(col2)
    print(col3)
    print("\n")

#n은 옮김 원판의 갯수, start는 첫 번째 기둥 sub는 두번째 기둥,  dest는 마지막 기둥이다.
def hanoi(n, start, sub, dest): 
    if(n==1):
        dest.append(start.pop())
        print("From : " , start , " To : " , dest)
        draw_hanoi()
    else:
        hanoi(n-1, start, dest, sub)
        dest.append(start.pop())
        print("From : " , start , " To : " , dest)
        draw_hanoi()
        hanoi(n-1, sub, start, dest)

n = int(input())
col1 = list(range(n,0,-1))
col2 = []
col3 = []
hanoi(n,col1,col2,col3)
"""