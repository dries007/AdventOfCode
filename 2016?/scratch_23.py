keyword = 'fbgdceah'
instructions = """rotate right 3 steps
swap position 7 with position 0
rotate left 3 steps
reverse positions 2 through 5
move position 6 to position 3
reverse positions 0 through 4
swap position 4 with position 2
rotate based on position of letter d
rotate right 0 steps
move position 7 to position 5
swap position 4 with position 5
swap position 3 with position 5
move position 5 to position 3
swap letter e with letter f
swap position 6 with position 3
swap letter a with letter e
reverse positions 0 through 1
reverse positions 0 through 4
swap letter c with letter e
reverse positions 1 through 7
rotate right 1 step
reverse positions 6 through 7
move position 7 to position 1
move position 4 to position 0
move position 4 to position 6
move position 6 to position 3
swap position 1 with position 6
swap position 5 with position 7
swap position 2 with position 5
swap position 6 with position 5
swap position 2 with position 4
reverse positions 2 through 6
reverse positions 3 through 5
move position 3 to position 5
reverse positions 1 through 5
rotate left 1 step
move position 4 to position 5
swap letter c with letter b
swap position 2 with position 1
reverse positions 3 through 4
swap position 3 with position 4
reverse positions 5 through 7
swap letter b with letter d
reverse positions 3 through 4
swap letter c with letter h
rotate based on position of letter b
rotate based on position of letter e
rotate right 3 steps
rotate right 7 steps
rotate left 2 steps
move position 6 to position 1
reverse positions 1 through 3
rotate based on position of letter b
reverse positions 0 through 4
swap letter g with letter c
move position 1 to position 5
rotate right 4 steps
rotate left 2 steps
move position 7 to position 2
rotate based on position of letter c
move position 6 to position 1
swap letter f with letter g
rotate right 6 steps
swap position 6 with position 2
reverse positions 2 through 6
swap position 3 with position 1
rotate based on position of letter h
reverse positions 2 through 5
move position 1 to position 3
rotate right 1 step
rotate right 7 steps
move position 6 to position 3
rotate based on position of letter h
swap letter d with letter h
rotate left 0 steps
move position 1 to position 2
swap letter a with letter g
swap letter a with letter g
swap position 4 with position 2
rotate right 1 step
rotate based on position of letter b
swap position 7 with position 1
rotate based on position of letter e
move position 1 to position 4
move position 6 to position 3
rotate left 3 steps
swap letter f with letter g
swap position 3 with position 1
swap position 4 with position 3
swap letter f with letter c
rotate left 3 steps
rotate left 0 steps
rotate right 3 steps
swap letter d with letter e
swap position 2 with position 7
move position 3 to position 6
swap position 7 with position 1
swap position 3 with position 6
rotate left 5 steps
swap position 2 with position 6"""

import collections
import re

swapPosition = re.compile(r'swap position (\d+) with position (\d+)')
swapLetter = re.compile(r'swap letter (\w) with letter (\w)')
rotateAbs = re.compile(r'rotate (left|right) (\d+) steps?')
rotateRel = re.compile(r'rotate based on position of letter (\w)')
reverse = re.compile(r'reverse positions (\d+) through (\d+)')
move = re.compile(r'move position (\d+) to position (\d+)')

keyword = list(keyword)

for instruction in reversed(instructions.split('\n')):
    print(''.join(keyword), end='\t')

    if swapPosition.match(instruction):
        p1, p2 = map(int, swapPosition.match(instruction).groups())
        print('Swap Positions', p1, p2)

        tmp = keyword[p1]
        keyword[p1] = keyword[p2]
        keyword[p2] = tmp

    elif swapLetter.match(instruction):
        p1, p2 = map(keyword.index, swapLetter.match(instruction).groups())
        print('Swap Letters', p1, p2)

        tmp = keyword[p1]
        keyword[p1] = keyword[p2]
        keyword[p2] = tmp

    elif rotateAbs.match(instruction):
        direction, steps = rotateAbs.match(instruction).groups()
        steps = int(steps)
        print('Rotate Absolute', direction, steps)

        if direction == 'left':
            steps = -steps

        keyword = collections.deque(keyword)
        keyword.rotate(steps)
        keyword = list(keyword)

    elif rotateRel.match(instruction):
        steps = keyword.index(rotateRel.match(instruction).groups()[0])
        if steps >= 4:
            steps += 1
        steps += 1
        print('Rotate Relative', steps)

        keyword = collections.deque(keyword)
        keyword.rotate(steps)
        keyword = list(keyword)

    elif reverse.match(instruction):
        p1, p2 = map(int, reverse.match(instruction).groups())
        print('Reverse', p1, p2)

        keyword[p1:p2+1] = keyword[p1:p2+1][::-1]

    elif move.match(instruction):
        p1, p2 = map(int, move.match(instruction).groups())
        print('Move', p1, p2)

        tmp = keyword[p1]
        keyword.remove(keyword[p1])
        keyword.insert(p2, tmp)

    else:
        raise ValueError("Instruction '" + instruction + "' unknown.")


print('Final keyword', ''.join(keyword))
