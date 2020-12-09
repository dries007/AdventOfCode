from enum import Enum, auto


example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class Opcode(Enum):
    NOP = auto()
    ACC = auto()
    JMP = auto()

    def __repr__(self):
        return self.name


def parse(inp: str):
    return [(Opcode[op.upper()], int(arg)) for op, arg in (line.split() for line in inp.splitlines())]


def run(program: list[(Opcode,int)]) -> (int, bool):
    ip = 0
    acc = 0
    visited = set()
    while ip not in visited:
        visited.add(ip)
        op, arg = program[ip]
        if op == Opcode.NOP:
            ip += 1
        elif op == Opcode.ACC:
            acc += arg
            ip += 1
        elif op == Opcode.JMP:
            ip += arg
        else:
            raise ValueError()
        if ip >= len(program):
            return acc, True
    return acc, False


def part1(inp):
    program = parse(inp)
    # print(*program, sep='\n')
    return run(program)[0]


def part2(inp):
    program = parse(inp)

    for i, (op, arg) in enumerate(program):
        if op == Opcode.ACC:
            continue
        # Change instruction
        program[i] = (Opcode.JMP if op == Opcode.NOP else Opcode.NOP, arg)
        acc, ok = run(program)
        if ok:
            return acc
        # Revert back to original instruction
        program[i] = (op, arg)

    raise ValueError()


def _main():
    print(part1(example))
    print(part1(open('in8.txt').read()))
    print(part2(example))
    print(part2(open('in8.txt').read()))


if __name__ == '__main__':
    _main()

