from game import Game
from direction import Direction


def get_user_confirmation() -> bool:
    """
    Ask the user whether they want to start the game.

    This function repeatedly prompts the user for confirmation until a valid
    response ('Y' or 'N') is provided. It ensures that the program does not
    proceed with invalid input.

    Returns:
        bool: True if the user chooses to start the game, False otherwise.
    """
    while True:
        choice = input("Are You sure You want to continue?\nPress 'Y' to play or 'N' to exit: ").strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input. Please press 'Y' or 'N'.\n")


def get_move_input() -> Direction:
    """
    Prompt the user for a movement command and validate the input.

    The function accepts only the WASD keys (case-insensitive). If the user
    enters anything else, they are prompted again until a valid direction is
    provided.

    Returns:
        Direction: The direction corresponding to the user's input.
    """
    while True:
        key = input("Move your robot by pressing: 'W' to go up, 'S' to go down, "
                    "'A' to go left and 'D' to go right: ").strip().lower()

        if key == "w":
            return Direction.UP
        elif key == "s":
            return Direction.DOWN
        elif key == "a":
            return Direction.LEFT
        elif key == "d":
            return Direction.RIGHT
        else:
            print("Invalid input. Please press W, A, S or D.\n")


def main() -> None:
    """
    Main entry point of the Robot Escape Room game.

    This function:
    - displays the welcome message,
    - asks the user for confirmation to start,
    - initializes the game controller,
    - repeatedly draws the scene, processes moves, and checks win conditions,
    - ends the game when the robot reaches the goal tile.

    The function handles all user interaction and delegates game logic to the
    Game class.
    """
    print("WELCOME IN ROBOT ESCAPE ROOM GAME !!!")

    if not get_user_confirmation():
        print("Goodbye!")
        return

    print("\nLet's go!")

    game = Game()

    while True:
        # Draw the current state of the map with the robot
        x, y = game.robot.get_position()
        game.scene.draw_scene_with_robot(x, y)

        # Get a valid movement direction from the user
        direction = get_move_input()

        # Process the move and display feedback
        status = game.process_move(direction)

        if status.is_blocked():
            print(f"Move NOT allowed. {status.message()} Try again.\n")
        else:
            print("Good move :) Keep going!\n")

        # Check win condition
        if game.check_win():
            print("YOU HAVE WON!!!")
            print(f"You did it in: {game.moves} moves :)")
            print("CONGRATULATIONS!!!")
            break


if __name__ == "__main__":
    main()
