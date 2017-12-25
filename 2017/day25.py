from collections import defaultdict
import re

re_begin = re.compile(r'^Begin in state ([A-Z])\.$')
re_steps = re.compile(r'^Perform a diagnostic checksum after (\d+) steps\.$')
re_state = re.compile(r'^In state ([A-Z]):$')
re_if = re.compile(r'^If the current value is (\d+):$')
re_write = re.compile(r'^- Write the value (\d+)\.$')
re_move = re.compile(r'^- Move one slot to the (right|left)\.$')
re_continue = re.compile(r'^- Continue with state ([A-Z])\.$')


class State:
    def __init__(self, name):
        self.name = name
        self.clauses = {}

    def __repr__(self):
        return '<State {}: {}>'.format(self.name, self.clauses)


class Clause:
    def __init__(self, num):
        self.num = num
        self.write = None
        self.move = None
        self.state = None

    def set_write(self, param):
        if self.write is not None:
            raise ValueError
        self.write = param

    def set_move(self, param):
        if self.move is not None:
            raise ValueError
        self.move = {'left': -1, 'right': +1}[param]

    def set_state(self, param):
        if self.state is not None:
            raise ValueError
        self.state = param

    def __repr__(self):
        return '<Clause {}, write {}, move {}, continue {}>'.format(self.num, self.write, self.move, self.state)


def parse(data):
    begin = None
    steps = None
    states = {}
    state = None
    clause = None

    for line in data.splitlines():
        line = line.strip()
        if len(line) == 0:
            continue
        m = re_state.match(line)
        if m:
            state = State(m.group(1))
            states[state.name] = state
            clause = None
            continue
        m = re_if.match(line)
        if m and state is not None:
            clause = Clause(int(m.group(1)))
            state.clauses[clause.num] = clause
            continue

        m = re_write.match(line)
        if m and clause is not None:
            clause.set_write(int(m.group(1)))
            continue
        m = re_move.match(line)
        if m and clause is not None:
            clause.set_move(m.group(1))
            continue
        m = re_continue.match(line)
        if m and clause is not None:
            clause.set_state(m.group(1))
            continue

        m = re_begin.match(line)
        if m and begin is None:
            begin = m.group(1)
            continue
        m = re_steps.match(line)
        if m and steps is None:
            steps = int(m.group(1))
            continue
        print(begin)
        print(steps)
        print(states)
        print(state)
        print(clause)
        raise Exception(line)

    return states, begin, steps


def part1(data):
    states, state, steps = parse(data)
    mem = defaultdict(lambda: 0)
    print(state, steps)
    print(*states, sep='\n')

    cursor = 0
    for loop in range(steps):
        clause = states[state].clauses[mem[cursor]]
        mem[cursor] = clause.write
        cursor += clause.move
        state = clause.state
    return sum(mem.values())


def part2(data):
    pass


if __name__ == '__main__':
    example_data = r'''Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.'''
    print("example1:", part1(example_data))
    # print("example2:", part2(example_data))
    input_data = r'''Begin in state A.
Perform a diagnostic checksum after 12261543 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.'''
    print("part1:", part1(input_data))
    # print("part2:", part2(input_data))
