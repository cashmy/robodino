from attack_type import AttackType


class Dinosaur:
    def __init__(self, dino_type, health, energy, attack_type):
        self.dino_type = dino_type
        self.health = health
        self.energy = energy
        self.attack_type = AttackType(attack_type)
        self.attack_power = self.attack_type.attack_power

    def dino_attr_list(self):
        print(f'Name: {self.dino_type}  \n   H: {self.health} E: {self.energy} '
              f'AT: {self.attack_type.type_of_attack} Att: {self.attack_power}')
        return self

    def update_health(self, damage):
        self.health -= damage
        return self

    def update_energy(self, energy_expended):
        self.energy -= energy_expended
        return self
