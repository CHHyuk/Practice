import all_unit

class slime(all_unit.all_unit):
    hp = 10
    normal_dmg = 3

    def normal_attack(self, enemy_hp):
        print("슬라임의 공격!")
        super().normal_attack()


class dragon(all_unit.all_unit):
    hp = 1000
    normal_dmg = 50
    skill_dmg = 300

    def normal_attack(self, enemy_hp):
        print("드래곤의 공격!")
        super().normal_attack()

    def skill_attack(self, enemy_hp):
        print("드래곤의 강력한 스킬공격!")
        super().normal_attack()
