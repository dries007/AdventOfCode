import collections

example = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

input = """initial state: ..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#

#..#. => .
..#.. => .
..#.# => #
##.#. => .
.#... => #
#.... => .
##### => #
.#.## => .
#.#.. => .
#.### => #
.##.. => #
##... => .
#...# => #
####. => #
#.#.# => .
#..## => .
.#### => .
...## => .
..### => #
.#..# => .
##..# => #
.#.#. => .
..##. => .
###.. => .
###.# => #
#.##. => #
..... => .
.##.# => #
....# => .
##.## => #
...#. => #
.###. => ."""


def life(rules: collections.defaultdict, state: collections.defaultdict):
    # print("Life", dict_to_state(state))
    mn = min(state.keys()) - 3
    mx = max(state.keys()) + 3
    # print(mn, '->', mx)
    d = state_as_dict()
    for x in range(mn, mx+2):
        substate = dict_to_state(state, x-2, x+3)
        result = rules[substate]
        # print(x, substate, '->', result)
        if result == '#':
            d[x] = result
    return d


def state_as_dict(state: str = None):
    d = collections.defaultdict(lambda: '.')
    if state:
        for i, s in enumerate(state):
            if s == '#':
                d[i] = s
    return d


def dict_to_state(data: collections.defaultdict, mn=None, mx=None):
    if mn is None:
        mn = min(data.keys())-1
    if mx is None:
        mx = max(data.keys())+2
    return ''.join((data[x] if x in data else '.' for x in range(mn, mx)))


def day12(inp, n):
    split = iter(inp.splitlines())
    initial = next(split)
    next(split)  # Empty line
    initial = initial.split(': ')[1]

    rules = collections.defaultdict(lambda: '.')
    for line in split:
        rule, outcome = line.split(' => ')
        rules[rule] = outcome
    # print(*rules.items(), sep='\n')

    state = state_as_dict(initial)
    for gen in range(1, n+1):
        state = life(rules, state)
        if gen % 10000 == 0:
            print(gen, dict_to_state(state), sum(state.keys()))

    return dict_to_state(state), sum(state.keys())


if __name__ == '__main__':
    # print(day12(example, 20))
    print(day12(input, 20))
    print(day12(input, 50000000000))
