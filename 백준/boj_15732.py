# BOJ 15732 도토리 숨기기
#   1. 입력
#   - N (채워넣을 상자의 개수. 1<= N <= 1,000,000)
#   - K (규칙의 개수, 1 ≤ K ≤ 10,000)
#   - D (도토리의 개수, 모든 규칙으로 넣을 수 있는 도토리의 총합 1 ≤ D ≤ 1,000,000,000)
#   - A, B, C (K번 반복, A~B상자까지 C간격으로 도토리 넣기 1 ≤ C ≤ A ≤ B ≤ N)
#   2. 출력
#   - 마지막 도토리가 들어가 있는 상자의 번호를 출력
#   3. 헷갈리는 점
#   - 딕셔너리? 링크드 리스트로 도토리를 넣는다 ? 
#   - '상자 하나에 들어갈 수 있는 도토리의 개수는 제한이 없으며'는 중복 제한 없음?
 
import sys
input = sys.stdin.readline 

N,K,D = map(int, input().split())  # 상자 개수, 규칙의 개수, 도토리 개수

# def bs(card_num, n):
#     start = 0
#     end = N-1
#     chk = False
#     while start <= end:
#         mid = (start + end) // 2 
#         if card_num[mid] == n: 
#                 chk = True
#                 break
#         elif card_num[mid] > n:
#             end = mid - 1
#         else: # card_num[cnt] < n :
#             start = mid + 1
#     print(1 if chk else 0, end=' ')

for i in range(N): # number of boxes
    for k in range(K): # number of rules
        dotori = [False for _ in range(N)] #init dotori boxes
        A, B, C = (map(int,input().split())) # A = start, B = end, C = spacing
        for d in range(D):
            cur = A
            if dotori[cur] == True:
                continue
            else:
                dotori[cur] = True
            cur += C
        print(dotori)