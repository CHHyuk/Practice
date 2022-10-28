
class all_unit():
    def normal_attack(self, enemy_hp):
        return enemy_hp - self.normal_dmg
    
    def skill_attack(self, enemy_hp):
        return enemy_hp - self.skill_dmg
