#자판기 만들기

#전역변수
money = 0
sales = 0

#메뉴 리스트를 출력해주는 함수
def menu_list():
    print("♥♡ ♥♡ ♥♡ ♥♡<<메뉴>>♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ")
    print("1. 콜라 300원")
    print("2. 우유 400원")
    print("3. 환타 500원")
    print("4. 주스 600원")
    print("5. 맥주 800원")

#현재 금액을 알려주는 함수
def print_current_money():
    global money
    print(f"현재 금액은 {money}원 입니다. \n")

#금액을 입력하는 함수
def input_money():
    global money
    while(True):
        entered__money = int(input("500, 1000, 5000, 10000, 50000 만 입력가능\n금액을 입력하시오: "))
        if entered__money in [500, 1000, 5000, 10000, 50000]:
            money += entered__money
            print_current_money()
            break
        else:
            print("존재하지 않는 화폐 단위입니다. \n")

#메뉴를 입력하는 함수
def input_menu():
    while(True):
        global money
        menu = int(input("메뉴의 번호를 입력하십시오: "))
        if(menu>0 and menu<=5):
            menu_func(menu)
            break
        else:
            print("존재하지 않는 음료입니다.\n")

#돈이 충분히 있는지 체크하는 함수
def money_check(price):
    global money
    while(True):
        if money<price:
            print("돈이 부족합니다.\n")
            print("♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡")
            str = input("돈을 더 지불하시겠습니까? Yes or No를 입력하십시오: ")
            if(str == "Yes"):
                input_money()
                if money>=price:
                    break
            elif(str == "No"):
                print("주문이 취소되었습니다. \n")
                return False
        else:
            break
    return True
#주문한 메뉴를 알려주고 금액을 차감해주는 함수
def menu_func(num):
    global money
    global sales
    if num == 1:
        print("콜라를 주문하셨습니다. \n")
        if not money_check(300):
            return
        money-=300 
        sales+=300
        print_current_money()
    elif num == 2:
        print("우유를 주문하셨습니다. \n")
        if not money_check(400):
            return
        money-=400
        sales+=400
        print_current_money()
    elif num == 3:
        print("환타를 주문하셨습니다. \n")
        if not money_check(500):
            return
        money-=500
        sales+=500
        print_current_money()
    elif num == 4:
        print("주스를 주문하셨습니다. \n")
        if not money_check(600):
            return
        money-=600
        sales+=600
        print_current_money()
    elif num == 5:
        print("맥주를 주문하셨습니다. \n")
        if not money_check(800):
            return
        money-=800
        sales+=800
        print_current_money()

#잔돈 발생시 거스름돈을 받을지 음료를 더 뽑을지 질문
def cash():
    print(f"거스름돈은 {money}원 입니다.\n")

def selection():
    print("♡ ♥♡ ♥ <<두근두근 자판기>> ♥♡ ♥♡")
    print("1. 메뉴")
    print("2. 돈 투입하기")
    print("3. 음료 선택")
    print("4. 남은 금액")
    print("5. 거스름돈")
    print("6. 종료")
    print("♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡")
    while(True):
        num = int(input("번호를 선택하십시오: "))
        if (num == 1):
            menu_list()
        elif(num == 2):
            input_money()
        elif(num == 3):
            input_menu()
        elif(num == 4):
            print_current_money()
        elif(num == 5):
            cash()
            break
        elif(num == 6):
            break
        print("♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡")

selection()
print(f"총 판매액은 {sales} 입니다.\n")
print("두근두근 자판기를 \n사랑해주셔서 감사합니다.\nଘ(੭˃ᴗ˂)━☆ﾟ.*･｡ﾟ")
print("♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡ ♥♡")
