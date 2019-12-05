def compute(mem, inp=None):
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
    outp = None
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
            store(inp)
        elif opcode == 4:
            # print('st')
            outp = load()
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
    return outp, mem


if __name__ == '__main__':
    print(*compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))
    print(*compute([3, 0, 4, 0, 99]))
    print(*compute([1002, 4, 3, 4, 33]))
    print(*compute([1101, 100, -1, 4, 0]))
    with open('in5.txt') as f:
        print('PART1', *compute([int(x) for x in f.read().split(',')], 1))

    print(*compute([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8))
    print(*compute([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7))
    print(*compute([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9))

    print(*compute([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8))
    print(*compute([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7))
    print(*compute([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9))

    print(*compute([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8))
    print(*compute([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8))

    with open('in5.txt') as f:
        print('PART2', *compute([int(x) for x in f.read().split(',')], 5))
