from status import MoveStatus


class Scene:
    """
    Represents the game map, including obstacles, empty spaces, and the goal.

    The Scene class stores the layout of the map and provides methods for:
    - checking borders,
    - detecting obstacles,
    - detecting the goal,
    - validating moves,
    - drawing the map with the robot.
    """

    GOAL = "M"
    OBSTACLE = "X"
    EMPTY = " "

    def __init__(self) -> None:
        """
        Initialize the scene with a predefined map layout.

        The map is a 2D grid represented as a list of lists,
        where each cell contains:
        - " " for empty space,
        - "X" for obstacle,
        - "M" for the goal.
        """
        self.map: list[list[str]] = [
            [" ", " ", " ", " ", "M"],
            [" ", " ", " ", " ", " "],
            [" ", "X", "X", " ", " "],
            [" ", "X", " ", " ", " "],
            [" ", "X", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        self._validate_map()

    def _validate_map(self) -> None:
        """
        Validate the structure and correctness of the map.

        Ensures:
        - all rows have the same length (rectangular grid),
        - the map contains at least one goal tile.

        Raises:
            ValueError: If the map is malformed or missing a goal.
        """
        if len(set(len(row) for row in self.map)) > 1:
            raise ValueError("All rows must have the same length")

        if not any(self.GOAL in row for row in self.map):
            raise ValueError("Map must contain a goal")

    @property
    def width(self) -> int:
        """
        Get the width of the map (number of columns).

        Returns:
            int: Width of the map.
        """
        return len(self.map[0])

    @property
    def height(self) -> int:
        """
        Get the height of the map (number of rows).

        Returns:
            int: Height of the map.
        """
        return len(self.map)

    def is_goal(self, x: int, y: int) -> bool:
        """
        Check whether the given coordinates contain the goal tile.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            bool: True if the tile is the goal, otherwise False.
        """
        return self.map[y][x] == self.GOAL

    def obstacle(self, x: int, y: int) -> bool:
        """
        Check whether the given coordinates contain an obstacle.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            bool: True if the tile is an obstacle, otherwise False.
        """
        return self.map[y][x] == self.OBSTACLE

    def check_if_move_is_allowed(self, x: int, y: int) -> MoveStatus:
        """
        Determine whether a move to the given coordinates is allowed.

        A move is considered:
        - BORDER if it goes outside the map,
        - OBSTACLE if it hits an obstacle,
        - ALLOWED otherwise.

        Args:
            x (int): Target x coordinate.
            y (int): Target y coordinate.

        Returns:
            MoveStatus: Status describing the result of the attempted move.
        """
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return MoveStatus.BORDER
        elif self.obstacle(x, y):
            return MoveStatus.OBSTACLE
        else:
            return MoveStatus.ALLOWED

    def draw_scene_with_robot(self, robot_x: int, robot_y: int) -> None:
        """
        Print the map to the console with the robot drawn at the given position.

        Args:
            robot_x (int): Robot's x coordinate.
            robot_y (int): Robot's y coordinate.

        Notes:
            The robot is displayed as 'R'.
            The map is surrounded by horizontal separators for readability.
        """
        print("-----------")
        for y, row in enumerate(self.map):
            line = "|"
            for x, cell in enumerate(row):
                if x == robot_x and y == robot_y:
                    line += "R|"
                else:
                    line += cell + "|"
            print(line)
            print("-----------")
