# The following variables should be refactored into a superclass
# from which weapon and attack_type will inherit these values.
attack_type = ['Bite', 'Claw/Slash', 'Tail whip', 'Bash', 'Gore/Rend']
attack_power = [20, 5, 10, 25, 15]


class AttackType:

    def __init__(self, attack):
        self.type_of_attack = self.attack_type_assignment(attack)
        index = attack_type.index(self.type_of_attack)
        self.attack_power = attack_power[index]

    @staticmethod
    def attack_type_assignment(attack):
        if not attack:
            print(attack_type)
            attack = input('Chose a primary attack from the above list: ')
            if not attack:
                attack = 'Bite'
        return attack
