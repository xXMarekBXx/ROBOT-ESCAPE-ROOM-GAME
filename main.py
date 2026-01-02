import os
from robot import Robot
from scene import Scene

robot = Robot()
scene = Scene()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[H\033[J")


def clear_console_draw_scene_and_give_appropriate_announcement(announcement):
    x, y = robot.get_robot_possition()
    clear_console()
    print(announcement)
    scene.draw_scene_with_robot(x, y)


def won_announcement():
    print("YOU HAVE WON!!!")
    print(f"You did it in: {robot.moves} moves :)")
    print("CONGRATULATIONS!!!")


def move_input():
    move = input("Move your robot by pressing:"
                 " 'W' to go up,"
                 " 'S' to go down,"
                 " 'A' to go left"
                 " and 'D' to go right: ").lower()
    return move


def starting_announcement():
    clear_console()
    print("WELCOME IN ROBOT ESCAPE ROOM GAME !!!")
    print("Are You sure You want to continue?")


def check_next_move(x, y, direction):
    new_x = x
    new_y = y

    if direction == 'w':
        new_y = y - 1
    elif direction == 's':
        new_y = y + 1
    elif direction == 'a':
        new_x = x - 1
    elif direction == 'd':
        new_x = x + 1
    return new_x, new_y


def draw_the_game():
    x, y = robot.get_robot_possition()

    if scene.is_goal(x, y):
        won_announcement()
        return True

    moving_the_robot = move_input()

    new_x, new_y = check_next_move(x, y, moving_the_robot)

    status = scene.check_if_move_is_allowed(new_x, new_y)

    if status == "move allowed":
        robot.set_robot_possition(moving_the_robot)
        clear_console_draw_scene_and_give_appropriate_announcement("Good move :)"
                                                                   " Keep going!")
    elif status == "border":
        clear_console_draw_scene_and_give_appropriate_announcement("Move NOT allowed. "
                                                                   "You have collided with the border of the map! "
                                                                   "Please try a different move.")
    elif status == "obstacle":
        clear_console_draw_scene_and_give_appropriate_announcement("Move NOT allowed. "
                                                                   "You have collided with the obstacle! "
                                                                   "Please try a different move.")


starting_announcement()
start_the_game = "Y"
close_the_game = "N"

while True:
    player_choice = input("Press 'Y' if you want to play or 'N' if you want to close the game: ").lower()

    if player_choice in ("y", "n"):
        break
    else:
        print("Invalid choice.")

if player_choice == "n":
    exit()
elif player_choice == "y":
    clear_console_draw_scene_and_give_appropriate_announcement("Lets Go!")
    while True:
        if draw_the_game():
            break
