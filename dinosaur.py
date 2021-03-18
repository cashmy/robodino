class Dinosaur:
    def __init__(self, dino_type, health, energy, attack_power):
        self.dino_type = dino_type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power

    def dino_attr_list(self):
        print(f'Name: {self.dino_type}  \n   H: {self.health} E: {self.energy} Att: {self.attack_power}')

