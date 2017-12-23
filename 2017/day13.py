def parse(data):
    return {int(k): int(v) for k, v in [x.split(': ') for x in data.splitlines()]}


def move(depth, pos, d):
    if d:  # Moving down
        pos += 1
        if pos == depth - 1:
            d = False
    else:  # Moving up
        pos -= 1
        if pos == 0:
            d = True
    return depth, pos, d


def calc_severity(data, offset=0):
    scanners = {k: (v, 0, True) for k, v in data.items()}
    del data

    for i in range(offset):
        for k in scanners.keys():
            scanners[k] = move(*scanners[k])

    sev = 0
    caught = False
    for i in range(1 + max(scanners.keys())):

        # print('pos in step', i, ':', scanners)

        if i in scanners.keys():
            scanner = scanners[i]
            # print('STEP', i, scanner)

            if scanner[1] == 0:
                # print('cought in', i)
                sev += scanner[0] * i
                caught = True

        for k in scanners.keys():
            scanners[k] = move(*scanners[k])

    return sev, caught


def part1(data):
    return calc_severity(parse(data))


def pos(depth, step):
    #  Thanks Reddit
    x = step % ((depth - 1) * 2)
    return 2 * (depth - 1) - x if x > depth - 1 else x


def part2(data):
    data = parse(data)

    offset = 0
    while True:
        if not any(pos(data[k], offset + k) == 0 for k in data.keys()):
            return offset
        offset += 1
        print(offset)


if __name__ == '__main__':
    example_data = r'''0: 3
1: 2
4: 4
6: 4
'''
    print("example1:", part1(example_data))
    print("example2:", part2(example_data))
    input_data = r'''0: 3
1: 2
2: 4
4: 6
6: 4
8: 6
10: 5
12: 6
14: 9
16: 6
18: 8
20: 8
22: 8
24: 8
26: 8
28: 8
30: 12
32: 14
34: 10
36: 12
38: 12
40: 10
42: 12
44: 12
46: 12
48: 12
50: 12
52: 14
54: 14
56: 12
62: 12
64: 14
66: 14
68: 14
70: 17
72: 14
74: 14
76: 14
82: 14
86: 18
88: 14
96: 14
98: 44'''
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))
