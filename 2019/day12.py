import copy
import itertools
import re

example1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

example2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

PARSE = re.compile(r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$')


class Moon:
    def __init__(self, i, px, py, pz, vx, vy, vz):
        self.i = i
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __repr__(self) -> str:
        return f'<Moon {self.i} p: {self.px},{self.py},{self.pz} v: {self.vx},{self.vy},{self.vz}>'


def parse_inp(inp):
    return [Moon(i, *map(int, PARSE.match(x).groups()), 0, 0, 0) for i, x in enumerate(inp.splitlines())]


def step(moons):
    for m1, m2 in itertools.combinations(moons, 2):
        if m1.px < m2.px:
            m1.vx += 1
            m2.vx -= 1
        if m1.px > m2.px:
            m1.vx -= 1
            m2.vx += 1
        if m1.py < m2.py:
            m1.vy += 1
            m2.vy -= 1
        if m1.py > m2.py:
            m1.vy -= 1
            m2.vy += 1
        if m1.pz < m2.pz:
            m1.vz += 1
            m2.vz -= 1
        if m1.pz > m2.pz:
            m1.vz -= 1
            m2.vz += 1

    for m in moons:
        m.px += m.vx
        m.py += m.vy
        m.pz += m.vz


def part1(inp, steps):
    moons = parse_inp(inp)

    for i in range(steps):
        # print('step ', i)
        step(moons)
        # print(*moons, sep='\n')

    e = sum(sum(map(abs, (m.px, m.py, m.pz))) *
            sum(map(abs, (m.vx, m.vy, m.vz))) for m in moons)
    print(e)


def part2(inp):
    moons = parse_inp(inp)
    history = {' '.join(map(repr, moons))}
    for i in itertools.count(0, 1):
        step(moons)
        s = ' '.join(map(repr, moons))
        if s in history:
            print(i+1)
            break
        history.add(s)


if __name__ == '__main__':
    # part1(example1, 10)
    # part1(example2, 100)
    # with open('in12.txt') as f:
    #     part1(f.read(), 1000)

    part2(example1)
    part2(example2)
    with open('in12.txt') as f:
        part2(f.read())

