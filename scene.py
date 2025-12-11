class Scene:
    map = [[" ", " ", " ", " ", "M"],
           [" ", " ", " ", " ", " "],
           [" ", "X", "X", " ", " "],
           [" ", "X", " ", " ", " "],
           [" ", "X", " ", " ", " "],
           [" ", " ", " ", " ", " "]]

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
