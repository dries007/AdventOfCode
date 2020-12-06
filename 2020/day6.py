example = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def parse1(group: list[str]):
    letters = set(''.join(group))
    # print(len(group), '->', letters)
    return len(letters)


def parse2(group: list[str]):
    common = set(group[0])
    for person in group[1:]:
        common &= set(person)
    # print(len(group), '->', common)
    return len(common)


def part1(inp):
    groups = []
    group = []
    for line in inp.splitlines():
        if not line:
            groups.append(parse1(group))
            group = []
        else:
            group.append(line)
    groups.append(parse1(group))
    return sum(groups)


def part2(inp):
    groups = []
    group = []
    for line in inp.splitlines():
        if not line:
            groups.append(parse2(group))
            group = []
        else:
            group.append(line)
    groups.append(parse2(group))
    return sum(groups)


def _main():
    print(part1(example))
    print(part2(example))
    print(part1(open('in6.txt').read()))
    print(part2(open('in6.txt').read()))


if __name__ == '__main__':
    _main()
