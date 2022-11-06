import User
import Pokemon
import random

class Map():
    
    def operate(self, A):
        gamemap_first = [
    ['1','1','1','1','1','1','1'],
    ['1','C','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','0','0','0','M','1','1'],
    ['1','S','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','1','1','1','1','1','1']
]     
        print(A.User_inven())
        print('이동하여 원하는 마을로 가주세요 wasd를 이용해 이동할 수 있습니다.')
        print('\n')
        for i in range(len(gamemap_first)):
            print(gamemap_first[i])
        print('\n')
        print('\n')
        print('현재 위치 좌표는','[',A.x + 1 ,',', A.y + 1,']','입니다')

        while True:
            A.move(input())
            if A.x == 1 and A.y == 1:
                Town(A, '초원')
                False
            elif A.x == 1 and A.y == 4:
                Town(A, '사막')
                False
            elif A.x == 4 and A.y == 3:
                Town(A, '물')
                False
        

class Town():
    
    def __init__(self,A,Town):
        self.name = Town + '마을'
        print(self.name, '에 오신 것을 환영합니다.')
        flag = True
        while flag:
            menu = input('1.퀘스트 2.상점 3.회복 4.전투 5.나가기 > ')
            if menu == '1':
                print('미구현')
            elif menu == '2':
                Shop.shop(A)
            elif menu == '3':
                Heal.hospital(A)
            elif menu == '4':
                fight.matching(A,Town)
            elif menu == '5' and Town == '초원':
                print('마을을 나갑니다')
                A.x = 1
                A.y = 2
                Map.operate(self, A)
            elif menu == '5' and Town == '사막':
                print('마을을 나갑니다')
                A.x = 1
                A.y = 5
                Map.operate(self, A)
            elif menu == '5' and Town == '물':
                print('마을을 나갑니다')
                A.x = 4
                A.y = 4
                Map.operate(self, A)

            


class fight():

    def matching(A,Town):
        list = range(0,5)
        i = random.choice(list)
        enemy = Pokemon.Pokemon(i)

        print(Town,'마을의 몬스터와 전투를 시작한다.')
        print('선택할 포켓몬을 고르세요')
        print(A.monlist_name)
        My_mon_name = input("> ")
        for x in range(len(A.monlist)):
            if A.monlist_name[x] == My_mon_name:
                My_mon = A.monlist[x]
                print('선택한 몬스터는',A.monlist_name[x],'입니다.')
        
        while True:
            print('전투가 시작됩니다.')
            print('적의 턴')

            enemy_input = random.choice(['1','2','3'])
            if enemy_input == '1':
                print(enemy.name,'의 기본공격!')
                My_mon.hp = My_mon.attack(enemy.dmg)
                print(enemy.dmg,'의 데미지를 입었다.')
            elif enemy_input == '2':
                print(enemy.name,'의',enemy.skill_name,'공격!')
                My_mon.hp = My_mon.attack(enemy.dmg * 2)
                print(enemy.dmg * 2,'의 데미지를 입었다.')
            elif enemy_input == '3':
                print('적의 공격이 빗나갔다.')
            
            print('내 몬스터의 체력 : ',My_mon.hp)

            if My_mon.hp <= 0:
                My_mon.hp = 0
                print('패배')
                print('전투 종료')
                break
            
            print("아군의 턴")
            print("1. 일반공격")
            print('2. 스킬공격')

            My_input = input('사용할 기술의 번호를 입력하세요 > ')
            if My_input == '1':
                print(My_mon.name,'의 기본공격!')
                enemy.hp = enemy.attack(My_mon.dmg)
                print(My_mon.dmg,'의 데미지를 입혔다.')
            elif My_input == '2':
                print(My_mon.name,'의',My_mon.skill_name,'공격!')
                enemy.hp = enemy.attack(My_mon.dmg * 2)
                print(My_mon.dmg * 2,'의 데미지를 입혔다.')

            print('적 몬스터의 체력 : ',enemy.hp)

            if enemy.hp <= 0:
                print('승리!! 100원과 100의 경험치를 얻었다.')
                A.money += 100
                My_mon.exp += 100
                if My_mon.exp >= 100:
                    print('레벨업!!')
                    My_mon.lv += 1
                    My_mon.exp -= 100
                    print(My_mon.name,'의 레벨이 1 올라',My_mon.lv,'레벨이 되었습니다.')
                print('전투 종료')
                break
        
class Heal():

    def hospital(A):
        while True:
            menu = input('몬스터를 모두 회복시키겠습니까? Y/N >')
            if menu == 'Y':
                for i in range(len(A.monlist)):
                    A.monlist[i].hp += 10
                    print(A.monlist[i].mon_status())
                print('모든 몬스터의 체력이 10 회복되었습니다.')
            elif menu == 'N':
                print('돌아갑니다')
                break



class Shop():

    def shop(A):
        while True:
            print('상점 진입','\n원하는 몬스터를 구입/판매할 수 있습니다.')
            menu = input('1.구입 2.판매 3.돌아가기 > ')
            if menu == '1':
                print('구입하실 물건을 선택해주세요')
                buy = input('1.피카츄(100원) 2.돌아가기')
                if buy == '1':
                    if A.money >= 100:
                        print(Pokemon.Pokemon(0).name,'을(를) 구매하였습니다.')
                        A.monlist.append(Pokemon.Pokemon(0))
                        A.monlist_name.append(Pokemon.Pokemon(0).name)
                        print('현재 보유중인 포켓몬',A.monlist_name)
                    else:
                        print('돈이 부족합니다.')
                elif buy == '2':
                    pass
            elif menu == '2':
                print('판매하실 물건을 선택해주세요')
                print(A.itemlist)
                sell = input('1.나가기')
                if sell == '1':
                    pass
            elif menu == '3':
                break

            
                
            

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




