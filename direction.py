from enum import Enum


class Direction(Enum):
    """
    Represents movement directions available in the game.

    Each direction corresponds to:
    - a keyboard key ('w', 's', 'a', 'd'),
    - a movement on the grid expressed as a coordinate delta (dx, dy),
      where dx and dy are integers forming a tuple[int, int].
    """

    UP: str = "w"
    DOWN: str = "s"
    LEFT: str = "a"
    RIGHT: str = "d"

    @staticmethod
    def key_to_direction(key: str) -> "Direction | None":
        """
        Convert a keyboard key into a Direction enum member.

        Args:
            key (str): Pressed key, e.g. 'w', 'a', 's', 'd'.

        Returns:
            Direction | None:
                - Direction enum value matching the key,
                - None if the key does not correspond to any direction.
        """
        mapping: dict[str, Direction] = {
            "w": Direction.UP,
            "s": Direction.DOWN,
            "a": Direction.LEFT,
            "d": Direction.RIGHT,
        }
        return mapping.get(key)

    @staticmethod
    def delta(direction: "Direction") -> tuple[int, int]:
        """
        Convert a Direction enum value into a coordinate delta.

        Args:
            direction (Direction): One of the Direction enum values.

        Returns:
            tuple[int, int]:
                A pair (dx, dy) representing movement on the grid:
                - UP    → (0, -1)
                - DOWN  → (0, 1)
                - LEFT  → (-1, 0)
                - RIGHT → (1, 0)
        """
        deltas: dict[Direction, tuple[int, int]] = {
            Direction.UP: (0, -1),
            Direction.DOWN: (0, 1),
            Direction.LEFT: (-1, 0),
            Direction.RIGHT: (1, 0),
        }
        return deltas[direction]
