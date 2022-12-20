from tkinter import *
from tkinter import messagebox
from math import *

window = Tk() # window 에 Tk() 셋
window.title('윈도우창 이름') # 윈도우 창 이름
window.geometry("300x500") # 크기 가로 x 세로
window.resizable(width = False, height = False) #리사이즈 금지

label1 = Label(window, text = '라벨1') # label1 변수에 Label() 셋, window 변수에 텍스트 표현
label2 = Label(window, text = '라벨2', font = ('궁서체', 30), fg = 'blue') # 궁서체 폰트 30크기, 글자 색깔 파랑
label3 = Label(window, text = '라벨3', bg = 'magenta', width = 20, height = 5, anchor = SE) # 백그라운드 마젠타, anchor 사우스이스트

label1.pack() # 라벨 표현
label2.pack()
label3.pack()

def clickButton():
    messagebox.showinfo('메세지 박스 제목', '메세지 박스 내용') # 함수 호출 시 메세지 박스 보여주기(제목,내용)

button1 = Button(window,text = '눌러주세요', fg = 'red', bg = 'yellow', command = clickButton) # 버튼1 변수에 버튼 생성, 커맨드(클릭 시) = clickButton 함수 호출
button1.pack(expand = 1) # 버튼 1 채워넣기(확장두께 = 1)

def calc(event):
    label.config(text = '결과=' + str(eval(entry.get())))

entry = Entry(window)
entry.bind("<return>", calc)
entry.pack()

label = Label(window)
label.pack()

window.mainloop()