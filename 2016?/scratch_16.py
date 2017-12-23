
input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

from enum import Enum, unique

@unique
class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def turn(self, to):
        if to == 'L':
            if self == Dir.N: return Dir.W
            if self == Dir.E: return Dir.N
            if self == Dir.S: return Dir.E
            if self == Dir.W: return Dir.S
        else:
            if self == Dir.N: return Dir.E
            if self == Dir.E: return Dir.S
            if self == Dir.S: return Dir.W
            if self == Dir.W: return Dir.N

    def move(self, to):
        global x, y, locations
        to = int(to)
        if self == Dir.N:
            for yy in range(y, y + to):
                location(x, yy)
            y += to
        elif self == Dir.E:
            for xx in range(x, x + to):
                location(xx, y)
            x += to
        elif self == Dir.S:
            for yy in range(y, y - to, -1):
                location(x, yy)
            y -= to
        elif self == Dir.W:
            for xx in range(x, x - to, -1):
                location(xx, y)
            x -= to

direction = Dir.N
x = 0
y = 0

locations = []

def location(x, y):
    # print(x, y)
    if (x, y) in locations:
        print("LOCATION: ", (x, y), x+y)
    locations.append((x, y))

for instr in input.split(", "):
    direction = direction.turn(instr[0])
    direction.move(instr[1:])
    # location(x, y)

print (x, y)
print(x+y)