input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 12 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

# input = """cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a"""

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

import re

lines = input.split('\n')
line = 0
while line < len(lines):
    print(line, '->', lines[line], registers)
    match = re.match(r'^cpy ([a-d]|-?\d+) ([a-d])$', lines[line])
    if match:
        src = match.group(1)
        dst = match.group(2)
        if src in registers:
            src = registers[src]
        else:
            src = int(src)
        registers[dst] = src
        line += 1
        continue
    match = re.match(r'^jnz ([a-d]|1) (-?\d+)$', lines[line])
    if match:
        src = match.group(1)
        dst = int(match.group(2))
        line += dst if src == '1' or registers[src] != 0 else 1
        continue
    match = re.match(r'^inc ([a-d])$', lines[line])
    if match:
        reg = match.group(1)
        registers[reg] += 1
        line += 1
        continue
    match = re.match(r'^dec ([a-d])$', lines[line])
    if match:
        reg = match.group(1)
        registers[reg] += -1
        line += 1
        continue
    raise ValueError(lines[line])

print(registers)
