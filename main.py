# Imports
from robot import Robot
from dinosaur import Dinosaur


def print_hi(name):
    print(f'Hi {name}, Lets get ready to r-u-u-u-m-ble!')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Cash')

    # Assemble the robots
    print('\n================================')
    robot1 = Robot('Able', 100, 100, 'Phaser')
    robot1.robot_attr_list()
    robot2 = Robot('Baker', 100, 100, 'Phaser')
    robot2.robot_attr_list()
    robot3 = Robot('Sarge', 250, 250, 'Chain Sword')
    robot3.robot_attr_list()

    # Assemble the dinosaurs
    print('\n================================')
    dinosaur1 = Dinosaur('Triceratops', 200, 100, 'Bash')
    dinosaur1.dino_attr_list()
    dinosaur2 = Dinosaur('Velociraptor', 100, 200, 'Tail whip')
    dinosaur2.dino_attr_list()
    dinosaur3 = Dinosaur('T-Rex', 250, 250, 'Bite')
    dinosaur3.dino_attr_list()
