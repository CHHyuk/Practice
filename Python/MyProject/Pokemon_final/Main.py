import User
import Pokemon


class Map():
    
    def operate(self,A):
        print(A.User_inven())
        print('처음 시작하셨군요. 이동하여 원하는 마을로 가주세요 wasd를 이용해 이동할 수 있습니다.')
        for i in User.gamemap:
            print(i)
        print('현재 위치 좌표는','[',A.x + 1 ,',', A.y + 1,']','입니다')
        while True:
            A.move(input())
            if User.gamemap[A.y][A.x] == 'C':
                Town(A, '초원')
                False
            elif User.gamemap[A.y][A.x] == 'S':
                Town(A, '사막')
                False
            elif User.gamemap[A.y][A.x] == 'M':
                Town(A, '물')
                False
    
    def town(self, A, Town):
        print('1')
        
class Town():
    
    def __init__(self,A,Town):
        self.name = Town + '마을'
        print(self.name, '에 오신 것을 환영합니다.')
        flag = True
        while flag:
            print('1.퀘스트 2.상점 3.회복 4.나가기')
            

def start():
    A = User.User(3,3)
    print('포켓몬스터 게임을 시작합니다')
    A.name = input('트레이너의 이름을 입력해주세요 > ')
    my_choice = input('첫 몬스터를 선택해주세요. 1.피카츄 > ')
    if my_choice == '1' or my_choice == '피카츄':
        M = Pokemon.Pokemon(0)
        A.monlist_name.append(M.name)
        A.monlist.append(M)
    START = Map()
    START.operate(A)

start()




