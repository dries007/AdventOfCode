from collections import defaultdict


def part1(prog):
    prog = prog.splitlines()
    size = len(prog)
    mem = defaultdict(lambda: 0)
    pc = 0

    def get(arg):
        try:
            return int(arg)
        except:
            return mem[arg]

    i = 0
    while pc < size:
        inst = prog[pc].split()
        pc += 1

        if inst[0] == 'set':
            mem[inst[1]] = get(inst[2])
        elif inst[0] == 'sub':
            mem[inst[1]] -= get(inst[2])
        elif inst[0] == 'mul':
            i += 1
            mem[inst[1]] *= get(inst[2])
        elif inst[0] == 'jnz':
            if get(inst[1]) != 0:
                pc += get(inst[2]) - 1

        # print(inst, dict(mem))
    return i


def part2(b):
    # Part 2 is a prime number check between b + 17000 and b * 100 + 100000
    b = b * 100 + 100000
    c = b + 17000
    h = 0
    for x in range(b, c + 1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h


if __name__ == '__main__':
    input_data = r'''set b 81
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''
    print("part1:", part1(input_data))
    print("part2:", part2(81))
