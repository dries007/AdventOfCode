import itertools
import math


example = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def part1(inp, slope=(3, 1)):
    x, y = 0, 0
    field = [[x for x in line] for line in inp.splitlines()]
    trees = []
    while y < len(field):
        trees.append(field[y][x % len(field[y])])
        x += slope[0]
        y += slope[1]
    return trees.count('#')


def part2(inp):
    trees = [
        part1(inp, slope=(1, 1)),
        part1(inp, slope=(3, 1)),
        part1(inp, slope=(5, 1)),
        part1(inp, slope=(7, 1)),
        part1(inp, slope=(1, 2)),
    ]
    return math.prod(trees)


def _main():
    assert part1(example) == 7
    assert part2(example) == 336
    print(part1(open('in3.txt').read()))
    print(part2(open('in3.txt').read()))


if __name__ == '__main__':
    _main()
