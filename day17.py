from collections import deque


def part1(data):
    i = 0
    mem = [0]
    for loop in range(2017):
        i = 1 + ((i + data) % len(mem))
        mem.insert(i, loop + 1)
    return mem[i + 1]


def part2(data):
    # Thanks reddit. The solution to part 1 would work, but it takes forever.
    mem = deque([0])
    for loop in range(50000000):
        mem.rotate(-data)
        mem.append(loop + 1)
        if loop % 100000 == 0:
            print(loop)
    return mem[mem.index(0) + 1]


if __name__ == '__main__':
    example_data = 3
    print("example1:", part1(example_data))
    # print("example2:", part2(example_data))
    input_data = 370
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))
