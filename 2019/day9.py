class GrowingList(list):
    # thanks https://stackoverflow.com/a/4544699
    def __setitem__(self, key, value):
        if key >= len(self):
            self.extend([0] * (key + 1 - len(self)))
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key >= len(self):
            self.extend([0] * (key + 1 - len(self)))
        return super().__getitem__(key)


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
        elif mode == 2:  # relative load
            # print(f'load immediate {parameter=}')
            return mem[parameter + rel_base]
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
        elif mode == 2:  # relative store
            mem[parameter + rel_base] = value
        else:
            raise RuntimeError('impossible store mode.')

    # Interpreter loop
    ip = 0
    rel_base = 0
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
        elif opcode == 9:  # adjust relative base
            rel_base += load()
        else:
            raise RuntimeError('Illegal opcode')
        # jump over all used arguments
        ip += offset


def part1(inp):
    mem = GrowingList(map(int, inp.split(',')))
    # print('before', mem)
    out = [x for x in compute(mem, iter((1, )))]
    print('OUT', out)
    # print('after', mem)
    print()


def part2(inp):
    mem = GrowingList(map(int, inp.split(',')))
    # print('before', mem)
    out = [x for x in compute(mem, iter((2,)))]
    print('OUT', out)
    # print('after', mem)
    print()


if __name__ == '__main__':
    # part1('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
    # part1('1102,34915192,34915192,7,4,7,99,0')
    # part1('104,1125899906842624,99')
    # with open('in9.txt') as f:
    #     part1(f.read())
    with open('in9.txt') as f:
        part2(f.read())
