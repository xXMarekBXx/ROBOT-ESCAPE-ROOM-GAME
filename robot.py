class Robot:
    def __init__(self):
        self.x = 0   # column
        self.y = 5   # row
        self.moves = 0 #how many moves

    def get_robot_possition(self):
        return self.x, self.y

    def set_robot_possition(self, move):
        self.moves += 1

        if move == "w":
            self.y -= 1
        elif move == "s":
            self.y += 1
        elif move == "a":
            self.x -= 1
        elif move == "d":
            self.x += 1
        return self.x, self.y
