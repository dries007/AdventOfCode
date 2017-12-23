from collections import defaultdict
from queue import Queue
import threading
import time


def part1(data):
    prog = data.splitlines()
    size = len(prog)
    mem = defaultdict(lambda: 0)
    pc = 0
    last_freq = 0

    def get(arg):
        try:
            return int(arg)
        except:
            return mem[arg]

    while pc < size:
        inst = prog[pc].split()
        pc += 1

        if inst[0] == 'snd':
            last_freq = get(inst[1])
        elif inst[0] == 'set':
            mem[inst[1]] = get(inst[2])
        elif inst[0] == 'add':
            mem[inst[1]] += get(inst[2])
        elif inst[0] == 'mul':
            mem[inst[1]] *= get(inst[2])
        elif inst[0] == 'mod':
            mem[inst[1]] %= get(inst[2])
        elif inst[0] == 'rcv':
            if get(inst[1]) != 0:
                print('recover', last_freq)
                return last_freq
        elif inst[0] == 'jgz':
            if get(inst[1]) != 0:
                pc += get(inst[2]) - 1

        # print(inst, mem)


class Program:
    def __init__(self, prog, pid, pipe=None, out=None):
        self.out = out
        self.prog = prog
        self.qin = pipe
        self.pid = pid

        self.size = len(prog)
        self.mem = defaultdict(lambda: 0)
        self.mem['p'] = self.pid
        self.counter = 0
        self.pc = 0
        self.blocked = False
        self.qout = Queue()

        self.die = False

    def get(self, arg):
        try:
            return int(arg)
        except:
            return self.mem[arg]

    def run(self):
        while 0 <= self.pc < self.size and not self.die:
            inst = self.prog[self.pc]
            self.pc += 1

            if inst[0] == 'snd':
                self.counter += 1
                if self.out is not None:
                    self.out.put(self.counter)
                self.qout.put(self.get(inst[1]))
            elif inst[0] == 'set':
                self.mem[inst[1]] = self.get(inst[2])
            elif inst[0] == 'add':
                self.mem[inst[1]] += self.get(inst[2])
            elif inst[0] == 'mul':
                self.mem[inst[1]] *= self.get(inst[2])
            elif inst[0] == 'mod':
                self.mem[inst[1]] %= self.get(inst[2])
            elif inst[0] == 'rcv':
                self.blocked = True
                self.mem[inst[1]] = self.qin.get()
                self.blocked = False
            elif inst[0] == 'jgz':
                if self.get(inst[1]) != 0:
                    self.pc += self.get(inst[2]) - 1


def part2(data):
    q = Queue()
    p0 = Program([x.split() for x in data.splitlines()], 0)
    p1 = Program([x.split() for x in data.splitlines()], 1, p0.qout, q)
    p0.qin = p1.qout

    tp0 = threading.Thread(target=p0.run)
    tp1 = threading.Thread(target=p1.run)

    tp0.start()
    tp1.start()

    while True:
        print(q.get())

    # import time
    # while not (p0.blocked and p1.blocked):
    #     time.sleep(10)
    #     while not (p0.blocked and p1.blocked):
    #         time.sleep(10)
    #         while not (p0.blocked and p1.blocked):
    #             time.sleep(10)
    #         time.sleep(10)
    #     time.sleep(10)

    # p0.die = p1.die = True
    # p0.qin.put(None)
    # p1.qin.put(None)

    print("DEADLOCK")

    return p1.counter


if __name__ == '__main__':
    example_data = r'''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''
    print("example1:", part1(example_data))
    example_data = r'''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''
    # print("example2:", part2(example_data))
    input_data = r'''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))
