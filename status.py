from enum import Enum


class MoveStatus(Enum):
    """
    Enumeration representing the possible outcomes of a movement attempt.

    Values:
        ALLOWED:   The move is valid and the robot can proceed.
        BORDER:    The move would go outside the map boundaries.
        OBSTACLE:  The move is blocked by an obstacle on the map.
    """

    ALLOWED: str = "move allowed"
    BORDER: str = "border"
    OBSTACLE: str = "obstacle"
