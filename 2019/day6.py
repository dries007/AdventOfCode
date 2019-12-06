example1 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''

example2 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''


def part1(lines):
    print('START')

    direct = {}
    parents = {}
    for line in lines:
        parent, child = line.strip().split(')')
        if parent not in direct:
            direct[parent] = set()
        direct[parent].add(child)
        assert child not in parents
        parents[child] = parent

    children = set().union(*direct.values())

    root, = (direct.keys() - children)
    cache = {root: 0}

    def depth(x):
        if x in cache:
            return cache[x]
        d = depth(parents[x]) + 1
        cache[x] = d
        return d

    total = sum(map(depth, children))
    print(cache)
    print('total', total)
    return total


def part2(lines):
    print('START')

    direct = {}
    parents = {}
    for line in lines:
        parent, child = line.strip().split(')')
        if parent not in direct:
            direct[parent] = set()
        direct[parent].add(child)
        assert child not in parents
        parents[child] = parent

    children = set().union(*direct.values())
    root, = (direct.keys() - children)

    print('direct', direct)
    print('parents', parents)

    def get_path(x):
        # print(f'get_path({x=})')
        if x == root:
            return x,
        return x, *get_path(parents[x])

    you = get_path('YOU')
    san = get_path('SAN')

    common = None
    for common in you:
        if common in san:
            break
    assert common is not None

    print('common', common)

    print(you)
    print(san)

    return you.index(common) - 1 + san.index(common) - 1


if __name__ == '__main__':
    # print(part1(example1.splitlines()))
    # with open('in6.txt') as f:
    #     print(part1(f))
    print(part2(example2.splitlines()))
    with open('in6.txt') as f:
        print(part2(f))
