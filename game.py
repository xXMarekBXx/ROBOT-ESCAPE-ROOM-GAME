from robot import Robot
from scene import Scene
from direction import Direction


class Game:
    """
    Core game controller that manages the robot, the scene, and the move counter.

    The Game class encapsulates the entire game state:
    - the robot and its position,
    - the scene (map layout, obstacles, goal),
    - the number of moves made by the player.

    It provides methods for applying moves and updating the game state.
    """

    def __init__(self) -> None:
        """
        Initialize the game with a robot, a scene, and a move counter.
        """
        self.robot: Robot = Robot()
        self.scene: Scene = Scene()
        self.moves: int = 0

    def apply_move(self, direction: Direction) -> None:
        """
        Apply a movement command to the robot and increment the move counter.

        Args:
            direction (Direction): Movement direction ('w', 'a', 's', 'd').

        Notes:
            This method assumes the move has already been validated.
            It does not check for borders or obstacles.
        """
        self.robot.move(direction)
        self.moves += 1
