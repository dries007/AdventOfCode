def parse(data):
    return [int(x) for x in data.split()]


def distribute(data):
    n = len(data)
    m = max(data)
    i = data.index(m)
    # print(n, m, i)
    data[i] = 0
    while m != 0:
        i = (i + 1) % n
        m -= 1
        data[i] += 1
    return data


def part1(data):
    known = []
    i = 0
    while data not in known:
        # print(i, data)
        i += 1
        known.append(data[:])
        distribute(data)
    return i


def part2(data):
    part1(data)
    target = data[:]
    # print("target", target)
    distribute(data)
    i = 1
    while target != data:
        # print(i, data)
        i += 1
        distribute(data)
    return i


if __name__ == '__main__':
    print("example1:", part1(parse('0 2 7 0')))

    input_data = '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5'
    print("part1:", part1(parse(input_data)))
    print("part2:", part2(parse(input_data)))
