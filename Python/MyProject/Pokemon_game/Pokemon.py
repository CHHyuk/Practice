import all_unit
import enemy


class Pokemon(all_unit.all_unit):
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.exp = 0
        self.lv = 1
        self.normal_dmg = 0
        self.skill_dmg = 0

    def hospital(self):
        print(self.name, '이(가) 회복 되었습니다.')
        print('HP  +10')
        print('현재 체력 : ',self.hp)

    def training(self):
        print(self.name, '이(가) 훈련을 했습니다.')
        print('EXP  +10')
        print('HP  -5')
        print('현재 체력 : ',self.hp)
        print('현재 경험치 : ',self.exp)

    def levelup(self):
        print(self.name, '이(가) 레벨업 하였습니다')
        print('LV  +1')
        print('현재 레벨 : ',self.lv)
    
    def status(self):
        print(self.name)
        print('HP:', self.hp)
        print('EXP:', self.exp)
        print('LV:', self.lv)
        print('기본 데미지 : ',self.normal_dmg)
        print('스킬 데미지 : ',self.skill_dmg)
    
    def evolution(self):
        print(self.name, '이(가) 진화하였습니다.')
    
class 피카츄(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = '피카츄'
        self.hp = 30
        self.normal_dmg = 3
        self.skill_dmg = 20
    
    def hospital(self):
        self.hp += 10
        super().hospital()

    def training(self):
        if self.hp > 5:
            self.exp += 10
            self.hp -= 5
            super().training()
            if self.exp >= 100:
                self.levelup()
                self.evolution()
            else:
                pass
        else:
            print('체력이 부족하여 훈련을 할 수 없습니다.')

    def levelup(self):
        if self.exp >= 100:
            self.exp -= 100
            self.lv += 1
            super().levelup()
        else:
            pass
    
    def evolution(self):
        if self.lv >= 10 and self.name =='피카츄':
            super().evolution()
            self.name = '라이츄'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        elif self.lv >= 30 and self.name == '라이츄':
            super().evolution()
            self.name = '라이츄 ver.2'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        else:
            pass

class 파이리(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = '파이리'
        self.hp = 25
        self.normal_dmg = 8
        self.skill_dmg = 20
    
    def hospital(self):
        self.hp += 10
        super().hospital()

    def training(self):
        if self.hp > 5:
            self.exp += 10
            self.hp -= 5
            super().training()
            if self.exp >= 100:
                self.levelup()
                self.evolution()
            else:
                pass
        else:
            print('체력이 부족하여 훈련을 할 수 없습니다.')

    def levelup(self):
        if self.exp >= 100:
            self.exp -= 100
            self.lv += 1
            super().levelup()
        else:
            pass
    
    def evolution(self):
        if self.lv >= 10 and self.name =='파이리':
            super().evolution()
            self.name = '리자드'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        elif self.lv >= 30 and self.name == '리자드':
            super().evolution()
            self.name = '리자몽'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        else:
            pass

class 꼬부기(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = '꼬부기'
        self.hp = 30
        self.normal_dmg = 5
        self.skill_dmg = 15
    
    def hospital(self):
        self.hp += 10
        super().hospital()

    def training(self):
        if self.hp > 5:
            self.exp += 10
            self.hp -= 5
            super().training()
            if self.exp >= 100:
                self.levelup()
                self.evolution()
            else:
                pass
        else:
            print('체력이 부족하여 훈련을 할 수 없습니다.')

    def levelup(self):
        if self.exp >= 100:
            self.exp -= 100
            self.lv += 1
            super().levelup()
        else:
            pass
    
    def evolution(self):
        if self.lv >= 10 and self.name =='꼬부기':
            super().evolution()
            self.name = '어니부기'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        elif self.lv >= 30 and self.name == '어니부기':
            super().evolution()
            self.name = '거북왕'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        else:
            pass

class 이상해씨(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = '이상해씨'
        self.hp = 40
        self.normal_dmg = 5
        self.skill_dmg = 15
    
    def hospital(self):
        self.hp += 10
        super().hospital()

    def training(self):
        if self.hp > 5:
            self.exp += 10
            self.hp -= 5
            super().training()
            if self.exp >= 100:
                self.levelup()
                self.evolution()
            else:
                pass
        else:
            print('체력이 부족하여 훈련을 할 수 없습니다.')

    def levelup(self):
        if self.exp >= 100:
            self.exp -= 100
            self.lv += 1
            super().levelup()
        else:
            pass
    
    def evolution(self):
        if self.lv >= 10 and self.name =='이상해씨':
            super().evolution()
            self.name = '이상해풀'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        elif self.lv >= 30 and self.name == '이상해풀':
            super().evolution()
            self.name = '이상해꽃'
            print(self.name, '(으)로 진화 하였습니다. 축하합니다.')
        else:
            pass

class Menu():
    def __init__(self, M):
        self.mon = M
    
    def run(self):
        flag = True
        while flag:
            menu = int(input('1.상태창 2.병원(hp +10) 3.훈련(exp +10 hp -5) 4.전투(미구현) 5.종료 > '))
            if menu == 1:
                self.mon.status()
            elif menu == 2:
                self.mon.hospital()
            elif menu == 3:
                self.mon.training()
            elif menu == 4:
                go = input('1. 슬라임 평원, 2. 드래곤 레어 3. 돌아가기 > ')
                if go == '1':
                    fight()
                elif go == '2':
                    fight()
                elif go == '3':
                    continue
            elif menu == 5:
                flag = False


def start():
    print('포켓몬스터 게임을 시작합니다.')
    my_choice = input('몬스터를 선택해주세요. 1.피카츄 2.파이리 3.꼬부기 4.이상해씨 : ')
    M = None
    if my_choice == '1':
        M = 피카츄()
    if my_choice == '2':
        M = 파이리()
    if my_choice == '3':
        M = 꼬부기()
    elif my_choice == '4':
        M = 이상해씨()
    M.status()
    MM = Menu(M)
    MM.run()

start()

"""
def fight():
    slime = enemy.slime
    dragon = enemy.dragon
    while True:
"""