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

    # This method takes in a array of objects and assigns the whole group to a fleet)
    def assign_cohort(self, robots_to_add):
        # Ex: robots_to_add[('R2D2', 10),('C3PO', 20),('R5D6', 30)]
        counter = 0
        while 0 < len(robots_to_add):
            self.assign_member(robots_to_add)
            counter += 1
