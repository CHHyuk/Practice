
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
        Mon = mon_list[i] # 리소스 아끼기
        self.number = Mon[0] # 리스트 A를 인덱스별로 정리
        self.name = Mon[1]
        self.hp = int(Mon[2])
        self.dmg = int(Mon[3])
        self.skill_name = Mon[4]
    
    def mon_status(self):
        print('몬스터 정보')
        print('이름 :',self.name)
        print('포켓몬 넘버 :',self.number)
        print('체력 :',self.hp)
        print('공격력 :',self.dmg)
        print('스킬 :',self.skill_name)
    
    def attack(self,enemy_dmg):
        return self.hp - enemy_dmg


filepath = 'C:\Users\Administrator\Desktop\12-21\Practice\Python\Training\Pokemon_final\Pokemon.txt'
with open(filepath,'r',encoding='UTF-8') as f: 
    mon_status = f.readlines()

mon_list = []
for i in mon_status:
    mon_list = mon_list + [i.split()]


    

