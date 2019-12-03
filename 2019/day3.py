import itertools


def dist(x, y):
    return abs(x) + abs(y)


def get_points(instructions):
    x, y, s = 0, 0, 0
    path = {}
    for code in instructions:
        direction = code[0]
        for _ in range(int(code[1:])):
            if direction == 'D':
                y -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            s += 1
            if (x, y) not in path:
                path[(x, y)] = s
    return path


def print_wire(wire1, wire2):
    max_x = max(itertools.chain(wire1, wire2), key=lambda x: x[0])[0] + 1
    min_x = min(itertools.chain(wire1, wire2), key=lambda x: x[0])[0] - 1
    max_y = max(itertools.chain(wire1, wire2), key=lambda x: x[1])[1] + 1
    min_y = min(itertools.chain(wire1, wire2), key=lambda x: x[1])[1] - 1

    def char(x, y):
        if x == 0 and y == 0:
            return 'O'
        if (x, y) in wire1 and (x, y) in wire2:
            return '#'
        if (x, y) in wire1:
            return '1'
        if (x, y) in wire2:
            return '2'
        return '.'

    for y in range(max_y, min_y-1, -1):
        print(*(char(x, y) for x in range(min_x, max_x+1)), sep='')


def part1(wire1, wire2):
    wire1 = get_points(wire1.split(','))
    wire2 = get_points(wire2.split(','))
    overlap = wire1.keys() & wire2.keys()
    # print(overlap)
    # print_wire(wire1, wire2)
    minimal_dist = min(dist(x, y) for x, y in overlap)
    print('min dist:', minimal_dist)
    return minimal_dist


def part2(wire1, wire2):
    wire1 = get_points(wire1.split(','))
    wire2 = get_points(wire2.split(','))
    overlap = wire1.keys() & wire2.keys()
    # print_wire(wire1, wire2)

    def calc(x, y):
        return wire1[(x, y)] + wire2[(x, y)]

    shortest = min(calc(x, y) for x, y in overlap)
    print('shortest', shortest)
    return shortest


if __name__ == '__main__':
    assert part1('R8,U5,L5,D3', 'U7,R6,D4,L4') == 6
    assert part1('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 159
    assert part1('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135
    with open('in3.txt') as f:
        print(part1(f.readline(), f.readline()))
    assert part2('R8,U5,L5,D3', 'U7,R6,D4,L4') == 30
    assert part2('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 610
    assert part2('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 410
    with open('in3.txt') as f:
        print(part2(f.readline(), f.readline()))
