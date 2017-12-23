"""
(0,0) is origin
"""
import collections

DIR_NAMES = ('→', '↑', '←', '↓')
DIRS = (
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
)


def get_coords(count):
    x, y = 0, 0
    dir = 0  # Direction of movement
    dir_moves = 1  # Moves to go in this direction
    dir_moves_count = 1  # Keep original dir_moves, so it can be incremented every 2nd dir change
    for i in range(1, count):
        x, y = DIRS[dir](x, y)
        # print(i + 1, DIR_NAMES[dir], (x, y))
        dir_moves -= 1
        if dir_moves == 0:
            dir = (dir + 1) % 4  # loop over all directions
            if dir % 2 == 0:  # Every second turn, the distance will be +1
                dir_moves_count += 1
            dir_moves = dir_moves_count
    return x, y


def part1(data):
    x, y = get_coords(data)
    return abs(x) + abs(y)


def part2(data):
    values = collections.defaultdict(lambda: 0)
    x, y = 0, 0
    dir = 0  # Direction of movement
    dir_moves = 1  # Moves to go in this direction
    dir_moves_count = 1  # Keep original dir_moves, so it can be incremented every 2nd dir change
    i = 0
    values[(0, 0)] = 1  # Seed origin
    while True:
        i += 1
        x, y = DIRS[dir](x, y)

        #  Value for X, Y is sum of all neighbors, with defaultdict it's OK that it requests empty positions or itself.
        values[(x, y)] = sum(values[(x + dx, y + dy)] for dx in range(-1, 2) for dy in range(-1, 2))

        #  Target
        if values[(x, y)] > data:
            return values[(x, y)]

        # print(i + 1, DIR_NAMES[dir], (x, y), values[(x, y)])

        # Same move logic as part 1.
        dir_moves -= 1
        if dir_moves == 0:
            dir = (dir + 1) % 4
            if dir % 2 == 0:
                dir_moves_count += 1
            dir_moves = dir_moves_count


if __name__ == '__main__':
    # print("Example 1 (0):", part1(1))
    # print("Example 12 (3):", part1(12))
    # print("Example 23 (2):", part1(23))
    # print("Example 1024 (31):", part1(1024))

    input_data = 289326
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))

