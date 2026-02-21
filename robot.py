from direction import Direction


class Robot:
    """
    Represents the robot controlled by the player.

    The robot stores its current position on the map and provides
    methods to retrieve its coordinates and move in a given direction.
    """

    START_X = 0
    START_Y = 5

    def __init__(self, start_x: int = START_X, start_y: int = START_Y) -> None:
        """
        Initialize the robot at a given starting position.

        Args:
            start_x (int): Initial x coordinate.
            start_y (int): Initial y coordinate.
        """
        self._x = start_x
        self._y = start_y

    def get_position(self) -> tuple[int, int]:
        """
        Get the current position of the robot.

        Returns:
            tuple[int, int]: Current (x, y) coordinates.
        """
        return self._x, self._y

    def move(self, direction: Direction) -> None:
        """
        Move the robot in the given direction.

        Args:
            direction (Direction): Movement direction enum value.
        """
        dx, dy = Direction.delta(direction)
        self._x += dx
        self._y += dy
