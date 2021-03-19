# Imports
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield
import random_attack


def make_an_attack(attack_power):
    hit = random_attack.random_att(attack_power)
    return hit


def battle_action():
    # NOTE: THIS REALLY SHOULD BE DONE USING A DATABASE OR AN ARRAY/LIST
    #       RATHER THAN SEPARATE INSTANCES OF  ROBOTS AND DINOSAURS.
    #       AN ARRAY/LIST WOULD BE MUCH MORE EFFICIENT
    # Assemble the robots
    print('\n================================')
    robot1 = Robot('Able', 50, 100, 'Phaser').robot_attr_list()
    robot2 = Robot('Baker', 50, 100, 'Phaser').robot_attr_list()
    robot3 = Robot('Sarge', 125, 250, 'Chain Sword').robot_attr_list()

    robot_fleet = Fleet('Armageddon')
    robot_fleet.assign_member(robot3.name, robot3.attack_power, robot3.health)
    robot_fleet.assign_member(robot1.name, robot1.attack_power, robot1.health)
    robot_fleet.assign_member(robot2.name, robot2.attack_power, robot2.health)
    robot_fleet.fleet_status()

    # Assemble the dinosaurs
    print('\n================================')
    dinosaur1 = Dinosaur('Triceratops', 75, 100, 'Bash').dino_attr_list()
    dinosaur2 = Dinosaur('Velociraptor', 50, 200, 'Tail whip').dino_attr_list()
    dinosaur3 = Dinosaur('T-Rex', 100, 250, 'Bite').dino_attr_list()

    dinosaur_herd = Herd('R-r-raw-R!')
    dinosaur_herd.add_member(dinosaur3.dino_type, dinosaur3.attack_power, dinosaur3.health)
    dinosaur_herd.add_member(dinosaur1.dino_type, dinosaur1.attack_power, dinosaur1.health)
    dinosaur_herd.add_member(dinosaur2.dino_type, dinosaur2.attack_power, dinosaur2.health)
    dinosaur_herd.herd_status()

    # Create the battle field
    water_loo = Battlefield('Water Loo')
    water_loo.side1_name = robot_fleet.name
    water_loo.side2_name = dinosaur_herd.name
    water_loo.side1_points = robot_fleet.defense_points
    water_loo.side2_points = dinosaur_herd.defense_points

    # Now fight
    battle_ended = False
    counter = 0
    engagements = len(robot_fleet.members)
    water_loo.battle_status()
    print('\n\n ***** Battle commencing *****')
    detail_print = input('Do you wish to see the details? (y/n): ')
    while not battle_ended:
        side1_damage = 0
        side2_damage = 0
        damage1 = 0
        # battle strikes happen here...
        if robot1.health > 0 and dinosaur1.health > 0:
            robot_attack_damage = make_an_attack(robot1.attack_power)
            dino_attack_damage = make_an_attack(dinosaur1.attack_power)
            dinosaur1.update_health(robot_attack_damage)
            robot1.update_health(dino_attack_damage)
            if detail_print == 'y':
                print(f'Robot {robot1.name} hits {dinosaur1.dino_type} for {robot_attack_damage} damage '
                      f'and it has {dinosaur1.health} health left.')
                print(f'The {dinosaur1.dino_type} hits {robot1.name} for {dino_attack_damage} damage '
                      f'and it has {robot1.health} health left.\n')
            side1_damage += dino_attack_damage
            side2_damage += robot_attack_damage
        else:
            engagements -= 1

        if robot2.health > 0 and dinosaur2.health > 0:
            robot_attack_damage = make_an_attack(robot2.attack_power)
            dino_attack_damage = make_an_attack(dinosaur2.attack_power)
            dinosaur2.update_health(robot_attack_damage)
            robot2.update_health(dino_attack_damage)
            if detail_print == 'y':
                print(f'Robot {robot2.name} hits {dinosaur2.dino_type} for {robot_attack_damage} damage '
                      f'and it has {dinosaur2.health} health left.')
                print(f'The {dinosaur2.dino_type} hits {robot2.name} for {dino_attack_damage} damage '
                      f'and it has {robot2.health} health left.\n')
            side1_damage += dino_attack_damage
            side2_damage += robot_attack_damage
        else:
            engagements -= 1

        if robot3.health > 0 and dinosaur3.health > 0:
            robot_attack_damage = make_an_attack(robot3.attack_power)
            dino_attack_damage = make_an_attack(dinosaur3.attack_power)
            dinosaur3.update_health(robot_attack_damage)
            robot3.update_health(dino_attack_damage)
            if detail_print == 'y':
                print(f'Robot {robot3.name} hit the {dinosaur3.dino_type} for {robot_attack_damage} damage '
                      f'and it has {dinosaur3.health} health left.')
                print(f'The {dinosaur3.dino_type} hit robot {robot3.name} for {dino_attack_damage} damage '
                      f'and it has {robot3.health} health left.\n')
            side1_damage += dino_attack_damage
            side2_damage += robot_attack_damage
        else:
            engagements -= 1

        water_loo.update_battle_status(side1_damage, side2_damage)
        if detail_print == 'y':
            water_loo.battle_status()
        counter += 1
        battle_ended = water_loo.battle_results(counter, engagements, detail_print)
        if engagements == 0:
            battle_ended = True
        elif counter > 15:
            print('Battle has stalemated. Troops are going home.')
            battle_ended = True
