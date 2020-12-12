import math

def parse(filename):
    with open(filename, "r") as f:
        instr = [ x.replace("\n", "") for x in f if x != "\n" ]
    return instr


class Boat:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def run(self, instructions):
        for instr in instructions:
            c, value = self.parse_instr(instr)
            if c == "F":
                self.forward(value)
            elif c == "R":
                self.right(value)
            elif c == "L":
                self.left(value)
            elif c == "N":
                self.north(value)
            elif c == "S":
                self.south(value)
            elif c == "E":
                self.east(value)
            elif c == "W":
                self.west(value)
            else:
                print(f"Instruction inconnue : {c}")

    def reset(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def north(self, value):
        self.y += value

    def south(self, value):
        self.y -= value

    def east(self, value):
        self.x += value

    def west(self, value):
        self.x -= value

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle

    def forward(self, value):
        angle = math.radians(self.angle)
        self.x += math.cos(angle) * value
        self.y += math.sin(angle) * value

    @staticmethod
    def parse_instr(instr):
        return (instr[0], int(instr[1:]))

    def print_infos(self):
        print(f"Boat({self.x}, {self.y}, {self.angle})")
        manhattan = abs(self.x) + abs(self.y)
        print(f"Manhattan distance {manhattan}")

class BestBoat(Boat):
    def __init__(self):
        Boat.__init__(self)
        self.wx = 10
        self.wy = 1

    def reset(self):
        Boat.reset(self)
        self.wx = 10
        self.wy = 1

    def north(self, value):
        self.wy += value

    def south(self, value):
        self.wy -= value

    def east(self, value):
        self.wx += value

    def west(self, value):
        self.wx -= value

    def forward(self, value):
        self.y += self.wy * value
        self.x += self.wx * value

    def left(self, angle):
        if angle == 90:
            tmp = self.wy
            self.wy = self.wx
            self.wx = -tmp
        elif angle == 180:
            self.wx *= -1
            self.wy *= -1
        elif angle == 270:
            tmp = self.wy
            self.wy = -self.wx
            self.wx = tmp
        else:
            pass

    def right(self, angle):
        self.left(360-angle)

    def print_infos(self):
        print(f"BestBoat({self.x}, {self.y})")
        manhattan = abs(self.x) + abs(self.y)
        print(f"Manhattan distance {manhattan}")

# Part 1
instructions = parse("data_test")
boat = Boat()
boat.run(instructions)
boat.print_infos()

# Part 2
best_boat = BestBoat()
best_boat.run(instructions)
best_boat.print_infos()
