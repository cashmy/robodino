# The following variables should be refactored into a superclass
# from which weapon and attack_type will inherit these values.
weapon = ['Phaser', 'Light Saber', 'Rifle', 'Pistol', 'Chain Sword']
attack_power = [20, 15, 10, 5, 25]


class Weapon:

    def __init__(self, weapon_type):
        self.weapon_type = weapon_type
        index = weapon.index(weapon_type)
        self.attack_power = attack_power[index]
