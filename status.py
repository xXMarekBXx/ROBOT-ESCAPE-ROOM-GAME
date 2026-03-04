from enum import Enum


class MoveStatus(Enum):
    """
    Enumeration representing the possible outcomes of a movement attempt.

    Values:
        ALLOWED:   The move is valid and the robot can proceed.
        BORDER:    The move would go outside the map boundaries.
        OBSTACLE:  The move is blocked by an obstacle on the map.
    """

    ALLOWED = "move allowed"
    BORDER = "border"
    OBSTACLE = "obstacle"

    def is_blocked(self) -> bool:
        """
        Check whether the movement result indicates a blocked move.

        Returns:
            bool: True if the move is blocked (obstacle or border), False otherwise.
        """
        return self in (MoveStatus.BORDER, MoveStatus.OBSTACLE)

    def message(self) -> str:
        """
        Provide a human-readable message describing why the move was blocked.

        Returns:
            str: Explanation of the movement failure.
        """
        if self == MoveStatus.OBSTACLE:
            return "You hit an obstacle!"
        if self == MoveStatus.BORDER:
            return "You hit the border!"
        return ""
