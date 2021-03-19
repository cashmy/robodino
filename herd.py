class Herd:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.strength_points = 0

    def add_member(self, dino_type, attack_power):
        # Do not allow duplicates
        # Refactor to allow for multiple number of dino_types
        #   ... and reduce the 'count' of the dino-types rather than remove in the 'kill' method.
        try:
            self.members.index(dino_type)
        except ValueError:
            self.members.append(dino_type)
        finally:
            self.strength_points += attack_power

    def kill_member(self, name, attack_power):
        try:
            self.members.remove(name)
        except ValueError:
            pass
        finally:
            self.strength_points -= attack_power

    def herd_status(self):
        print(f'Herd: {self.name} has {len(self.members)} members and total strength of {self.strength_points}')
        counter = 0
        while counter < len(self.members):
            print(f'      {self.members[counter]}')
            counter += 1
