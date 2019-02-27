from rover.grid import Grid as Area
from rover.rover import Rover, RoverV2
import sys
import pickle

class RoverCommand:
    def __init__(self):
        self.grid = None
        self.rover = None
        self.load_state()

    def run(self):
        while True:
            command = input('Command:')
            command_chunks = command.split(' ')
            if (command_chunks[0] == 'g'):
                self.grid = Area(int(command_chunks[1]), int(command_chunks[2]))
            if (command_chunks[0] == 'r'):
                if (command_chunks[1] == 'n'):
                    self.rover = Rover('R', self.grid)
                if (command_chunks[1] == 'n2'):
                    self.rover = RoverV2('R', self.grid)
                if (command_chunks[1] == 'r'):
                    self.rover.right()
                if (command_chunks[1] == 'l'):
                    self.rover.left()
                if (command_chunks[1] == 'f'):
                    self.rover.forward()
                if (command_chunks[1] == 'b'):
                    self.rover.backward()
            if (command_chunks[0] == 'q'):
                self.save_state()
                sys.exit(0)
            # print (grid)

    def save_state(self):
        with open('rover.txt', 'wb') as rover_file:
            pickle.dump(self.rover, rover_file)
        # rover_file = open('rover.txt', 'wb')
        # pickle.dump(self.rover, rover_file)
        # rover_file.close()
        # grid_file = open('grid.txt', 'wb')
        # pickle.dumps(self.grid, grid_file)
        # grid_file.close()

    def load_state(self):
        with open('rover.txt', 'rb') as rover_file:
            self.rover = pickle.load(rover_file)

        # try:
        #     rover_file = open('rover.txt', 'rb')
        # except FileNotFoundError:
        #     pass
        # else:
        #     self.rover = pickle.load(rover_file)
        #     rover_file.close()
        # try:
        #     grid_file = open('grid.txt', 'rb')
        # except FileNotFoundError:
        #     pass
        # else:
        #     self.grid = pickle.load(grid_file)
        #     grid_file.close()

if __name__ == '__main__':
    RoverCommand().run()