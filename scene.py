from status import MoveStatus


class Scene:
    """
    Represents the game map, including obstacles, borders, and the goal tile.

    The Scene class stores the map layout as a 2D list of characters.
    It provides methods for:
    - drawing the scene with the robot,
    - checking whether a move is allowed,
    - detecting the goal tile.
    """

    def __init__(self, map_data: list[list[str]]) -> None:
        """
        Initialize the scene with externally provided map data.

        Args:
            map_data (list[list[str]]): 2D list representing the map layout.
        """
        self.map: list[list[str]] = map_data
        self.height: int = len(map_data)
        self.width: int = len(map_data[0]) if self.height > 0 else 0

    @classmethod
    def from_file(cls, path: str) -> "Scene":
        """
        Load a map from a text file and create a Scene instance.

        Each line in the file becomes one row of the map.
        Each character becomes one tile.

        Args:
            path (str): Path to the map file.

        Returns:
            Scene: A new Scene instance based on the file contents.
        """

        with open(path, "r") as f:
            raw = [list(line.rstrip("\n")) for line in f]

        return cls(raw)

    def draw_scene_with_robot(self, robot_x: int, robot_y: int) -> None:
        """
        Print the map to the console with the robot drawn at the given position.

        Args:
            robot_x (int): Robot's x coordinate.
            robot_y (int): Robot's y coordinate.
        """
        for y, row in enumerate(self.map):
            line = ""
            for x, tile in enumerate(row):
                if x == robot_x and y == robot_y:
                    line += "R"
                else:
                    line += tile
            print(line)

    def is_goal(self, x: int, y: int) -> bool:
        """
        Check whether the given coordinates contain the goal tile.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            bool: True if the tile is the goal ('M'), otherwise False.
        """
        return self.map[y][x] == "M"

    def check_if_move_is_allowed(self, x: int, y: int) -> MoveStatus:
        """
        Determine whether the robot can move onto the tile at the given coordinates.

        This method validates a potential move by checking:
        - whether the target coordinates are inside the map boundaries,
        - whether the tile is part of the outer frame ('.' or '|'),
        - whether the tile is an obstacle ('X'),
        - whether the tile is free space (' ') or the goal ('M').

        Movement rules:
        - Moving outside the map returns MoveStatus.BORDER.
        - Moving onto '.' or '|' (outer frame) returns MoveStatus.BORDER.
        - Moving onto 'X' returns MoveStatus.OBSTACLE.
        - Moving onto ' ' or 'M' returns MoveStatus.ALLOWED.

        Args:
            x (int): Target X coordinate.
            y (int): Target Y coordinate.

        Returns:
            MoveStatus: Result describing whether the move is allowed, blocked by
                        an obstacle, or hits the map border.
        """

        # Border of the map (outside array)
        if x < 0 or y < 0 or y >= self.height or x >= self.width:
            return MoveStatus.BORDER

        tile = self.map[y][x]

        # Outer frame (.|)
        if tile in (".", "|"):
            return MoveStatus.BORDER

        # Obstacles
        if tile == "X":
            return MoveStatus.OBSTACLE

        # Free space or goal
        return MoveStatus.ALLOWED
