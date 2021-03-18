class Fleet:
    def __init__(self):
        self.name = ""
        self.members = []
        self.strength_points = 0

    def add_member(self, name, attack_power):
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
