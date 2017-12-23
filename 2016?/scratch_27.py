input = """cpy a d
cpy 4 c
cpy 633 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21"""
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

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
    # def toggle(self):
    #     return Jnz(self.a, self.b)

class Inc:
    def __init__(self, r):
        self.r = r
    def __repr__(self):
        return '%s++' % self.r
    def act(self):
        registers[self.r] += 1
        return 1
    # def toggle(self):
    #     return Dec(self.r)

class Dec:
    def __init__(self, r):
        self.r = r
    def __repr__(self):
        return '%s--' % self.r
    def act(self):
        registers[self.r] -= 1
        return 1
    # def toggle(self):
    #     return Inc(self.r)

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
    # def toggle(self):
    #     return Cpy(self.r, self.o)
#
# class Tgl:
#     def __init__(self, o):
#         self.o = o
#     def __repr__(self):
#         return 'Toggle %s' % self.o
#     def act(self):
#         if self.o in registers:
#             o = pc + registers[self.o]
#         else:
#             o = pc + int(self.o)
#         if o < 0 or o >= len(program):
#             return 1
#         program[o] = program[o].toggle()
#         print('TOGGLE', o, program[o])
#         print(*program, sep='\n')
#         return 1
#     def toggle(self):
#         return Inc(self.o)
#
class Out:
    def __init__(self, o):
        self.o = o
    def __repr__(self):
        return 'Toggle %s' % self.o
    def act(self):
        if self.o in registers:
            o = registers[self.o]
        else:
            o = int(self.o)
        output(o)
        return 1
    # def toggle(self):
    #     return Inc(self.o)

import re

cpy = re.compile(r'cpy ([a-d]|-?\d+) ([a-d])')
inc = re.compile(r'inc ([a-d])')
dec = re.compile(r'dec ([a-d])')
jnz = re.compile(r'jnz ([a-d]|-?\d+) ([a-d]|-?\d+)')
# tgl = re.compile(r'tgl ([a-d]|-?\d+)')
out = re.compile(r'out ([a-d]|-?\d+)')

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
    # match = tgl.match(line)
    # if match:
    #     program.append(Tgl(*match.groups()))
    #     continue
    match = out.match(line)
    if match:
        program.append(Out(*match.groups()))
        continue
    raise ValueError(line)

print(*program, sep='\n')

prevOut = None
def output(o):
    global prevOut
    if o != 0 and o != 1:
        raise Exception("o not 1 or 0", o)
    if prevOut is None:
        if o != 0:
            raise Exception('First out wasn\'t 0', o)
    if prevOut == 0 and o != 1:
        raise Exception('Prev was 0, o wasn\'t 1', o)
    if prevOut == 1 and o != 0:
        raise Exception('Prev was 1, o wasn\'t 0', o)
    prevOut = o
    print('Out', o)

a = 0
while True:
    try:
        pc = 0
        prevOut = None
        while pc < len(program):
            pc += program[pc].act()
        break
    except Exception as e:
        print(e)
        a += 1
        registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
        print('Inc A', registers)
