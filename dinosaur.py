from attack_type import AttackType


class Dinosaur:
    def __init__(self, dino_type, health, energy, attack_type):
        self.dino_type = dino_type
        self.health = health
        self.energy = energy
        self.attack_type = AttackType(attack_type)
        self.attack_power = self.attack_type.attack_power

    def dino_attr_list(self):
        print(f'Name: {self.dino_type}  \n   H: {self.health} E: {self.energy} AT: {self.attack_type.type_of_attack} Att: {self.attack_power}')

