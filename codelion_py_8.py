"""
codelion python 제 8강 - 반복문

파이썬의 반복문은 for "index" in "iteration 대상"의 형태로 작성한다.
- 1. 기본 반복 문법은 아래와 같은 형태로, 'n'이라는 정수횟수 - 1만큼, ;에 이어져 나오는 구문을 반복한다. 
    for i in range(n):
        print(i)

- 2. List의 모든 데이터 출력
    for i in List:
        print(i)
# for i in range(len(list)): 형태도 가능하지만 효율적으로 출력하자

- 3. Dictionary의 모든 데이터 출력
    for key, value in dictionary.items():
        print(key)
        print(value)
#이때, value에 대한 iterator를 설정하지 않고 print(key)로 출력할 경우에도 딕셔너리의 key와 매칭되는 value가 함께 튜플 오브젝트로 출력된다.

9강, Set

List를 이용하여 집합(Set)을 만들 수 있다.
- 집합 자료형은, 중복 데이터를 허용하지 않는다. 
- 두 set을 다루는 연산은 합집합, 차집합, 교집합이 있다.
- 또한, set은 요소의 순서를 보장하지 않는다. 

"""
#반복문 문법 - 기본
for i in range(30):
    print(i)

#리스트의 모든 데이터 출력
foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
for i in foods:
    print(i)

#dictionary 데이터 출력
information = {'고향':'수원', '취미' : '영화보기', '좋아하는 음식' : '국수'}
for i in information.items():
    print(i)

print("========== 9강 ==========")
foods_set1 = set(foods) #중복 제거
foods_set2 = set(["된장찌개", "피자", "제육볶음", "된장찌개"]) 

# 선언 방식은 달랐지만 같은 결과가 출력됨
print(foods_set1)
print(foods_set2)

print("========== 10강 ==========")
menu1 = set(["된장찌개", "제육볶음", "돌솥밥", "김치찌개"])
menu2 = set(["된장찌개", "돈까스정식", "낚지덮밥", "날치알비빔밥"])
menu3 = menu1 | menu2 #합집합 연산. shift + \ 인 '|' 기호 사용
menu4 = menu1 & menu2 #교집합 연산.
menu5 = menu1 - menu2 #차집합 연산.
print(menu1)
print(menu2)
print(menu3)
print(menu4)
print(menu5)