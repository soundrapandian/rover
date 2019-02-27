class Grid:
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.grid = [[None] * cols] * rows

    def __str__(self):
        return str(self.grid)

    def position_rover(self, rover):
        print (rover.name, rover.x, rover.y, self.cols, self.rows)
        # if not (0 <= rover.x < self.cols or 
        #         0 <= rover.y < self.rows):
        #     raise Exception("Invalid")



