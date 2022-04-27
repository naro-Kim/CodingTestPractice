"""
codelion python 제 6강 ~ 제 7강 - Dictionary, List

{'고향':'수원', '취미' : '영화보기', '좋아하는 음식' : '국수'}
Key와 value를 통해 데이터를 나열하는 자료형

- information 객체의 key를 통해 value를 출력하는데엔 두가지 방법이 있다.
- 1. key를 인덱스로 오브젝트의 key에 매칭되는 value를 출력한다. (단, 이때 인덱스에 정수 지정은 불가능)
- 2. get attribute를 통해 key에 매칭되는 value를 출력한다.

"""
information = {'고향':'수원', '취미' : '영화보기', '좋아하는 음식' : '국수'}
foods = ["된장찌개", "피자", "제육볶음"]

print("나의 고향은 " + information['고향'])
print("나의 취미는 " + information.get("취미"))
print(len(information))

print("==========")
# dinctionary에 정보를 추가하기
# dictname["new_key"] = "new_data" 의 형식으로 기존 딕셔너리에 정보를 추가할 수 있다.

information["특기"] = "고양이랑 놀기"
information["사는 곳"] = "망원"
print(len(information)) # len() function으로 dictionary object의 길이를 확인할 수 있다.

print("==========")
del information["좋아하는 음식"] #del 키워드를 통해 dictionary object의 값을 삭제할 수 있다.
print(information)
print(len(information))

print("==========")
information.clear()
print(information)
print(len(information))

print("==========")
print("list[1] 출력 : " + foods[1]) # List는 인덱스를 통해 value를 출력할 수 있다.
print("list[-1] 출력 : " + foods[-1]) # List는 인덱스를 통해 value를 출력할 수 있다.
print(len(foods))

print("==========")
# List에 정보를 추가하기
# List는 dictionary와 다르게, append() function을 이용해 추가한다.
# foods[4] = "감자" syntax error 불가능
foods.append("물고구마")
print("append() 실행 후 list[-1] 출력 : " + foods[-1]) 
print(len(foods))

print("==========")
del foods[-1]
print("del 키워드 실행 후 list[-1] 출력 : " + foods[-1]) 
print(len(foods))