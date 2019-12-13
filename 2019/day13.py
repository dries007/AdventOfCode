import os
from collections import defaultdict

from day9 import compute, GrowingList


def part1(inp):

    def input():
        pass

    outp = compute(GrowingList(int(x) for x in inp.split(',')), input)

    screen = defaultdict(lambda: 0)

    for x in outp:
        y = next(outp)
        tile = next(outp)
        screen[(x, y)] = tile

    print(sum(1 for v in screen.values() if v == 2))


def play(inp):

    mem = GrowingList(int(x) for x in inp.split(','))
    mem[0] = 2

    def tile_char(x):
        if x == 0:
            return ' '
        elif x == 1:
            return '#'
        elif x == 2:
            return '+'
        elif x == 3:
            return '-'
        elif x == 4:
            return '.'

        return str(x)

    def draw():
        mx = max(x for x, y in screen.keys())
        my = max(y for x, y in screen.keys())
        for y in range(my):
            print(''.join(tile_char(screen[(x, y)]) for x in range(mx)))

    def input():
        while True:
            draw()
            yield 0

    outp = compute(mem, input())

    screen = defaultdict(lambda: 0)

    for x in outp:
        y = next(outp)
        tile = next(outp)
        screen[(x, y)] = tile


if __name__ == '__main__':
    with open('in13.txt') as f:
        part1(f.read())
    with open('in13.txt') as f:
        play(f.read())
