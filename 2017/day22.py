import enum


class Direction(enum.Enum):
    UP = (lambda x, y: (x, y - 1), '↑')
    LEFT = (lambda x, y: (x - 1, y), '←')
    DOWN = (lambda x, y: (x, y + 1), '↓')
    RIGHT = (lambda x, y: (x + 1, y), '→')

    def __repr__(self):
        return self.value[1]

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)

    def __str__(self):
        return self.__repr__()

    def left(self):
        return _LEFT[self]

    def right(self):
        return _RIGHT[self]

    def __reversed__(self):
        return _REV[self]


_LEFT = {
    Direction.UP: Direction.LEFT,
    Direction.LEFT: Direction.DOWN,
    Direction.DOWN: Direction.RIGHT,
    Direction.RIGHT: Direction.UP,
}
_RIGHT = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}
_REV = {
    Direction.UP: Direction.DOWN,
    Direction.RIGHT: Direction.LEFT,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
}


def parse(data):
    data = data.splitlines()
    n = len(data)//2
    grid = {}
    for y in range(2*n+1):
        for x in range(2*n+1):
            if data[y][x] == '#':
                grid[(x-n, y-n)] = '#'
    return grid, (-n, -n, n, n)


def print_grid(grid, size, carrier, direction):
    for y in range(size[1], size[3] + 1):
        row = []
        for x in range(size[0], size[2] + 1):
            pos = (x, y)
            if pos == carrier:
                row += repr(direction)
            elif pos in grid:
                row += grid[pos]
            else:
                row += '.'
        print(''.join(row))
    print(direction, carrier)


def part1(grid):
    grid, size = parse(grid)
    carrier = (0, 0)
    direction = Direction.UP
    print_grid(grid, size, carrier, direction)

    i = 0
    for loop in range(10000):
        print(loop)
        if carrier in grid:
            direction = direction.right()
            grid.pop(carrier)
        else:
            i += 1
            direction = direction.left()
            grid[carrier] = '#'
        carrier = direction(*carrier)
        size = (min(size[0], carrier[0]), min(size[1], carrier[1]),
                max(size[2], carrier[0]), max(size[3], carrier[1]))

    print_grid(grid, size, carrier, direction)
    return i


def part2(grid):
    grid, size = parse(grid)
    carrier = (0, 0)
    direction = Direction.UP
    print_grid(grid, size, carrier, direction)

    i = 0
    for loop in range(10000000):
        if loop % 1000 == 0:
            print(loop)
        if carrier not in grid:
            direction = direction.left()
            grid[carrier] = 'W'
        else:
            state = grid[carrier]
            if state == 'W':
                grid[carrier] = '#'
                i += 1
            elif state == '#':
                grid[carrier] = 'F'
                direction = direction.right()
            elif state == 'F':
                grid.pop(carrier)
                direction = reversed(direction)

        carrier = direction(*carrier)
        size = (min(size[0], carrier[0]), min(size[1], carrier[1]),
                max(size[2], carrier[0]), max(size[3], carrier[1]))

    print_grid(grid, size, carrier, direction)
    return i


if __name__ == '__main__':
    example_data = r'''..#
#..
...'''
    print("example1:", part1(example_data))
    print("example2:", part2(example_data))
    input_data = r'''....##.#.#.#...#.##.##.#.
##.####..###..#.#.#.###.#
.#.#...#.##....#......###
...#.....##.###....##.###
#.########.#.#####..##.#.
.#..#..#.#..#....##.#...#
.....#.##..#.#.....##..##
....###....###....###.#..
..#..#..#..#.##.#.#..##.#
.##......#...##.#.#.##.#.
.#####.#.#.##...###...#..
#..###..#....#....##..#..
###..#....#.##.##.....#..
##.##..#.##.#..#####.#.#.
#....#.######.#.#.#.##.#.
###.##.#.######.#..###.#.
#...###.#.#..##..####....
###...##.###..###..##..#.
..##.###...#.....##.##.##
..##..#.###.###.....#.###
#..###.##.#.###......####
#.#...#..##.###.....##.#.
#..#.##...##.##....#...#.
..#.#..#..#...##.#..###..
......###....#.....#....#'''
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))
