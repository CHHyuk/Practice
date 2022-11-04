from Pokemon_data import Dataextract

class Unit(): # 모든 유닛들은 고유한 이름과 능력치를 가짐
    
    def __init__(self):
        self.number = 0
        self.name = ''
        self.lv = 1
        self.hp = 0
        self.exp = 0
        self.dmg = 0
        self.skill_name = ''

class Pokemon(Unit): # 포켓몬 정보

    def __init__(self,i):
        super().__init__()
        Mon = Dataextract(i)
        self.number = Mon[0] # 리스트 A를 인덱스별로 정리
        self.name = Mon[1]
        self.hp = int(Mon[2])
        self.dmg = int(Mon[3])
        self.skill_name = Mon[4]