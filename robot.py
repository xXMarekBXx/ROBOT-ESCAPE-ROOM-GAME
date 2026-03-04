from direction import Direction
from config import ROBOT_START_X, ROBOT_START_Y


class Robot:
    """
    Represents the robot controlled by the player.

    The robot stores its current position on the map and provides methods
    to retrieve its coordinates and move in a given direction. The starting
    position is configurable and loaded from the global configuration file.
    """

    def __init__(self, start_x: int = ROBOT_START_X, start_y: int = ROBOT_START_Y) -> None:
        """
        Initialize the robot at a given starting position.

        Args:
            start_x (int): Initial x coordinate of the robot.
            start_y (int): Initial y coordinate of the robot.
        """
        self._x = start_x
        self._y = start_y

    def get_position(self) -> tuple[int, int]:
        """
        Get the current position of the robot.

        Returns:
            tuple[int, int]: Current (x, y) coordinates of the robot.
        """
        return self._x, self._y

    def move(self, direction: Direction) -> None:
        """
        Move the robot in the given direction.

        The movement is based on the delta values defined in the Direction enum.
        This method does not perform any validation — it simply updates the
        robot's coordinates.

        Args:
            direction (Direction): Movement direction enum value.
        """
        dx, dy = Direction.delta(direction)
        self._x += dx
        self._y += dy
