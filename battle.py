# Imports
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd


def battle_action():
    # Assemble the robots
    print('\n================================')
    robot1 = Robot('Able', 100, 100, 'Phaser')
    robot1.robot_attr_list()
    robot2 = Robot('Baker', 100, 100, 'Phaser')
    robot2.robot_attr_list()
    robot3 = Robot('Sarge', 250, 250, 'Chain Sword')
    robot3.robot_attr_list()

    robot_fleet = Fleet('Armageddon')
    robot_fleet.assign_member(robot3.name, robot3.attack_power)
    robot_fleet.assign_member(robot1.name, robot1.attack_power)
    robot_fleet.assign_member(robot2.name, robot2.attack_power)
    robot_fleet.fleet_status()

    # Assemble the dinosaurs
    print('\n================================')
    dinosaur1 = Dinosaur('Triceratops', 200, 100, 'Bash')
    dinosaur1.dino_attr_list()
    dinosaur2 = Dinosaur('Velociraptor', 100, 200, 'Tail whip')
    dinosaur2.dino_attr_list()
    dinosaur3 = Dinosaur('T-Rex', 250, 250, 'Bite')
    dinosaur3.dino_attr_list()

    dinosaur_herd = Herd('R-r-raw-R!')
    dinosaur_herd.add_member(dinosaur3.dino_type, dinosaur3.attack_power)
    dinosaur_herd.add_member(dinosaur1.dino_type, dinosaur1.attack_power)
    dinosaur_herd.add_member(dinosaur2.dino_type, dinosaur2.attack_power)
    dinosaur_herd.herd_status()

