def part1(inp, base, phases):
    inp = list(map(int, inp))
    # print(0, '->', ''.join(map(str, inp)))

    def gen(p):
        first = True
        while True:
            for b in base:
                for _ in range(p+1):
                    if first:
                        first = False
                        continue
                    yield b

    for p in range(phases):
        inp = [int(str(sum(a*b for a, b in zip(gen(x), inp)))[-1]) for x in range(len(inp))]
        # print(p+1, '->', ''.join(map(str, inp)))
    return ''.join(map(str, inp))


if __name__ == '__main__':
    # part1('98765', (1, 2, 3))
    print(part1('12345678', (0, 1, 0, -1), 4))
    print(part1('80871224585914546619083218645595', (0, 1, 0, -1), 100)[0:8])
    print(part1('19617804207202209144916044189917', (0, 1, 0, -1), 100)[0:8])
    print(part1('69317163492948606335995924319873', (0, 1, 0, -1), 100)[0:8])
    print('REAL 1')
    with open('in16.txt') as f:
        print(part1(f.read().strip(), (0, 1, 0, -1), 100)[0:8])

    print(part1('03036732577212944063491565474664' * 10000, (0, 1, 0, -1), 100)[303673:303673+8])
    print(part1('02935109699940807407585447034323' * 10000, (0, 1, 0, -1), 100)[293510:293510+8])
    print(part1('03081770884921959731165446850517' * 10000, (0, 1, 0, -1), 100)[308177:308177+8])
    print('REAL 2')
    with open('in16.txt') as f:
        print(part1(f.read().strip() * 10000, (0, 1, 0, -1), 100)[78009100:78009100+8])
