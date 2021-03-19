from weapon import Weapon


class Robot:
    def __init__(self, name, health, power_level, weapon_type):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = Weapon(weapon_type)
        self.attack_power = self.weapon.attack_power

    def robot_attr_list(self):
        print(f'Name: {self.name}  \n   H: {self.health} P: {self.power_level} W: {self.weapon.weapon_type} Att: {self.weapon.attack_power}')
        return self

    def update_health(self, damage):
        self.health -= damage
        return self

    def update_power_level(self, energy_expended):
        self.power_level -= energy_expended
        return self
