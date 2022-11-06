from re import S
import random

class Unit(): # 모든 유닛들은 고유한 이름과 능력치를 가짐
    
    def __init__(self):
        self.number = 0
        self.name = ''
        self.lv = 1
        self.hp = 0
        self.exp = 0
        self.dmg = 0
        self.skill_name = ''

class User():
    self.monlist[i].hp -= damage
    def __init__(self):
        self.name = ''
        self.monlist = [] # 각 자리마다 한마리씩 들어감, 최대 6마리 가지고다님, 0 = 아무것도 없는 상태
        self.monlist_num = [] # 번호로 인식가능하게
        self.itemlist = {'작은 포션':0,'큰 포션':0,'기타 아이템':0} # 인벤토리 작은포션 10 회복 / 큰포션 30 회복 / 기타아이템 상점판매시 10원
        self.money = 0

    def status(self):
        print('유저의 이름 : ',self.name)
        print('현재 보유중인 몬스터 : ',self.monlist)
        print('현재 보유중인 아이템 : ',self.itemlist)
        print('현재 보유중인 돈 : ',self.money)

class wildenemy():

    def __init__(self,i):
        E_Mon = Data.Dataextract(i)
        self.name = E_Mon[1]
        self.hp = int(E_Mon[2])
        self.dmg = int(E_Mon[3])
        self.skill_name = E_Mon[4]

    def attack(self, enemy_hp):
        return enemy_hp - self.dmg

class Data():
    
    def Dataextract(i):
        filepath = 'C:/git/Practice/Python/MyProject/Pokemon_OOP/Pokemon.txt'
        with open(filepath,'r',encoding='UTF-8') as f: 
            data = f.readlines()
        D = data[i].strip().split() # D = [포켓몬 번호, 이름, 체력, 공격력, 스킬 이름]
        return D

class Pokemon(Unit): # 포켓몬 정보

    def __init__(self,i):
        super().__init__()
        Mon = Data.Dataextract(i)
        self.number = Mon[0] # 리스트 A를 인덱스별로 정리
        self.name = Mon[1]
        self.hp = int(Mon[2])
        self.dmg = int(Mon[3])
        self.skill_name = Mon[4]
    
    def attack(self, enemy_hp):
        return enemy_hp - self.dmg
    
    def s_attack(self,enemy_hp):
        return enemy_hp - (self.dmg * 2)

class Menu():   # 기본적인 메뉴 호출
    
    def __init__(self,A):
        A.status()

    def 마을(self,A):
        flag = True
        while flag:
            print("마을에 들어왔습니다")
            menu = input('1. 내 정보 2. 상점 3. 전투 4. 퀘스트 5. 나가기 > ')
            if menu == '1':
                A.status()
            elif menu == '2':
                print("미구현")
                #Interact.shop()
            elif menu =='3':
                fight.matching(A)
            elif menu =='4':
                print('미구현')
            elif menu == '5':
                print('미구현')     

class fight():
    
    def __init__(self,A):
        pass

    def matching(A):
        list = range(0,5)
        i = random.choice(list)
        enemy = wildenemy(i)
        print("야생의", enemy.name ,'이(가) 나타났다!')
        print("선택할 포켓몬의 이름을 입력하세요")
        print(A.monlist)
        My_mon_name = input("> ")
        if My_mon_name in A.monlist:
            My_mon =  A.monlist.# 새로 선언한거임.
        else:
            print('그런 몬스터는 없습니다')

        while True:
            print('전투가 시작됩니다.')
            print('적의 턴')

            enemy_input = random.choice(['1','2'])
            if enemy_input == '1':
                print("적의 기본공격")
                My_mon.hp = enemy.attack(My_mon.hp)
            elif enemy_input == '2':
                print("공격이 빗나갔습니다")

            print("내 몬스터 체력", My_mon.hp)

            if My_mon.hp <= 0:
                break

            print("아군의 턴")
            print("1. 일반공격")
            print('2. 빗나가기')

            My_input = input('사용할 기술의 번호를 입력하세요 > ')
            if My_input == '1':
                print(My_mon.name ,"의 기본공격")
                enemy.hp = My_mon.attack(enemy.hp)
            elif My_input == '2':
                print("공격이 빗나갔습니다")

            print("적 몬스터 체력", enemy.hp)

            if enemy.hp <= 0:
                break

        print("전투 종료")


"""
class Interact():

    def shop():
        A = User()
        print('상점 진입','\n원하는 몬스터를 구입/판매할 수 있습니다.')
        menu = input('1.구입 2.판매 3.돌아가기')
        if menu == '1':
            buy = input('1.피카츄 2.돌아가기> ')
            if buy == '1':
                print(Pokemon(0).name,'을(를) 구매하였습니다.')
                A.monlist.append(Pokemon(0).name)
                A.monlist_num.append(0)
                print(A.monlist)
            elif buy == '2':
                print('돌아갑니다')
        elif menu == '2':
            sell = input(A.monlist,'중 판매하실 포켓몬의 이름을 입력하세요> ')
            if sell in A.monlist:
                A.monlist.remove(sell)
                A.monlist_num.remove()
                print(sell,'을(를) 판매하였습니다.')
            else:
                print('포켓몬의 이름을 제대로 입력하지 않았습니다')
        elif menu == '3':
            print('돌아갑니다')
"""


def start():
    print('포켓몬스터 게임을 시작합니다.','\n당신의 이름은?')
    A = User()
    A.name = input()
    print('당신의 이름은', A.name, '입니다.')
    my_choice = input('첫 몬스터를 선택해주세요. 1.피카츄 : ')
    if my_choice == '1':
        M = Pokemon(0)
        A.monlist.append(M.name)
        A.monlist_num.append(0)
    AA = Menu(A)
    AA.마을(A)

start()