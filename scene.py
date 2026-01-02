class Scene:
    map = [[" ", " ", " ", " ", "M"],
           [" ", " ", " ", " ", " "],
           [" ", "X", "X", " ", " "],
           [" ", "X", " ", " ", " "],
           [" ", "X", " ", " ", " "],
           [" ", " ", " ", " ", " "]]

    def is_goal(self, x, y):
        return self.map[y][x] == "M"

    def obstacle(self, x, y):
        return self.map[y][x] == "X"

    def check_if_move_is_allowed(self, x, y):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
            return "border"
        elif self.obstacle(x,y):
            return "obstacle"
        else:
            return "move allowed"

    def draw_scene_with_robot(self, robot_x, robot_y):
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
