class Robot:
    START_X = 0
    START_Y = 5

    def __init__(self, start_x: int = START_X, start_y: int = START_Y):
        self._x = start_x
        self._y = start_y

    def get_position(self) -> tuple[int, int]:
        return self._x, self._y

    def move(self, direction: str) -> None:
        """Move robot in given direction (w/a/s/d)."""
        moves = {
            'w': (0, -1),
            's': (0, 1),
            'a': (-1, 0),
            'd': (1, 0)
        }
        if direction in moves:
            dx, dy = moves[direction]
            self._x += dx
            self._y += dy
