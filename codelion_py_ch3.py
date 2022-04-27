"""
codelion - Ch3. Python으로 만드는 익명 질문 게시판

게시판을 관리하기 위한 기능 구현
[프로그램의 데이터 저장하기 - Dictionary 만을 사용하기 ]
- 1. 데이터를 딕셔너리로 저장한다. 질문은 Key, 답변은 Value로 저장한다. 

[프로그램의 데이터 저장하기 - List안에 Dictionary 데이터 입력]
- 0. 딕셔너리의 key와 value로 쓸 string을 설정하고 빈 딕셔너리를 초기화한다.
- 1. 앞의 과정과 동일하게, while문을 통해 데이터를 딕셔너리로 저장한다.
- 2. 저장한 딕셔너리를 리스트형로 캐스팅해,  List[0]에는 0번째 사람의 답변을, List[1]에는 1번째 사람의 답변을 저장하는 식으로 저장한다.


"""
#1번 방식
total_dictionary = {}

while True:
    q = input("질문을 입력해주세요. : ") #사용자의 입력값을 변수 q에 저장
    if( q == "q"):
        break
    else:
        total_dictionary[q] = "" # key에 q를 넣고, value는 빈 상태

for i in total_dictionary:
    print(i)
    ans = input("위 질문의 답변을 입력해주세요. : ")
    total_dictionary[i] = ans # dictionary 사이즈만큼 key q에 매칭되는 ans를 저장한다.

print(total_dictionary)


#2번 방식 
total_list = [] #[] 대괄호 주의~

while True:
    q = input("질문을 입력해주세요. : ") #사용자의 입력값을 변수 q에 저장
    if( q == "q"):
        break
    else:
        total_list.append({"Q" : q, "A" : ""}) # tatal_list에 key = question, value = ""인 딕셔너리 형태를 append한다. 

for i in total_list:
    print(i["Q"])
    ans = input("답변을 입력해주세요. : ")
    i["A"] = ans

print(total_list)