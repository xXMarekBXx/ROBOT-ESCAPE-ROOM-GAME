import os
from robot import Robot
from scene import Scene

robot = Robot()
scene = Scene()

moves = 0


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def update_screen(message):
    x, y = robot.get_position()
    clear_console()
    print(message)
    scene.draw_scene_with_robot(x, y)


def won_announcement():
    print("YOU HAVE WON!!!")
    print(f"You did it in: {moves} moves :)")
    print("CONGRATULATIONS!!!")


def move_input():
    valid_moves = {"w", "a", "s", "d"}

    while True:
        move = input(
            "Move your robot by pressing:"
            " 'W' to go up,"
            " 'S' to go down,"
            " 'A' to go left"
            " and 'D' to go right: "
        ).lower()

        if move in valid_moves:
            return move

        print("Invalid input. Please press W, A, S or D.")


def starting_announcement():
    clear_console()
    print("WELCOME IN ROBOT ESCAPE ROOM GAME !!!")
    print("Are You sure You want to continue?")


def check_next_move(x, y, direction):
    new_x = x
    new_y = y

    if direction == 'w':
        new_y -= 1
    elif direction == 's':
        new_y += 1
    elif direction == 'a':
        new_x -= 1
    elif direction == 'd':
        new_x += 1

    return new_x, new_y


def check_win():
    x, y = robot.get_position()
    return scene.is_goal(x, y)


def process_move(direction):
    x, y = robot.get_position()
    new_x, new_y = check_next_move(x, y, direction)
    return scene.check_if_move_is_allowed(new_x, new_y)


def apply_move(direction):
    robot.move(direction)


# -------------------------
# GAME START
# -------------------------

starting_announcement()

while True:
    player_choice = input("Press 'Y' to play or 'N' to exit: ").lower()

    if player_choice in ("y", "n"):
        break
    print("Invalid choice.")

if player_choice == "n":
    exit()

update_screen("Let's go!")

while True:

    if check_win():
        won_announcement()
        break

    direction = move_input()

    status = process_move(direction)

    if status == "move allowed":
        moves += 1
        apply_move(direction)
        update_screen("Good move :) Keep going!")

    elif status == "border":
        update_screen("Move NOT allowed. You hit the border! Try again.")

    elif status == "obstacle":
        update_screen("Move NOT allowed. You hit an obstacle! Try again.")
