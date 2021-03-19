# The following variables should be refactored into a superclass
# from which weapon and attack_type will inherit these values.
weapon = ['Phaser', 'Light Saber', 'Rifle', 'Pistol', 'Chain Sword']
attack_power = [20, 15, 10, 5, 25]


class Weapon:

    def __init__(self, weapon_type):
        self.weapon_type = self.weapon_assignment(weapon_type)
        index = weapon.index(self.weapon_type)
        self.attack_power = attack_power[index]

    @staticmethod
    def weapon_assignment(weapon_type):
        if not weapon_type:
            print(weapon)
            weapon_type = input('Chose a weapon from the above list: ')
            if not weapon_type:
                weapon_type = 'Phaser'
        return weapon_type
