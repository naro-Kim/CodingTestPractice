"""
codelion python 제 12강 ~ 15강 - 오늘은 뭐먹지?

프로그램 개요 : 점심을 먹기위한 메뉴를 선정하고, 사용자가 입력하도록 한다
- 1.  while문을 통해, input에 입력받은 string을 'lunch' List에 추가한다.
- 이때, List에 추가하는 방식은 두 가지가 있는데, 하나는 변수 선언을 통해 데이터를 추가하는 방법과 다른 하나는 
인풋을 바로 넣는 방법이다. 단, 인풋을 바로 넣는 방식을 사용할 경우 인풋을 조건으로 분기(종료나 함수 실행 등등..)할 수 없다.

- 2. 메뉴 제외하기 : 집합과 집합 사이의 차집합 연산을 통해 List형태의 item을 set_lunch 집합에서 제외할 수 있다.

"""
import random
import time
menu = []
set_menu = set(menu)

def func1():
    print("입력을 멈추려면, Q를 입력하세요. ")
    while True:
        item = input("무엇을 먹어볼까요? : ")
        if(item == "q" or "Q"):
            break
        else:
            menu.append(item)
    set_menu = set(menu)
    return

def func2():
    print("삭제를 멈추려면, Q를 입력하세요. \n")
    while True:
        print("현재 메뉴 리스트 : ",set_menu, "\n")
        item = input("어떤 메뉴를 삭제할까요? : ")
        if not set_menu:
            print("메뉴가 없습니다!")
            break
        elif(item == "q" or "Q"):
            break
        else:
            set_menu = set_menu-set(item)
    return

def func3():
    print("메뉴 선택 멈추려면, Q를 입력하세요.\n 계속하려면 아무거나 입력하세요. ")
    print("현재 메뉴 리스트 : ", set_menu, "\n")
    if(input == "Q" or "q"):
        return 
    else:
        for i in range(5):
            print(i + "...")
            time.sleep(1)
    print(random.choice(list(set_menu)))    
    


while True:
    print("\/\/\/\/\/\/\/오늘의 메뉴는 뭘까요~?\/\/\/\n")
    print(">> 메뉴를 추가하려면 \"1\"을 입력하세요.")
    print(">> 메뉴를 삭제하려면 \"2\"를 입력하세요.")
    print(">> 메뉴를 뽑으려면 \"3\"을 입력하세요.")
    print(">> 프로그램을 종료하려면 \"Q\"를 입력하세요.\n")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")

    enter = input()
    if(enter == "1"):
        func1()
    elif(enter == "2"):
        func2()
    elif(enter == "3"):
        func3()
    elif(enter == "Q" or "q"):
        break