class Rover:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.step = 1
        self.x, self.y = 0, 0
        self._register_rover_position()

    def __str__(self):
        return self.name

    def left(self):
        self.x -= self.step
        self._register_rover_position()

    def right(self):
        self.x += self.step
        self._register_rover_position()

    def forward(self):
        self.y += self.step
        self._register_rover_position()

    def backward(self):
        self.y -= self.step
        self._register_rover_position()

    def _register_rover_position(self):
        self.grid.position_rover(self)

class RoverV2(Rover):
    def __init__(self, name, grid):
        Rover.__init__(self, name, grid)
        self.step = 2