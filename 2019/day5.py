def compute(mem, inp=None):
    def decode_mode():
        nonlocal offset
        # get digit at index offset+1
        mode = (instr // (10 ** (offset+1))) % 10
        val = mem[ip + offset]
        print(f'decode {instr=} {offset=} {mode=} {val=}')
        offset += 1
        return mode, val

    def load():
        print('load')
        mode, parameter = decode_mode()
        if mode == 0:
            print(f'load addr mode {parameter=} {mem[parameter]=}')
            return mem[parameter]
        elif mode == 1:
            print(f'load immediate {parameter=}')
            return parameter
        else:
            raise RuntimeError('impossible load mode')

    def store(value):
        print('store')
        mode, parameter = decode_mode()
        if mode == 0:
            print(f'store addr mode mem[{parameter=}]<-{value=}')
            mem[parameter] = value
        else:
            raise RuntimeError('impossible store mode.')

    print('START', mem)
    ip = 0
    outp = None
    while True:
        instr = mem[ip]
        opcode = instr % 100
        offset = 1
        print(f'cycle {ip=} {instr=} {opcode=}')
        if opcode == 99:
            print('Halt!')
            break
        elif opcode == 1:
            store(load() + load())
        elif opcode == 2:
            store(load() * load())
        elif opcode == 3:
            store(inp)
        elif opcode == 4:
            outp = load()
            print('Output set', outp)
        else:
            RuntimeError('Illegal opcode')

        ip += offset
    return outp, mem


def part1(mem):
    compute(mem, 1)


if __name__ == '__main__':
    # part1()
    # print(compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))
    print(compute([3, 0, 4, 0, 99]))
    print(compute([1002, 4, 3, 4, 33]))
    print(compute([1101, 100, -1, 4, 0]))
    with open('in5.txt') as f:
        part1([int(x) for x in f.read().split(',')])
