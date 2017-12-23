input = """cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 74 c
jnz 88 d
inc a
inc d
jnz d -2
inc c
jnz c -5"""
# registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

# input = """cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a"""
# registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

class Cpy:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return '%s->%s' % (self.a, self.b)
    def act(self):
        if self.a in registers:
            src = registers[self.a]
        else:
            src = int(self.a)
        registers[self.b] = src
        return 1
    def toggle(self):
        return Jnz(self.a, self.b)

class Inc:
    def __init__(self, r):
        self.r = r
    def __repr__(self):
        return '%s++' % self.r
    def act(self):
        registers[self.r] += 1
        return 1
    def toggle(self):
        return Dec(self.r)

class Dec:
    def __init__(self, r):
        self.r = r
    def __repr__(self):
        return '%s--' % self.r
    def act(self):
        registers[self.r] -= 1
        return 1
    def toggle(self):
        return Inc(self.r)

class Jnz:
    def __init__(self, r, o):
        self.r = r
        self.o = o
    def __repr__(self):
        return 'if !%s -> %s' % (self.r, self.o)
    def act(self):
        if self.o in registers:
            o = registers[self.o]
        else:
            o = int(self.o)
        if self.r in registers:
            if registers[self.r] != 0:
                return o
        elif int(self.r) != 0:
            return o
        return 1
    def toggle(self):
        return Cpy(self.r, self.o)

class Tgl:
    def __init__(self, o):
        self.o = o
    def __repr__(self):
        return 'Toggle %s' % self.o
    def act(self):
        if self.o in registers:
            o = pc + registers[self.o]
        else:
            o = pc + int(self.o)
        if o < 0 or o >= len(program):
            return 1
        program[o] = program[o].toggle()
        print('TOGGLE', o, program[o])
        print(*program, sep='\n')
        return 1
    def toggle(self):
        return Inc(self.o)

import re

cpy = re.compile(r'cpy ([a-d]|-?\d+) ([a-d])')
inc = re.compile(r'inc ([a-d])')
dec = re.compile(r'dec ([a-d])')
jnz = re.compile(r'jnz ([a-d]|-?\d+) ([a-d]|-?\d+)')
tgl = re.compile(r'tgl ([a-d]|-?\d+)')

program = []

for line in input.split('\n'):
    match = cpy.match(line)
    if match:
        program.append(Cpy(*match.groups()))
        continue
    match = inc.match(line)
    if match:
        program.append(Inc(*match.groups()))
        continue
    match = dec.match(line)
    if match:
        program.append(Dec(*match.groups()))
        continue
    match = jnz.match(line)
    if match:
        program.append(Jnz(*match.groups()))
        continue
    match = tgl.match(line)
    if match:
        program.append(Tgl(*match.groups()))
        continue
    raise ValueError(line)

print(*program, sep='\n')

print('START')

pc = 0
while pc < len(program):
    pc += program[pc].act()
    print(registers)

print('END')

print(registers)