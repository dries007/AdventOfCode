def generator(factor, val, mod):
    while True:
        val = (val * factor) % 2147483647
        if val % mod == 0:
            yield val


def part1(a, b):
    ga = generator(16807, a, 1)
    gb = generator(48271, b, 1)

    return sum(next(ga) & 0xFFFF == next(gb) & 0xFFFF for _ in range(40_000_000))


def part2(a, b):
    ga = generator(16807, a, 4)
    gb = generator(48271, b, 8)

    return sum(next(ga) & 0xFFFF == next(gb) & 0xFFFF for _ in range(5_000_000))


if __name__ == '__main__':
    # print("example1:", part1(65, 8921))
    print("example2:", part2(65, 8921))
    # print("part1:", part1(703, 516))
    print("part2:", part2(703, 516))
