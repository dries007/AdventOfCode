import re
import collections
from pprint import pprint


example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def part1(inp):
    rules = {}
    for rule in inp.splitlines():
        outer, inner = rule[:-1].split(" bags contain ")
        if inner == "no other bags":
            rules[outer] = set()
        else:
            rules[outer] = set(re.fullmatch(r"\d+ (.*) bags?", x).groups()[0] for x in inner.split(", "))

    can_contain = set()

    def search(needle: str):
        if needle in can_contain:
            return True
        if "shiny gold" in rules[needle]:
            can_contain.add(needle)
            return True
        for v in rules[needle]:
            if search(v):
                return True
        return False

    ok = set()
    for x in list(rules.keys()):
        if search(x):
            ok.add(x)

    return len(ok)


def part2(inp):
    rules = {}
    for rule in inp.splitlines():
        outer, inner = rule[:-1].split(" bags contain ")
        if inner == "no other bags":
            rules[outer] = {}
        else:
            rules[outer] = {}
            for x in inner.split(", "):
                n, c = re.fullmatch(r"(\d+) (.*) bags?", x).groups()
                rules[outer][c] = int(n)

    counts = {}

    def count(needle: str) -> int:
        if needle in counts:
            return counts[needle]

        running = sum(rules[needle].values())
        for c, n in rules[needle].items():
            y = count(c)
            running += n * y
        counts[needle] = running
        return running

    return count("shiny gold")


def _main():
    print(part1(example))
    print(part2(example))
    print(part1(open('in7.txt').read()))
    print(part2(open('in7.txt').read()))


if __name__ == '__main__':
    _main()
