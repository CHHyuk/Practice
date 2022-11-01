from re import S


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
    
    def __init__(self):
        self.monlist = [0,0,0,0,0,0] # 각 자리마다 한마리씩 들어감, 최대 6마리 가지고다님, 0 = 아무것도 없는 상태
        self.itemlist = {'작은 포션':0,'큰 포션':0,'기타 아이템':0} # 인벤토리 작은포션 10 회복 / 큰포션 30 회복 / 기타아이템 상점판매시 10원
        self.money = 0

class Data():
    
    def Dataextract(i):
        filepath = 'C:/git/Practice/Python/MyProject/Pokemon_OOP/Pokemon.txt'
        with open(filepath,'r',encoding='UTF-8') as f: 
            data = f.readlines()
        D = data[i].strip().split() # D = [포켓몬 번호, 이름, 체력, 공격력, 스킬 이름]
        return D

class Pokemon(Unit,Data): # 포켓몬 정보

    def __init__(self,i):
        super().__init__()
        self.number = D[0] # 리스트 D를 인덱스별로 정리
        self.name = D[1]
        self.hp = D[2]
        self.dmg = D[3]
        self.skill_name = D[4]

class Interact(Pokemon): # 전투, 상점 등 상호작용

    def __init__(self):
        super().__init__()
    
  #  def hospital(self):

def start():
    print('포켓몬스터 게임을 시작합니다.')
    my_choice = input('첫 몬스터를 선택해주세요. 1.피카츄 2.파이리 3.꼬부기 4.이상해씨 : ')
    if my_choice == '1':
        
    elif my_choice == '2':
        Pokemon
    elif my_choice == '3':
        Data.Dataextract(2)
    elif my_choice == '4':
        Data.Dataextract(3)

start()


# class Map(): # 맵 시스템

  #  def 


A = Pokemon(0)
print(A.number,A.name,A.hp,A.dmg,A.exp,A.skill_name)