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
            return ' '  # Nothing
        elif x == 1:
            return '█'  # Wall
        elif x == 2:
            return '▒'  # Block
        elif x == 3:
            return '▔'  # Paddle
        elif x == 4:
            return '●'  # Ball

        return str(x)

    def draw():
        os.system('clear')
        print('SCORE:', score)
        mx = max(x for x, y in screen.keys())
        my = max(y for x, y in screen.keys())
        for y in range(my+1):
            print(''.join(tile_char(screen[(x, y)]) for x in range(mx+1)))

    def input():
        while True:
            paddle = None
            ball = None
            for pos, tile in screen.items():
                if tile == 3:
                    paddle, _ = pos
                if tile == 4:
                    ball, _ = pos
            # print(paddle, ball)
            draw()
            if paddle < ball:
                yield 1
            elif paddle > ball:
                yield -1
            else:
                yield 0

    outp = compute(mem, input())

    screen = defaultdict(lambda: 0)
    score = None

    for x in outp:
        y = next(outp)
        tile = next(outp)
        if x == -1 and y == 0:
            score = tile
        else:
            screen[(x, y)] = tile

    draw()


if __name__ == '__main__':
    with open('in13.txt') as f:
        part1(f.read())
    with open('in13.txt') as f:
        play(f.read())
