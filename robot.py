class Robot:
    def __init__(self):
        self.x = 0   # column
        self.y = 5   # row

    def get_robot_possition(self):
        return self.x, self.y

    def set_robot_possition(self, move):
        if move == "w":
            self.y -= 1
        elif move == "s":
            self.y += 1
        elif move == "a":
            self.x -= 1
        elif move == "d":
            self.x += 1
        return self.x, self.y
