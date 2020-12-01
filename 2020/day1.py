example = """1721
979
366
299
675
1456
"""


def part1(inp):
    inp = [int(x) for x in inp.splitlines()]
    for x in inp:
        for y in inp:
            if x + y == 2020:
                return x * y


def part2(inp):
    inp = [int(x) for x in inp.splitlines()]
    for x in inp:
        for y in inp:
            for z in inp:
                if x + y + z == 2020:
                    return x * y * z


def _main():
    assert part1(example) == 514579
    assert part2(example) == 241861950
    print(part1(open('in1.txt').read()))
    print(part2(open('in1.txt').read()))


if __name__ == '__main__':
    _main()
