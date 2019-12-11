from collections import defaultdict
from day9 import compute, GrowingList


def draw(mem, part2):
    x, y = 0, 0
    direction = 0
    field = defaultdict(lambda: False)

    if part2:
        field[(0, 0)] = True

    def inputs():
        while True:
            yield field[(x, y)]

    prog = compute(mem, inputs())
    print('START', (x, y), direction)
    for paint in prog:
        rot = next(prog)
        field[(x, y)] = paint == 1
        direction += 1 if rot else -1
        direction %= 4
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
        print('STEP', paint, rot, (x, y), direction)

    print(len(field))

    x1 = min(x for x, y in field.keys())
    x2 = max(x for x, y in field.keys())
    y1 = max(y for x, y in field.keys())
    y2 = min(y for x, y in field.keys())

    for y in range(y1, y2-1, -1):
        print(''.join('#' if field[(x, y)] else ' ' for x in range(x1, x2+1)))


if __name__ == '__main__':
    with open('in11.txt') as f:
        draw(GrowingList(int(x) for x in f.read().split(',')), False)

    with open('in11.txt') as f:
        draw(GrowingList(int(x) for x in f.read().split(',')), True)
