attack_type = ['Bite', 'Claw/Slash', 'Tail whip', 'Bash', 'Gore/Rend']
attack_power = [20, 5, 10, 25, 15]


class AttackType:

    def __init__(self, type_of_attack):
        self.type_of_attack = type_of_attack
        index = attack_type.index(type_of_attack)
        self.attack_power = attack_power[index]
