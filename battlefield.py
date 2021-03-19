import random_attack
from robot import Robot


class Battlefield:
    battle_end = False

    def __init__(self, name):
        self.name_of_battle = name
        self.side1_name = "Offenders"  # The aggressors
        self.side2_name = "Defenders"  # The defenders
        self.side1_points = 10
        self.side2_points = 10

    def update_battle_status(self, side1_hits, side2_hits):
        self.side1_points -= side1_hits
        self.side2_points -= side2_hits

    def battle_status(self):
        print(f'The Attackers: {self.side1_name} have a current defense of {self.side1_points}')
        print(f'The Defenders: {self.side2_name} have a current defense of {self.side2_points}')

    def battle_results(self, attack_turns, engagements):
        if self.side1_points <= 0:
            print(f'The defenders, {self.side2_name} have beat back the terrible attackers after {attack_turns} actions!')
            self.battle_end = True
        elif self.side2_points <= 0:
            print(f'The attackers, {self.side1_name} have aggressively won the day after {attack_turns} actions!')
            self.battle_end = True
        elif engagements <= 0:
            if self.side2_points > self.side1_points:
                print(f'The Defenders {self.side2_name} has a successful defense after {attack_turns} actions.')
            else:
                print(f'The Attackers {self.side1_name} has a tactical victory after {attack_turns} actions.')
            self.battle_end = True
        else:
            print(f' *****     The battle is still raging!     ***** \n')
        return self.battle_end
