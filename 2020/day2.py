import re

example = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

P = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', re.IGNORECASE)


def part1(inp):
    inp = (P.fullmatch(x).groups() for x in inp.splitlines())
    return sum(int(mn) <= pwd.count(letter) <= int(mx) for mn, mx, letter, pwd in inp)


def part2(inp):
    inp = (P.fullmatch(x).groups() for x in inp.splitlines())
    inp = ((int(a), int(b), letter, pwd) for a, b, letter, pwd in inp)
    tmp = ((pwd[a-1] == letter) ^ (pwd[b-1] == letter) for a, b, letter, pwd in inp)
    return sum(tmp)


def _main():
    assert part1(example) == 2
    assert part2(example) == 1
    print(part1(open('in2.txt').read()))
    print(part2(open('in2.txt').read()))


if __name__ == '__main__':
    _main()
