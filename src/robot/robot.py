from argparse import ArgumentParser
import re

# Constants
DIRECTIONS = ('EAST', 'SOUTH', 'WEST', 'NORTH')
MOVES = ((1, 0), (0, -1), (-1, 0), (0, 1))
COMMANDS = {'MOVE', 'LEFT', 'RIGHT', 'REPORT'}
BOUNDARY = 5


class Robot:
    def __init__(self, verbose=False):
        self.position_x = None
        self.position_y = None
        self.facing = None
        self.is_placed = False
        self.verbose = verbose
        self.methods = {'PLACE': self.place, 'MOVE': self.move, 'LEFT': self.turn_left,
                        'RIGHT': self.turn_right, 'REPORT': self.report}

    @staticmethod
    def is_valid_position(x, y):
        if type(x) == int and type(y) == int:
            if 0 <= x < BOUNDARY and 0 <= y < BOUNDARY:
                return True
        return False

    @staticmethod
    def is_valid_direction(facing):
        if facing in DIRECTIONS:
            return True
        return False

    @staticmethod
    def is_valid_command(command):
        if command in COMMANDS:
            return True
        # check if it's a place command.
        search_obj = re.search(r'PLACE\s+(\d+)\s*,\s*(\d+)\s*,\s*([A-Z]+)', command)
        if search_obj:
            return True
        return False

    def execute(self, command):
        if self.is_valid_command(command):
            # check if it's a place command.
            search_obj = re.search(r'PLACE\s+(\d+)\s*,\s*(\d+)\s*,\s*([A-Z]+)', command)
            if search_obj:
                x = int(search_obj.group(1))
                y = int(search_obj.group(2))
                facing = search_obj.group(3)
                return self.methods['PLACE'](x, y, facing)

            else:
                return self.methods[command]()
        else:
            if self.verbose:
                print('Please enter a valid command.')
            return False

    def place(self, x, y, facing):
        if self.is_valid_position(x, y) and self.is_valid_direction(facing):
            self.position_x = x
            self.position_y = y
            self.facing = DIRECTIONS.index(facing)
            self.is_placed = True
            return self.position_x, self.position_y, facing
        if self.verbose:
            print("You entered a wrong position or a direction.")
        return None

    def report(self):
        if self.is_placed:
            message = f'{self.position_x},{self.position_y},{DIRECTIONS[self.facing]}'
            if self.verbose:
                print(message)
            return message
        else:
            if self.verbose:
                print("Can't report the status of the robot because the Robot is not placed yet.")
            return ""

    def turn_left(self):
        if self.is_placed:
            self.facing = (self.facing - 1) % 4
            return DIRECTIONS[self.facing]
        else:
            if self.verbose:
                print("Can't turn left because the Robot is not placed yet.")
            return None

    def turn_right(self):
        if self.is_placed:
            self.facing = (self.facing + 1) % 4
            return DIRECTIONS[self.facing]
        else:
            if self.verbose:
                print("Can't turn right because Robot is not placed yet.")
            return None

    def move(self):
        if self.is_placed:
            new_position_x = self.position_x + MOVES[self.facing][0]
            new_position_y = self.position_y + MOVES[self.facing][1]
            if self.is_valid_position(new_position_x, new_position_y):
                self.position_x = new_position_x
                self.position_y = new_position_y
            return self.position_x, self.position_y
        else:
            if self.verbose:
                print("Can't not move the robot because the Robot is not placed yet.")
            return None


def main():
    parser = ArgumentParser()
    robot = Robot(verbose=True)
    parser.add_argument('-f', '--file', type=str, help='-f [filename]')
    args = parser.parse_args()

    if not args.file:
        while True:
            command = input("Please enter your command: ")
            robot.execute(command)
    else:
        with open(args.file, 'r') as f:
            commands = f.read().splitlines()
            # change verbose to False when use a file as input.
            robot.verbose = False
            for command in commands:
                if len(command) > 0:
                    res = robot.execute(command)
                    if command == "REPORT":
                        print(res)


if __name__ == "__main__":
    main()
