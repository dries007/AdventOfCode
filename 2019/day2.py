def part1(inp):
    mem = [int(x) for x in inp.split(',')]
    mem[1] = 12
    mem[2] = 2
    print(compute(mem))


def part2(inp):
    mem = [int(x) for x in inp.split(',')]
    for noun in range(100):
        for verb in range(100):
            mem_copy = mem[:]
            mem_copy[1] = noun
            mem_copy[2] = verb
            mem_copy = compute(mem_copy)
            if mem_copy[0] == 19690720:
                print('Gotcha!', 100*noun+verb, noun, verb, mem_copy)
                return
            # print('nope', noun, verb)


def compute(mem):
    i = 0
    while True:
        if mem[i] == 99:
            # print('Halt', i, mem)
            break
        elif mem[i] == 1:
            p1 = mem[i + 1]
            p2 = mem[i + 2]
            p3 = mem[i + 3]
            mem[p3] = mem[p1] + mem[p2]
        elif mem[i] == 2:
            p1 = mem[i + 1]
            p2 = mem[i + 2]
            p3 = mem[i + 3]
            mem[p3] = mem[p1] * mem[p2]
        else:
            print('error', i)
            raise Exception()
        i += 4
    return mem


if __name__ == '__main__':
    compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    compute([1, 0, 0, 0, 99])
    compute([2, 3, 0, 3, 99])
    compute([2, 4, 4, 5, 99, 0])
    compute([1, 1, 1, 4, 99, 5, 6, 0, 99])
    with open('in2.txt') as f:
        part1(f.read())
    with open('in2.txt') as f:
        part2(f.read())
