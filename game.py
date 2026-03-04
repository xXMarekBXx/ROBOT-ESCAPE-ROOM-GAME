from robot import Robot
from scene import Scene
from direction import Direction
from status import MoveStatus
from config import MAP_FILE


class Game:
    """
    Core game controller that manages the robot, the scene, and the move counter.

    The Game class encapsulates the entire game state:
    - the robot and its position,
    - the scene (map layout, obstacles, goal),
    - the number of moves made by the player.

    It provides methods for validating and applying moves, updating the game
    state, and checking win conditions.
    """

    def __init__(self) -> None:
        """
        Initialize the game with a robot, a scene loaded from file,
        and a move counter set to zero.
        """
        self.robot: Robot = Robot()
        self.scene = Scene.from_file(MAP_FILE)
        self.moves: int = 0

    def apply_move(self, direction: Direction) -> None:
        """
        Apply a movement command to the robot and increment the move counter.

        This method assumes the move has already been validated by the scene.
        It does not check for borders or obstacles.

        Args:
            direction (Direction): Movement direction.
        """
        self.robot.move(direction)
        self.moves += 1

    def check_win(self) -> bool:
        """
        Check whether the robot has reached the goal tile.

        Returns:
            bool: True if the robot's current position matches the goal
                  location defined in the scene, otherwise False.
        """
        x, y = self.robot.get_position()
        return self.scene.is_goal(x, y)

    def process_move(self, direction: Direction) -> MoveStatus:
        """
        Validate and apply a movement attempt in the given direction.

        This method:
        - computes the next coordinates based on the robot's current position,
        - checks whether the move is allowed by the scene (walls, borders, etc.),
        - applies the move and increments the move counter if allowed.

        Args:
            direction (Direction): Direction in which the robot intends to move.

        Returns:
            MoveStatus: Result of the attempted move (allowed, blocked, border).
        """
        dx, dy = Direction.delta(direction)
        x, y = self.robot.get_position()
        new_x, new_y = x + dx, y + dy

        status = self.scene.check_if_move_is_allowed(new_x, new_y)

        if status == MoveStatus.ALLOWED:
            self.apply_move(direction)

        return status
