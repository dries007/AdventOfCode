import math
import string
from pprint import pprint


example1 = '''.#..#
.....
#####
....#
...##'''

example2 = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''

example3 = '''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''

example4 = '''.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..'''

example5 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''

example6 = '''.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.........###..
..#.#.....#....##'''


def parse_asteroids(inp):
    asteroids = set()
    for y, row in enumerate(inp.strip().splitlines()):
        for x, char in enumerate(row.strip()):
            if char == '.':
                continue
            asteroids.add((x, y))
    return asteroids, x+1, y+1


def distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x * x + y * y)


def is_visible_from(target, pos, asteroids):
    obstructions = asteroids - {target, pos}
    # Round 5 because fuck floats...
    d = round(distance(target, pos), 5)
    for x in obstructions:
        if round(distance(target, x) + distance(x, pos), 5) == d:
            # print(f'{pos=}->{target=} obstructed by {x}.')
            return False
    # print(f'{pos=}->{target=} visible.')
    return True

    # return not any(distance(target, x) + distance(x, pos) == d for x in obstructions)


def draw(width, height, data, asteroids):
    for y in range(height):
        for x in range(width):
            if (x, y) in data:
                print(data[(x, y)], end='')
            elif (x, y) in asteroids:
                print('+', end='')
            else:
                print(' ', end='')
        print()


def part1(inp):
    asteroids, width, height = parse_asteroids(inp)
    # print(asteroids)
    data = {pos: sum(is_visible_from(target, pos, asteroids) for target in asteroids if target != pos) for pos in asteroids}
    # pprint(data)
    # draw(width, height, data)
    best = max(data, key=lambda x: data[x])
    print(best, data[best])
    return best


def cast_ray(asteroids, w, h, pos, a):
    obstructions = asteroids - {pos}
    x, y = pos[0], pos[1]
    dx = math.sin(a) * 0.01
    dy = math.cos(a) * 0.01
    # print(f'lazer {a=}')
    while True:
        rx, ry = round(x, 3), round(y, 3)
        if (rx, ry) in obstructions:
            return rx, ry
        if x < 0 or y < 0 or x > w or y > h:
            break
        x = x + dx
        y = y - dy


def part2(inp, pos):
    asteroids, width, height = parse_asteroids(inp)
    data = {pos: '%'}
    a = 0
    i = 0
    while i < 10 and a < 2 * math.tau:
        zap = cast_ray(asteroids, width, height, pos, a)
        if zap:
            print(f'ZAP! {zap=} {a=} {i=}')
            asteroids.remove(zap)
            i += 1
            data[zap] = i
        a += math.tau/36000
    draw(width, height, data, asteroids)


if __name__ == '__main__':
    # part1(example1)
    # part1(example2)
    # part1(example3)
    # part1(example4)
    # part1(example5)
    # with open('in10.txt') as f:
    #     part1(f.read())

    part2(example6, (8, 3))
    # part2(example5, (11, 13))
    # with open('in10.txt') as f:
    #     part2(f.read(), (25, 31))
