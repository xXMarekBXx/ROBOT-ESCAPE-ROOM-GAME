import os
from robot import Robot
from scene import Scene

robot = Robot()
scene = Scene()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[H\033[J")


def draw_the_game():
    clear_console()
    x, y = robot.get_robot_possition()
    scene.draw_scene_with_robot(x, y)
    moving_the_robot = input("Move your robot by pressing:"
                             " 'W' to go up,"
                             " 'S' to go down,"
                             " 'A' to go left"
                             " and 'D' to go right: ").lower()
    robot.set_robot_possition(moving_the_robot)
    x, y = robot.get_robot_possition()
    scene.draw_scene_with_robot(x, y)


clear_console()
print("WELCOME IN ROBOT ESCAPE ROOM GAME !!!")
print("Are You sure You want to continue?")

start_the_game = "Y"
close_the_game = "N"
player_choice = input("press 'Y' if you want to play or 'N' if you want to close the game: ").lower()

if player_choice == "n":
    exit()
elif player_choice == "y":
    while True:
        draw_the_game()
