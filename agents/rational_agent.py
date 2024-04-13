class RationalAgent:
    def __init__(self, map, limit):
        self.map = map
        self.initial_position = (0, 0)
        self.position = (0, 0)
        self.position_content = self.map.grid[self.position[0]][self.position[1]]

        self.holding = None
        self.points = 0
        self.limit = limit
        self.countItems = 0

    def left(self):
        self.position = (self.position[0], self.position[1] - 1)
        self.update_position_content()

    def right(self):
        self.position = (self.position[0], self.position[1] + 1)
        self.update_position_content()

    def up(self):
        self.position = (self.position[0] - 1, self.position[1])
        self.update_position_content()

    def down(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.update_position_content()

    def grab_item(self, item):
        self.map.grid[self.position[0]][self.position[1]] = ' '
        self.holding = item

    def drop_item(self):
        self.map.grid[self.position[0]][self.position[1]] = self.holding
        self.holding = None

    def noOp(self):
        pass

    def update_position_content(self):
        self.position_content = self.map.grid[self.position[0]][self.position[1]]

    def back_initial_position(self):
        while self.position[0] != self.initial_position[0]:
            self.up()
        while self.position[1] != self.initial_position[1]:
            self.left()

    def countPoints(self):
        if self.map.grid[self.initial_position[0]][self.initial_position[1]] == '1':
            self.points += 10
            self.countItems += 1
        if self.map.grid[self.initial_position[0]][self.initial_position[1]] == '2':
            self.points += 20
            self.countItems += 1
        self.map.grid[self.initial_position[0]][self.initial_position[1]] = ' '