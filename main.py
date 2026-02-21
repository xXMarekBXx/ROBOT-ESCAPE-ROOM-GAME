import os
from game import Game
from status import MoveStatus
from direction import Direction


def clear_console() -> None:
    """
    Clear the terminal screen.

    Uses the appropriate command depending on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def update_screen(game: Game, message: str) -> None:
    """
    Clear the screen and redraw the game scene with the robot.

    Args:
        game (Game): The current game instance containing robot and scene.
        message (str): A message to display above the scene.
    """
    x, y = game.robot.get_position()
    clear_console()
    print(message)
    game.scene.draw_scene_with_robot(x, y)


def won_announcement(game: Game) -> None:
    """
    Display a winning message when the player reaches the goal.

    Args:
        game (Game): The current game instance, used to show move count.
    """
    print("YOU HAVE WON!!!")
    print(f"You did it in: {game.moves} moves :)")
    print("CONGRATULATIONS!!!")


def move_input() -> Direction:
    """
    Prompt the user for a movement direction until a valid one is entered.

    Returns:
        Direction: One of the Direction enum values (UP, DOWN, LEFT, RIGHT).
    """
    while True:
        key = input(
            "Move your robot by pressing:"
            " 'W' to go up,"
            " 'S' to go down,"
            " 'A' to go left"
            " and 'D' to go right: "
        ).lower()

        direction = Direction.key_to_direction(key)

        if direction is not None:
            return direction

        print("Invalid input. Please press W, A, S or D.")


def starting_announcement() -> None:
    """
    Display the initial welcome message before the game starts.
    """
    clear_console()
    print("WELCOME IN ROBOT ESCAPE ROOM GAME !!!")
    print("Are You sure You want to continue?")


def check_next_move(x: int, y: int, direction: Direction) -> tuple[int, int]:
    """
    Calculate the next position based on the movement direction.

    Args:
        x (int): Current x coordinate.
        y (int): Current y coordinate.
        direction (Direction): Movement direction enum value.

    Returns:
        tuple[int, int]: New (x, y) position after applying the movement.
    """
    dx, dy = Direction.delta(direction)
    return x + dx, y + dy


def check_win(game: Game) -> bool:
    """
    Check whether the robot has reached the goal.

    Args:
        game (Game): The current game instance.

    Returns:
        bool: True if the robot is on the goal tile, otherwise False.
    """
    x, y = game.robot.get_position()
    return game.scene.is_goal(x, y)


def process_move(game: Game, direction: Direction) -> MoveStatus:
    """
    Determine whether a move is allowed based on the game scene.

    Args:
        game (Game): The current game instance.
        direction (Direction): Movement direction enum value.

    Returns:
        MoveStatus: Status describing whether the move is allowed,
                    blocked by border, or blocked by obstacle.
    """
    x, y = game.robot.get_position()
    new_x, new_y = check_next_move(x, y, direction)
    return game.scene.check_if_move_is_allowed(new_x, new_y)


def main() -> None:
    """
    Main entry point of the game.

    Handles:
    - Game initialization
    - User confirmation
    - Game loop
    - Movement processing
    - Win detection
    """
    game = Game()

    starting_announcement()

    while True:
        player_choice = input("Press 'Y' to play or 'N' to exit: ").lower()

        if player_choice in ("y", "n"):
            break
        print("Invalid choice.")

    if player_choice == "n":
        return

    update_screen(game, "Let's go!")

    while True:
        if check_win(game):
            won_announcement(game)
            break

        direction = move_input()
        status = process_move(game, direction)

        if status == MoveStatus.ALLOWED:
            game.apply_move(direction)
            update_screen(game, "Good move :) Keep going!")
        elif status == MoveStatus.BORDER:
            update_screen(game, "Move NOT allowed. You hit the border! Try again.")
        elif status == MoveStatus.OBSTACLE:
            update_screen(game, "Move NOT allowed. You hit an obstacle! Try again.")


if __name__ == "__main__":
    main()
