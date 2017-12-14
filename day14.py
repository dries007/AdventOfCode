from functools import reduce


def knot_hash(data):
    lst = list(range(256))
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    # print("data", lst)
    # print("input", lengths)
    n = len(lst)

    for _ in range(64):
        for l in lengths:
            # print('len', l, 'pos', pos, 'skip', skip, 'lst', lst, 'section', lst[pos:(pos + l)], (pos + l))
            sub = []
            for i in range(l):
                sub.append(lst[(pos + i) % n])
            # print(sub)
            sub = list(reversed(sub))
            # print(sub)
            for i in range(l):
                lst[(pos + i) % n] = sub[i]
            pos += l + skip
            skip += 1
    dense = [reduce(lambda a, b: a ^ b, lst[i:i + 16]) for i in range(0, n, 16)]
    return ''.join(['{:02x}'.format(x) for x in dense])


def flood_fill(mem, r, k):
    mem[r][k] = '.'
    if r > 0:
        if mem[r - 1][k] == '1':
            flood_fill(mem, r - 1, k)
    if r < 127:
        if mem[r + 1][k] == '1':
            flood_fill(mem, r + 1, k)
    if k > 0:
        if mem[r][k - 1] == '1':
            flood_fill(mem, r, k - 1)
    if k < 127:
        if mem[r][k + 1] == '1':
            flood_fill(mem, r, k + 1)


def find_region(mem):
    r = 0
    k = -1

    while k == -1:
        try:
            k = mem[r].index('1')
        except ValueError:
            r += 1
        except IndexError:
            return False

    print(r, k, mem[r][k])
    flood_fill(mem, r, k)
    print(*(''.join(x) for x in mem), sep='\n')
    print('-' * 128)
    return True


def part1(data):
    count = 0
    mem = []
    for r in range(128):
        k = data + '-' + str(r)
        v = [x for x in '{0:0128b}'.format(int(knot_hash(k), 16))]
        mem.append(v)
        # print(k, v)
        count += v.count('1')
    print(*(''.join(x) for x in mem), sep='\n')

    regions = 0
    while find_region(mem):
        regions += 1

    return count, regions


if __name__ == '__main__':
    print('a0c2017 in binary:', '{0:b}'.format(int('a0c2017', 16)))

    example_data = r'flqrgnkx'
    print("example1, example2:", part1(example_data))
    input_data = r'hfdlxzhv'
    print("part1, part2:", part1(input_data))
