class Battlefield:
    def __init__(self):
        self.name_of_battle = ""
        self.side1_name = ""  # The aggressors
        self.side2_name = ""  # The defenders
        self.side1_points = 0
        self.side2_points = 0

    def robot_attack(self, robot, dinosaur):
        pass

    def dino_attack(self, dinosaur, robot):
        pass

    def battle_action(self):
        if self.side1_points <= 0:
            print(f'The defenders, {self.side2_name} have beat back the terrible attackers!')
        elif self.side2_points <= 0:
            print(f'The attackers, {self.side1_name} have aggressively won the day!')
        else:
            print(f'The battle is still raging!')
