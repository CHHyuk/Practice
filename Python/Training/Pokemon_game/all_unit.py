
class all_unit():
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.exp = 0
        self.lv = 1
        self.normal_dmg = 0
        self.skill_dmg = 0
    
    def normal_attack(self, enemy_hp):
        return enemy_hp - self.normal_dmg
    
    def skill_attack(self, enemy_hp):
        return enemy_hp - self.skill_dmg
