from tkinter import *
from tkinter import messagebox
import random
#변수 초기화 
win = 0
tie = 0
lose = 0


#컴퓨터는 랜덤으로 가위, 바위, 보 중에 고름
def computer():
    choices = ['가위', '바위', '보']
    choice_computer = random.choice(choices)
    return choice_computer


#결과 판단용용
def game(choice_me):
    global win
    global tie
    global lose

    choice_computer = computer()

    if choice_me == choice_computer:
        result = "무승부!"
        tie += 1
    elif (choice_me == '가위' and choice_computer == '보') or (choice_me == '바위' and choice_computer == '가위') or (choice_me == '보' and choice_computer == '바위'):
        result = "승리!"
        win += 1
    else:
        result = "패배!"
        lose+=1
    #변경해주는 configure 사용
    label_choice.configure(text = f"컴퓨터 : {choice_computer} vs 나 : {choice_me}")
    label_match.configure(text = f"{result}")
    label_result.configure(text = f"승리 : {win} / 패배 : {lose} / 무승부 : {tie}")



#버튼 누르면 내 선택 저장
def select_scissors():
    game('가위')

def select_rock():
    game('바위')

def select_paper():
    game('보')

#메시지 박스를 이용해서 게임이 끝났을 때 게임 실행 정보를 표시
def quit_game():
    count = win + tie + lose
    winning_rate = win/count*100
    messagebox.showinfo("게임 종료",f"\n게임 수 :\t {count} \n승리 :\t {win} \n패배 :\t {lose}  \n무승부 :\t {tie} \n승률 : \t {winning_rate:.2f}%")
    root.quit()


#tkinter 사용해서 gui 만들기
root = Tk()
root.geometry("400x300")
root.title("가위바위보 게임")

label_welcome = Label(root, text = "<두근두근 가위바위보 게임>", font = "Helvetica 20")
label_welcome.pack()

#프레임으로 버튼 3개 묶어주기기
frame = Frame(root)
frame.pack(pady=20) 

#가위바위보 버튼
button_s = Button(frame, text = "가위",width = 10, height = 2, bg="red", command=select_scissors)
button_s.pack(side=LEFT, padx = 5)

button_r = Button(frame, text = "바위",width = 10, height = 2,bg="yellow", command=select_rock)
button_r.pack(side=LEFT, padx = 5)


button_p = Button(frame, text = "보",width = 10, height = 2, bg="blue",command=select_paper)
button_p.pack(side=LEFT, padx = 5)


#경과를 업데이트해가며 보여주는 label 
label_choice = Label(root, text="컴퓨터 vs 나", font="Helvetica 16", pady=20)
label_choice.pack()

label_match = Label(root, text = "결과는?", font="Helvetica 14", pady=10)
label_match.pack()

label_result = Label(root, text="승리: 0 / 패배: 0 / 무승부: 0", font="Helvetica 14", pady=10)
label_result.pack()

#종료 버튼
quit_button = Button(root, text="종료", width=5, height=1, bg="gray", command=quit_game)
quit_button.place(x=330, y=260)


root.mainloop()