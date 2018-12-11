import multiprocessing


def powerLevel(x, y, inp):
    rackid = x + 10
    pwr = rackid * y
    pwr += inp
    pwr *= rackid
    pwr /= 100
    pwr %= 10
    return int(pwr) - 5


def day11(inp, size):
    # print(inp, size)

    grid = [[powerLevel(x+1, y+1, inp) for x in range(300)] for y in range(300)]

    maxes = [[sum(grid[y+yy][x+xx] for xx in range(0, size) for yy in range(0, size))
              for x in range(0, 300-size)]
             for y in range(0, 300-size)]
    maxed = max(max(l) for l in maxes)

    for i, line in enumerate(maxes):
        if maxed in line:
            print(inp, size, '->', (line.index(maxed)+1, i+1), maxed)
            return ','.join(map(str, (line.index(maxed)+1, i+1, size))), maxed

    # return maxed


    # print(*(''.join(map(lambda x: '{:2}'.format(x), line)) for line in maxes), sep='\n')


def day11_2(inp, max_size):
    with multiprocessing.Pool() as p:
        results = p.starmap(day11, ((inp, i) for i in range(1, max_size+1)), chunksize=1)
        p.close()
        p.join()
    # print(*results, sep='\n')
    return max(results, key=lambda x: x[1])


if __name__ == '__main__':
    # print(powerLevel(3, 5, 8), '->', 4)
    # print(powerLevel(122, 79, 57), '->', -5)
    # print(powerLevel(217, 196, 39), '->', 0)
    # print(powerLevel(101, 153, 71), '->', 4)

    # print(day11(18, 2), '->', 29)
    # print(day11(42, 2), '->', 30)
    # print(day11(3214, 2))

    print(day11_2(18, 18), '->', 113)
    print(day11_2(42, 16), '->', 119)
    print(day11_2(3214, 300))




