import itertools


def compute(mem, inp):
    """
    Intcode computation generator (yields output values, returns on halt)

    mem must be a mutable list of memory.
    inp must be a generator/iterator of inputs.
    """
    def decode_mode():
        """
        Decode parameter mode for the current parameter. Increments parameter offset.
        """
        nonlocal offset
        # get digit (0-9) at index 'offset+1'. +1 to account for double digit opcodes.
        mode = (instr // (10 ** (offset + 1))) % 10
        val = mem[ip + offset]
        # print(f'decode {instr=} {offset=} {mode=} {val=}')
        offset += 1
        return mode, val

    def load():
        """
        Load next argument (based on offset).
        Does all mode handling/offset increase.
        """
        mode, parameter = decode_mode()
        if mode == 0:  # address based load
            # print(f'load addr mode {parameter=} {mem[parameter]=}')
            return mem[parameter]
        elif mode == 1:  # immediate value load
            # print(f'load immediate {parameter=}')
            return parameter
        else:
            raise RuntimeError('impossible load mode')

    def store(value):
        """
        Store next argument (based on offset).
        Does all mode handling/offset increase.
        """
        mode, parameter = decode_mode()
        if mode == 0:  # address based store
            # print(f'store addr mode mem[{parameter=}]<-{value=}')
            mem[parameter] = value
        else:
            raise RuntimeError('impossible store mode.')

    # Interpreter loop
    ip = 0
    while True:
        instr = mem[ip]  # full instruction
        opcode = instr % 100  # opcode only
        offset = 1  # 1 because the first load/store should use the _next_ memory location instead of the current.
        # print(f'cycle {ip=} {instr=} {opcode=}')
        if opcode == 99:  # halt
            return
        elif opcode == 1:  # add
            store(load() + load())
        elif opcode == 2:  # multiply
            store(load() * load())
        elif opcode == 3:   # read input (blocking)
            store(next(inp))
        elif opcode == 4:  # write output (blocking)
            yield load()
        elif opcode == 5:  # jump if not zero
            if load() != 0:
                ip = load()
                continue  # Skip autoincrement of ip
            offset += 1   # jump over next argument
        elif opcode == 6:  # jump if zero
            if load() == 0:
                ip = load()
                continue  # Skip autoincrement of ip
            offset += 1   # jump over next argument
        elif opcode == 7:  # less than
            store(1 if load() < load() else 0)
        elif opcode == 8:  # equal
            store(1 if load() == load() else 0)
        else:
            raise RuntimeError('Illegal opcode')
        # jump over all used arguments
        ip += offset


def amplifiers1(mem, phases):
    signal = 0
    for phase in phases:
        signal = next(compute(mem[:], iter((phase, signal))))
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
    """
    Generator recursion with feedback madness lies ahead!

    Computation is done by creating a chain of generators, from last to first circuit.
    The inputs to the Intcode machine is generator by the input_generator function.

    This function creates the next Intcode machine with it's own input_generator...
    The first circuit (the last in this generator chain) is special:
    It first gets a bootstrap value (0) to get everything going, then it always
    gets whatever the last circuit yielded in response. (feedback)
    """
    feedback = None

    def input_generator(amp):
        yield phases[amp]  # fist input = phase setting

        if amp == 0:  # first amp is special
            yield 0  # bootstrap input
            while True:  # feedback from last amp
                yield feedback

        # Create more amps!
        yield from compute(mem[:], input_generator(amp - 1))

    # back-to-front chain. The output of this is the output of the last amp.
    chain = compute(mem[:], input_generator(len(phases)-1))

    # Loop over all of the iterations of amplifier E and store it's output as feedback.
    # When the for loop ends, amp E has halted and returned it's last value.
    for feedback in chain:
        pass

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
