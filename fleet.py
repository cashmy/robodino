from robot import Robot


class Fleet:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.strength_points = 0

    def assign_member(self, name, attack_power):
        # Do not allow duplicates
        try:
            self.members.index(name)
        except ValueError:
            self.members.append(name)
        finally:
            self.strength_points += attack_power

    def kill_member(self, name, attack_power):
        try:
            self.members.remove(name)
        except ValueError:
            pass
        finally:
            self.strength_points -= attack_power

    def fleet_status(self):
        print(f'Fleet: {self.name} has {len(self.members)} members and total strength of {self.strength_points}')
        counter = 0
        while counter < len(self.members):
            print(f'       {self.members[counter]}')
            counter += 1
