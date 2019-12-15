import itertools
from collections import defaultdict

from day9 import compute, GrowingList
import sys, tty, termios


full_maze = ''' ▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓ 
▓···········▓·······▓·················▓·▓
 ▓▓·▓▓▓▓▓▓▓·▓·▓▓▓▓▓·▓·▓▓▓·▓▓▓▓▓▓▓▓▓▓▓·▓·▓
▓···▓···▓···▓···▓···▓·▓···▓···········▓·▓
▓·▓▓▓·▓·▓▓▓·▓▓▓·▓▓▓·▓▓▓·▓▓▓·▓▓▓▓▓▓▓▓▓▓▓·▓
▓·····▓···▓···▓···▓·····▓·▓·▓···········▓
▓·▓▓▓▓ ▓▓·▓▓▓·▓·▓·▓▓▓▓▓▓▓·▓·▓·▓▓▓▓▓·▓▓▓·▓
▓·····▓·▓·▓···▓·▓···▓···▓···▓···▓···▓·▓·▓
 ▓▓▓▓·▓·▓·▓▓▓·▓·▓▓▓·▓·▓·▓·▓▓▓▓▓▓▓·▓▓▓·▓·▓
▓···▓·▓·▓···▓·▓···▓·▓·▓·▓·▓·····▓·▓···▓·▓
 ▓▓·▓·▓·▓▓▓·▓·▓▓▓▓▓·▓·▓·▓·▓·▓▓▓·▓·▓·▓▓▓·▓
▓···▓·▓···▓·▓·▓·····▓·▓·▓·▓···▓···▓·▓···▓
▓·▓·▓·▓▓▓·▓·▓·▓·▓▓▓▓▓▓▓·▓·▓▓▓·▓▓▓▓▓·▓·▓▓ 
▓·▓·▓·····▓·▓···▓·······▓·····▓···▓·▓···▓
▓·▓▓▓▓▓▓▓·▓·▓▓▓▓▓·▓▓▓▓▓▓▓▓▓▓▓▓▓·▓·▓·▓▓▓·▓
▓·········▓·▓·····▓···▓·········▓·▓···▓·▓
▓·▓▓▓▓▓▓▓▓▓·▓·▓·▓▓▓·▓·▓·▓▓▓▓▓▓▓·▓·▓·▓·▓·▓
▓·▓·······▓·▓·▓·····▓·▓·▓·····▓·▓···▓·▓·▓
▓·▓·▓▓▓▓▓·▓·▓▓ ▓▓▓▓·▓·▓·▓▓▓·▓·▓·▓▓▓▓▓▓▓·▓
▓·▓·▓·····▓···▓···▓·▓·······▓·▓·········▓
▓·▓▓▓·▓▓▓·▓▓▓·▓·▓·▓▓▓▓▓▓▓▓▓▓▓·▓▓▓▓▓▓▓▓▓▓ 
▓···▓·▓·····▓···▓·▓X··▓·····▓·······▓···▓
 ▓▓·▓·▓·▓▓▓▓▓▓▓▓▓·▓▓▓·▓▓▓▓▓·▓▓▓▓▓▓▓·▓·▓·▓
▓·▓···▓·▓·······▓···▓·▓·········▓·▓·▓·▓·▓
▓·▓▓▓▓▓·▓·▓▓▓▓▓·▓▓▓·▓·▓·▓▓▓▓▓▓▓·▓·▓·▓▓▓·▓
▓···▓···▓·····▓···▓·▓·▓·▓·····▓···▓·····▓
▓·▓▓▓·▓▓▓▓▓▓▓·▓▓▓·▓·▓·▓·▓·▓▓▓·▓▓▓·▓▓▓▓▓·▓
▓·····▓·····▓·▓·····▓·▓···▓·▓·▓···▓···▓·▓
▓·▓▓▓▓▓▓▓·▓▓▓·▓▓▓▓▓·▓·▓·▓▓▓·▓·▓▓▓·▓▓▓·▓·▓
▓·▓·······▓···▓···▓·▓·▓·▓···▓···▓·····▓·▓
▓·▓▓▓▓▓·▓·▓·▓▓▓·▓·▓·▓·▓·▓·▓▓▓▓▓·▓▓▓▓▓▓▓·▓
▓·▓·····▓·▓·····▓·▓·▓·▓···▓···▓·····▓···▓
▓·▓·▓▓▓▓▓·▓▓▓▓▓▓▓·▓·▓·▓▓▓·▓·▓·▓▓▓·▓·▓·▓▓ 
▓·▓···▓·▓·▓·····▓·▓·▓·▓···▓·▓···▓·▓·▓·▓·▓
▓·▓▓▓·▓·▓·▓·▓▓▓▓▓·▓·▓·▓▓▓▓▓·▓▓▓·▓▓▓·▓·▓·▓
▓·····▓·▓·▓·▓·····▓·▓·······▓·▓·▓···▓·▓·▓
 ▓▓▓▓▓▓·▓·▓·▓·▓▓▓·▓▓▓▓▓▓▓▓▓▓▓·▓·▓·▓▓▓·▓·▓
▓···▓···▓·▓·▓···▓·▓·········▓···▓·▓···▓·▓
▓O▓·▓·▓·▓·▓·▓▓▓·▓▓▓·▓▓▓▓▓·▓▓▓·▓▓▓·▓·▓▓▓·▓
▓·▓···▓·······▓·········▓·····▓·········▓
 ▓ ▓▓▓ ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓ '''


def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def part1(mem):
    tiles = {(0, 0): '.'}
    px, py = 0, 0
    d = None

    def draw():
        start_x = min(x for x, y in tiles.keys()) - 1
        start_y = min(y for x, y in tiles.keys()) - 1
        end_x = max(x for x, y in tiles.keys()) + 1
        end_y = max(y for x, y in tiles.keys()) + 1

        print('   ┌', *('─' for _ in range(start_x, end_x+1)), '┐', sep='')
        for y in range(end_y, start_y-1, -1):
            print('%3d' % y, end='')
            print('│', end='')
            for x in range(start_x, end_x+1):
                if px == x and py == y:
                    if d == 0:
                        print('↑', end='')
                    elif d == 1:
                        print('↓', end='')
                    elif d == 2:
                        print('→', end='')
                    elif d == 3:
                        print('←', end='')
                    else:
                        print('X', end='')
                elif (x, y) in tiles:
                    print(tiles[(x, y)], end='')
                else:
                    print(' ', end='')
            print('│')
        print('   └', *('─' for _ in range(start_x, end_x+1)), '┘', sep='')

    def input_gen():
        nonlocal d
        for i in itertools.count(0, 1):
            print('input', i)
            draw()
            x = get_char()
            if ord(x) == 27:
                assert get_char() == '['
                d = 'ABCD'.index(get_char())
            else:
                d = 'ZSDG'.index(x.upper())
            yield d + 1
            od = d
            if code != 0:
                for i, j in ((0, 1), (1, 0), (2, 3), (3, 2)):
                    d = i
                    yield d + 1
                    if code != 0:
                        d = j
                        yield d + 1
            d = od

    output = compute(mem, input_gen())

    for code in output:
        # print('code', code)

        dy = 0
        dx = 0

        if d == 0:
            dy = 1
        elif d == 1:
            dy = -1
        elif d == 2:
            dx = 1
        elif d == 3:
            dx = -1

        # print(dict(tiles))

        if code == 0:
            # print('wall')
            tiles[(px + dx, py + dy)] = '▓'
        elif code == 1:
            # print('open')
            tiles[(px, py)] = '·'
            px, py = px + dx, py + dy
        elif code == 2:
            tiles[(px, py)] = 'o'
            print("FOUND O2", (px, py))
            px, py = px + dx, py + dy


def parse_maze():
    maze = defaultdict(lambda: False)
    pos = None
    target = None
    for y, line in enumerate(full_maze.splitlines()):
        print(y, line)
        for x, c in enumerate(line):
            if c == '·':
                maze[(x, y)] = True
            elif c == 'X':
                pos = (x, y)
                maze[(x, y)] = True
            elif c == 'O':
                target = (x, y)
                maze[(x, y)] = True
    return maze, pos, target


def solve_maze():
    maze, pos, target = parse_maze()

    shortest = None

    def step(target, path, pos):
        nonlocal shortest
        # dump(maze, [target], path, pos)
        path.append(pos)

        if shortest is not None and len(shortest) < len(path):
            print('Got some shorter already, drop.', len(shortest), len(path))
            return

        if pos == target:
            if shortest is None:
                shortest = path
                print('First path', len(path), path)
            elif len(path) < len(shortest):
                shortest = path
                print('New shorter path!', len(path), path)

        x, y = pos
        if maze[(x + 1, y)] and (x + 1, y) not in path:
            step(target, path[:], (x + 1, y))
        if maze[(x - 1, y)] and (x - 1, y) not in path:
            step(target, path[:], (x - 1, y))
        if maze[(x, y + 1)] and (x, y + 1) not in path:
            step(target, path[:], (x, y + 1))
        if maze[(x, y - 1)] and (x, y - 1) not in path:
            step(target, path[:], (x, y - 1))

    print('Pathing from', pos, 'to', target)
    step(target, [], pos)

    print(len(shortest), shortest)


def solve_o2():
    maze, _, o2 = parse_maze()
    empties = set(k for k, v in maze.items() if v)
    empties.remove(o2)
    filled = {o2}

    print(empties)
    print(filled)

    def draw():
        for y, line in enumerate(full_maze.splitlines()):
            for x, c in enumerate(line):
                if (x, y) in filled:
                    print('*', end='')
                else:
                    print(c, end='')
            print()
        # input()

    i = 0
    while len(empties) != 0:
        for x, y in set(filled):
            for pos in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if pos in empties:
                    empties.remove(pos)
                    filled.add(pos)

        i += 1
        print(i)
        print(empties)
        print(filled)
    # draw()


if __name__ == '__main__':
    # with open('in15.txt') as f:
    #     part1(GrowingList(int(x) for x in f.read().split(',')))
    # solve_maze()
    solve_o2()
