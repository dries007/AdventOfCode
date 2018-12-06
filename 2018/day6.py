import re
import string
import collections


example = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''
input = '''194, 200
299, 244
269, 329
292, 55
211, 63
123, 311
212, 90
292, 169
359, 177
354, 95
101, 47
95, 79
95, 287
294, 126
81, 267
330, 78
202, 165
225, 178
266, 272
351, 326
180, 62
102, 178
151, 101
343, 145
205, 312
74, 193
221, 56
89, 89
242, 172
59, 138
83, 179
223, 88
297, 234
147, 351
226, 320
358, 338
321, 172
54, 122
263, 165
126, 341
64, 132
264, 306
72, 202
98, 49
238, 67
310, 303
277, 281
222, 318
357, 169
123, 225'''

RE_LINE = re.compile(r'(\d+), (\d+)', re.IGNORECASE)

ALPHABET = string.ascii_letters + string.digits
TIE = '.'
REMOVED = '*'
UNKNOWN = '?'
NEAR = '#'
FAR = TIE


class Point:
    def __init__(self, x: int, y: int, symbol: str) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.symbol = symbol

    def __repr__(self) -> str:
        return '<{};{} {}>'.format(self.x, self.y, self.symbol)

    def __str__(self):
        return self.symbol

    def dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


def print_grid(grid):
    print(*(''.join(map(lambda x: str(x), r)) for r in grid), sep='\n')


def day6_1(inp):
    points = [
        Point(*map(int, RE_LINE.match(line).groups()), ALPHABET[i]) for i, line in enumerate(inp.splitlines())
    ]
    minX = min(points, key=lambda x: x.x).x-1
    minY = min(points, key=lambda x: x.y).y-1
    maxX = max(points, key=lambda x: x.x).x+2
    maxY = max(points, key=lambda x: x.y).y+2

    def closest(x, y):
        distances = [(p.dist(x, y), p.symbol) for p in points]
        distances.sort(key=lambda d: d[0])
        if distances[0][0] == distances[1][0]:
            return TIE

        return distances[0][1]

    grid = [[closest(x, y) for x in range(minX, maxX)] for y in range(minY, maxY)]
    print("Filled")
    print_grid(grid)

    removed = []
    for y in (0, len(grid)-1):
        for x in (0, len(grid[0])-1):
            remove = grid[y][x]
            if remove in removed:
                continue
            if remove == TIE:
                continue
            removed.append(remove)

    counts = collections.defaultdict(lambda: 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in removed:
                grid[y][x] = REMOVED
            else:
                counts[grid[y][x]] += 1
    counts = [*sorted(counts.items(), key=lambda i: i[1], reverse=True)]
    return counts


def day6_2(inp):
    points = [Point(*map(int, RE_LINE.match(line).groups()), ALPHABET[i]) for i, line in enumerate(inp.splitlines())]
    minX = min(points, key=lambda x: x.x).x - 1
    minY = min(points, key=lambda x: x.y).y - 1
    maxX = max(points, key=lambda x: x.x).x + 2
    maxY = max(points, key=lambda x: x.y).y + 2

    def distance_sum(x, y):
        return NEAR if sum([p.dist(x, y) for p in points]) < 10000 else FAR

    grid = [[distance_sum(x, y) for x in range(minX, maxX)] for y in range(minY, maxY)]
    print("Filled")
    print_grid(grid)

    counts = collections.defaultdict(lambda: 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            counts[grid[y][x]] += 1
    counts = [*sorted(counts.items(), key=lambda i: i[1], reverse=True)]
    return counts


if __name__ == '__main__':
    print(*day6_1(example))
    print(*day6_1(input))
    print(*day6_2(example))
    print(*day6_2(input))
