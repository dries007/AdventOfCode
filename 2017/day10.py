from functools import reduce


def part1(lst, lengths):
    pos = 0
    skip = 0
    # print("data", lst)
    # print("input", lengths)
    n = len(lst)

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

    # print('end', pos, skip, lst)
    return lst[0] * lst[1]


def part2(lst, lengths):
    lengths += [17, 31, 73, 47, 23]

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

    # print('end', pos, skip, lst)
    print(lst)

    dense = [reduce(lambda a, b: a ^ b, lst[i:i + 16]) for i in range(0, n, 16)]
    print(len(dense), dense)
    return ''.join(['{:02x}'.format(x) for x in dense])


if __name__ == '__main__':
    print("example1:", part1(list(range(5)), [3, 4, 1, 5]))
    print("example2 '':", part2(list(range(256)), []))
    print("example2 'AoC 2017':", part2(list(range(256)), [ord(x) for x in 'AoC 2017']))
    print("example2 '1,2,3':", part2(list(range(256)), [ord(x) for x in '1,2,3']))
    print("example2 '1,2,4:", part2(list(range(256)), [ord(x) for x in '1,2,4']))

    input_data = r'165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'
    print("part1:", part1(list(range(256)), [int(x) for x in input_data.split(',')]))
    print("part2:", part2(list(range(256)), [ord(x) for x in input_data]))
