# BOJ 10815 숫자카드 
#   1. 입력
#   - N(상근이가 가진 카드 개수. 1<= N <= 5000,000)
#   - 숫자에 적힌 정수 (-10,000,000 <= num < 10,000,000)
#   - M(있는지 확인할 카드 개수)
#   - 확인하려는 정수 (-10,000,000 <= num < 10,000,000)
#   2. 출력
#   - 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 
#   - 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다. 
#   3. 아이디어
#   - sort해서 찾으려는 숫자 혹은 적힌 숫자를 정렬하고 그 다음 이진 탐색을 진행한다.
#   - 중복은 문제에서 고려하지 않아도 된다.
 
import sys
input = sys.stdin.readline 

N = int(input()) 
card_num = list(map(int,input().split())) # list of card numbers
M = int(input()) 
is_number = list(map(int,input().split()))# list of checking numbers

card_num.sort()

def bs(card_num, n):
    start = 0
    end = N-1
    chk = False
    while start <= end:
        mid = (start + end) // 2 
        if card_num[mid] == n: 
                chk = True
                break
        elif card_num[mid] > n:
            end = mid - 1
        else: # card_num[cnt] < n :
            start = mid + 1
    print(1 if chk else 0, end=' ')

for n in is_number:
    bs(card_num, n) 