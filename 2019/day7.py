import itertools


def compute(mem, inp):
    def decode_mode():
        """
        Decode parameter mode
        """
        nonlocal offset
        # get digit at index offset+1
        mode = (instr // (10 ** (offset + 1))) % 10
        val = mem[ip + offset]
        # print(f'decode {instr=} {offset=} {mode=} {val=}')
        offset += 1
        return mode, val

    def load():
        # print('load')
        mode, parameter = decode_mode()
        if mode == 0:
            # print(f'load addr mode {parameter=} {mem[parameter]=}')
            return mem[parameter]
        elif mode == 1:
            # print(f'load immediate {parameter=}')
            return parameter
        else:
            raise RuntimeError('impossible load mode')

    def store(value):
        # print('store')
        mode, parameter = decode_mode()
        if mode == 0:
            # print(f'store addr mode mem[{parameter=}]<-{value=}')
            mem[parameter] = value
        else:
            raise RuntimeError('impossible store mode.')

    # print('START', mem)
    ip = 0
    while True:
        instr = mem[ip]
        opcode = instr % 100
        offset = 1
        # print(f'cycle {ip=} {instr=} {opcode=}')
        if opcode == 99:
            # print('Halt!')
            break
        elif opcode == 1:
            # print('add')
            store(load() + load())
        elif opcode == 2:
            # print('mult')
            store(load() * load())
        elif opcode == 3:
            # print('ld')
            store(next(inp))
        elif opcode == 4:
            # print('st')
            yield load()
            # print('Output set', outp)
        elif opcode == 5:
            val = load()
            ip_next = load()
            if val != 0:
                ip = ip_next
                continue  # Skip autoincrement of ip
        elif opcode == 6:
            val = load()
            ip_next = load()
            if val == 0:
                ip = ip_next
                continue  # Skip autoincrement of ip
        elif opcode == 7:
            store(1 if load() < load() else 0)
        elif opcode == 8:
            store(1 if load() == load() else 0)
        else:
            raise RuntimeError('Illegal opcode')

        ip += offset
    # print('Halt')
    # return mem


def amplifiers1(mem, phases):
    signal = 0
    for phase in phases:
        # print(f'Next amp {phase=} {signal=}')
        signal = next(compute(mem[:], iter((phase, signal))))
    # print('Output ', signal)
    return signal


def part1(mem):
    max_out = 0
    max_phase = None
    for phases in itertools.permutations(list(range(5))):
        out = amplifiers1(mem, phases)
        if out > max_out:
            max_out = out
            max_phase = phases
    print(max_out, max_phase)
    return max_out, max_phase


def amplifiers2(mem, phases):
    feedback = None

    def input_generator(amp):
        nonlocal feedback

        # fist input = phase setting
        # print('yield phase', phases[amp], 'for amp', amp)
        yield phases[amp]

        if amp == 0:
            # bootstrap
            # print('yield bootstrap for amp', amp)
            yield 0
            # feedback
            while True:
                # print('yield feedback', feedback, 'for amp', amp)
                yield feedback

        # more amps
        # print('yield from next for amp', amp)
        yield from compute(mem[:], input_generator(amp - 1))

    last = compute(mem[:], input_generator(len(phases)-1))

    # Loop over all of the iterations of amplifier E and store it's output
    for feedback in last:
        pass

    # print(feedback)
    return feedback


def part2(mem):
    max_out = 0
    max_phase = None
    for phases in itertools.permutations(list(range(5, 10))):
        out = amplifiers2(mem, phases)
        if out > max_out:
            max_out = out
            max_phase = phases
    print(max_out, max_phase)
    return max_out, max_phase


if __name__ == '__main__':
    # part1([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    # part1([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
    # part1([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
    # with open('in7.txt') as f:
    #     print('PART1', part1([int(x) for x in f.read().split(',')]))

    # amplifiers2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], (9,8,7,6,5))
    part2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
    part2([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10])
    with open('in7.txt') as f:
        print('PART2', part2([int(x) for x in f.read().split(',')]))
