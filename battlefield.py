import random_attack


class Battlefield:
    battle_end = False

    def __init__(self, name):
        self.name_of_battle = name
        self.side1_name = "Offenders"  # The aggressors
        self.side2_name = "Defenders"  # The defenders
        self.side1_points = 10
        self.side2_points = 10

    def robot_attack(self, robot_name, dinosaur_type):
        robot_hit = random_attack.random_att(10)
        return robot_hit

    def dino_attack(self, dinosaur_type, robot_name):
        pass

    def battle_results(self):
        if self.side1_points <= 0:
            print(f'The defenders, {self.side2_name} have beat back the terrible attackers!')
            self.battle_end = True
        elif self.side2_points <= 0:
            print(f'The attackers, {self.side1_name} have aggressively won the day!')
            self.battle_end = True
        else:
            print(f'The battle is still raging!')