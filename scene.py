class Scene:
    GOAL = "M"
    OBSTACLE = "X"
    EMPTY = " "

    def __init__(self):
        self.map = [
            [" ", " ", " ", " ", "M"],
            [" ", " ", " ", " ", " "],
            [" ", "X", "X", " ", " "],
            [" ", "X", " ", " ", " "],
            [" ", "X", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    def is_goal(self, x, y):
        return self.map[y][x] == self.GOAL

    def obstacle(self, x, y):
        return self.map[y][x] == self.OBSTACLE

    def check_if_move_is_allowed(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return "border"
        elif self.obstacle(x, y):
            return "obstacle"
        else:
            return "move allowed"

    def draw_scene_with_robot(self, robot_x: int, robot_y: int) -> None:
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

