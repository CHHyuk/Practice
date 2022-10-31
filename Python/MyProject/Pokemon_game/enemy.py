import all_unit

class 하급_적(all_unit.all_unit):
    def __init__(self):
        self.hp = 20
        self.normal_dmg = 2
        self.skill_dmg = 5

    def normal_attack(self, enemy_hp):
        print(self.name, ", 기본 공격!")
        super().normal_attack()

    def skill_attack(self, enemy_hp):
        print(self.name,", 스킬 공격!")
        super().skill_attack()

class 중급_적(all_unit.all_unit):
    def __init__(self):
        self.hp = 200
        self.normal_dmg = 15
        self.skill_dmg = 50

    def normal_attack(self, enemy_hp):
        print(self.name, ", 기본 공격!")
        super().normal_attack()

    def skill_attack(self, enemy_hp):
        print(self.name,", 스킬 공격!")
        super().skill_attack()
 
class 상급_적(all_unit.all_unit):
    def __init__(self):
        self.hp = 1000
        self.normal_dmg = 30
        self.skill_dmg = 200

    def normal_attack(self, enemy_hp):
        print(self.name, ", 기본 공격!")
        super().normal_attack()

    def skill_attack(self, enemy_hp):
        print(self.name,", 스킬 공격!")
        super().skill_attack()