import re
import string
import collections


example = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''
input = '''Step F must be finished before step Q can begin.
Step A must be finished before step K can begin.
Step K must be finished before step R can begin.
Step D must be finished before step X can begin.
Step L must be finished before step T can begin.
Step V must be finished before step W can begin.
Step J must be finished before step N can begin.
Step B must be finished before step W can begin.
Step X must be finished before step C can begin.
Step W must be finished before step I can begin.
Step Q must be finished before step P can begin.
Step E must be finished before step M can begin.
Step C must be finished before step N can begin.
Step U must be finished before step O can begin.
Step O must be finished before step R can begin.
Step N must be finished before step Z can begin.
Step R must be finished before step I can begin.
Step G must be finished before step H can begin.
Step T must be finished before step H can begin.
Step M must be finished before step P can begin.
Step Y must be finished before step I can begin.
Step S must be finished before step Z can begin.
Step I must be finished before step H can begin.
Step H must be finished before step P can begin.
Step P must be finished before step Z can begin.
Step Y must be finished before step P can begin.
Step A must be finished before step O can begin.
Step V must be finished before step O can begin.
Step G must be finished before step Y can begin.
Step K must be finished before step B can begin.
Step I must be finished before step P can begin.
Step D must be finished before step L can begin.
Step A must be finished before step P can begin.
Step O must be finished before step T can begin.
Step F must be finished before step C can begin.
Step M must be finished before step S can begin.
Step V must be finished before step Q can begin.
Step G must be finished before step I can begin.
Step O must be finished before step I can begin.
Step N must be finished before step I can begin.
Step E must be finished before step O can begin.
Step N must be finished before step S can begin.
Step J must be finished before step H can begin.
Step C must be finished before step P can begin.
Step E must be finished before step N can begin.
Step T must be finished before step P can begin.
Step A must be finished before step G can begin.
Step A must be finished before step V can begin.
Step C must be finished before step H can begin.
Step A must be finished before step Y can begin.
Step E must be finished before step U can begin.
Step T must be finished before step Y can begin.
Step Q must be finished before step S can begin.
Step Y must be finished before step S can begin.
Step E must be finished before step P can begin.
Step N must be finished before step T can begin.
Step T must be finished before step M can begin.
Step Q must be finished before step M can begin.
Step H must be finished before step Z can begin.
Step D must be finished before step Y can begin.
Step J must be finished before step R can begin.
Step U must be finished before step R can begin.
Step K must be finished before step N can begin.
Step A must be finished before step W can begin.
Step A must be finished before step H can begin.
Step X must be finished before step G can begin.
Step V must be finished before step J can begin.
Step W must be finished before step C can begin.
Step I must be finished before step Z can begin.
Step V must be finished before step H can begin.
Step R must be finished before step H can begin.
Step U must be finished before step N can begin.
Step O must be finished before step Z can begin.
Step X must be finished before step S can begin.
Step E must be finished before step G can begin.
Step W must be finished before step U can begin.
Step U must be finished before step G can begin.
Step D must be finished before step Z can begin.
Step E must be finished before step R can begin.
Step L must be finished before step B can begin.
Step B must be finished before step R can begin.
Step G must be finished before step T can begin.
Step F must be finished before step K can begin.
Step R must be finished before step S can begin.
Step J must be finished before step Z can begin.
Step Q must be finished before step U can begin.
Step X must be finished before step O can begin.
Step F must be finished before step I can begin.
Step W must be finished before step R can begin.
Step W must be finished before step Y can begin.
Step M must be finished before step Y can begin.
Step S must be finished before step I can begin.
Step F must be finished before step O can begin.
Step C must be finished before step Y can begin.
Step N must be finished before step G can begin.
Step O must be finished before step S can begin.
Step Q must be finished before step O can begin.
Step K must be finished before step T can begin.
Step X must be finished before step Z can begin.
Step L must be finished before step N can begin.
Step S must be finished before step P can begin.'''

RE_LINE = re.compile(r'Step (.) must be finished before step (.) can begin.', re.IGNORECASE)


def day6_1(inp):
    letters = set()
    dependencies = collections.defaultdict(lambda: [])

    for line in inp.splitlines():
        a, b = RE_LINE.match(line).groups()
        letters.add(a)
        dependencies[b].append(a)

    for l, lst in dependencies.items():
        lst.sort()

    start = list(letters - dependencies.keys())
    start.sort()

    order = []
    working = next(iter(start))
    start.remove(working)
    print("Starting with", start)
    while any(map(lambda x: len(x[1]) != 0, dependencies.items())):
        print(*dependencies.items())
        print("Working", working, "Order:", *order)
        order.append(working)
        possible = []
        possible.extend(start)
        for task, deps in dependencies.items():
            if working in deps:
                print("Remove", working, "from", task)
                deps.remove(working)
            if len(deps) == 0:
                possible.append(task)
        print("Next?", possible)
        possible.sort()
        if len(possible) == 0:
            raise Exception("Kapot 2")
        working = possible[0]
        if working in dependencies:
            del dependencies[working]
        if working in start:
            start.remove(working)
    order.append(working)
    return ''.join(order)


def day6_2(inp, n, delay):
    pass


if __name__ == '__main__':
    print(day6_1(example))
    print(day6_1(input))
    # print(day6_2(example, 2, 0))
    # print(day6_2(input))
