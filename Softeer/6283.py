import sys
input = sys.stdin.readline

def is_ascending(arr):
    return arr == [1,2,3,4,5,6,7,8]

def is_descending(arr):
    return arr == [8,7,6,5,4,3,2,1]

nums = list(map(int, input().split()))
if is_ascending(nums):
    print("ascending")
elif is_descending(nums):
    print("descending")
else:
    print("mixed")