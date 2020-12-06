def parse(line):
    rows = [*range(128)]
    for c in line[:7]:
        print(c, len(rows)//2, rows)
        if c == 'F':
            rows = rows[:len(rows)//2]
        elif c == 'B':
            rows = rows[len(rows)//2:]
        else:
            assert False
    row, = rows

    cols = [*range(8)]
    for c in line[7:]:
        print(c, len(cols)//2, cols)
        if c == 'L':
            cols = cols[:len(cols)//2]
        elif c == 'R':
            cols = cols[len(cols)//2:]
        else:
            assert False
    col, = cols

    print(line, row, col, row * 8 + col)
    return row, col, row * 8 + col


def part1(inp):
    return max(parse(x)[2] for x in inp.splitlines())


def part2(inp):
    seats = [parse(x)[2] for x in inp.splitlines()]
    seats.sort()
    for p, x in zip(seats, seats[1:]):
        if p != x - 1:
            return x - 1


def _main():
    assert parse("FBFBBFFRLR") == (44, 5, 357)
    assert parse("BFFFBBFRRR") == (70, 7, 567)
    assert parse("FFFBBBFRRR") == (14, 7, 119)
    assert parse("BBFFBBFRLL") == (102, 4, 820)
    print(part1(open('in5.txt').read()))
    print(part2(open('in5.txt').read()))


if __name__ == '__main__':
    _main()
