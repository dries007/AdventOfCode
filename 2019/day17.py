from day9 import compute, GrowingList


def part1(mem):
    def inp():
        pass

    out = compute(mem, inp())

    screen = []
    line = ''

    for c in out:
        c = chr(c)
        if c == '\n':
            screen.append(line)
            line = ''
        else:
            line += c

    print(*screen, sep='\n')

    # screen = [
    #      "..#..........",
    #      "..#..........",
    #      "#######...###",
    #      "#.#...#...#.#",
    #      "#############",
    #      "..#...#...#..",
    #      "..#####...^..",
    # ]

    total = 0
    for y in range(1, len(screen)-1):
        for x in range(1, len(screen[y])-1):
            if screen[y][x] == '#':
                if screen[y][x-1] == '#' and screen[y][x+1] == '#' and screen[y-1][x] == '#' and screen[y+1][x] == '#':
                    print('+ at', x, y, '->', x*y)
                    total += x*y
                    screen[y] = screen[y][:x] + 'O' + screen[y][x+1:]

    print()
    print(*screen, sep='\n')
    print(total)


def part2(mem):
    main = 'B,A,B,C,B,C,A,C,C,A'
    a = 'R,4,L,4,L,4,R,8,R,10'
    b = 'L,4,L,4,L,10,R,4'
    c = 'R,4,L,10,R,10'
    video = False

    print('main', main)
    print('a', a)
    print('b', b)
    print('c', c)
    assert len(main) <= 20
    assert len(a) <= 20
    assert len(b) <= 20
    assert len(c) <= 20

    def inp():
        print('>> inputting main <<', main)
        for x in main:
            yield ord(x)
        yield ord('\n')
        print('>> inputting a <<', a)
        for x in a:
            yield ord(x)
        yield ord('\n')
        print('>> inputting b <<', b)
        for x in b:
            yield ord(x)
        yield ord('\n')
        print('>> inputting c <<', c)
        for x in c:
            yield ord(x)
        yield ord('\n')
        print('>> inputting video <<', video)
        yield ord('y' if video else 'n')
        yield ord('\n')

    mem[0] = 2
    out = compute(mem, inp())

    for x in out:
        print(chr(x), end='')
        if x > 127:
            print(x)


if __name__ == '__main__':
    # with open('in17.txt') as f:
    #     part1(GrowingList(int(x) for x in f.read().split(',')))
    with open('in17.txt') as f:
        part2(GrowingList(int(x) for x in f.read().split(',')))


"""
1←←←0
↓
↓
↓
2→→→→→→→→→3   d→→→→→→→→→→
          ↓   ↑
          ↓   ↑
          ↓   ↑
      5←←←4   ↑
      ↓       ↑
      ↓       ↑ N→→→→→→→→→O   R→→→→→→→S
      ↓       ↑ ↑         ↓   ↑       ↓
      6→→→7   c←←←b       ↓   ↑       ↓
          ↓     ↑ ↑       ↓   ↑       ↓
    C→→→D ↓     ↑ ↑       P→→→Q       ↓
    ↑   ↓ ↓     ↑ ↑                   ↓
    ↑   ↓ ↓   Z→→→a                   ↓
    ↑   ↓ ↓   ↑ ↑                     ↓
    ↑   E→→→→→→→→→F                   ↓
    ↑     ↓   ↑ ↑ ↓                   ↓
9←←←←←←←←←8 L→→→M ↓               U←←←T
↓   ↑       ↑ ↑   ↓               ↓
↓   ↑       ↑ ↑   ↓               ↓
↓   ↑       ↑ ↑   ↓               ↓
A→→→B       J←←←←←↓←←←I           ↓
              ↑   ↓   ↑           ↓
              Y←←←↓←←←↑←X         ↓
                  ↓   ↑ ↑         ↓
                  G→→→H ↑         ↓
                        ↑         ↓
                        W←←←←←←←←←V

0   1   2    3   4   5   6   7   8    9   A   B    C   D   E    F    G   H   I    J   L   M    N    O   P   Q   R   S    T   U    V    W   X    Y    Z   a   b   c   d
L,4,L,4,L,10,R,4,R,4,L,4,L,4,R,8,R,10,L,4,L,4,L,10,R,4,R,4,L,10,R,10,L,4,L,4,L,10,R,4,R,4,L,10,R,10,R,4,L,4,L,4,R,8,R,10,R,4,L,10,R,10,R,4,L,10,R,10,R,4,L,4,L,4,R,8,R,10
L,4,L,4,L,10,R,4,        A           ,L,4,L,4,L,10,R,4,R,4,L,10,R,10,L,4,L,4,L,10,R,4,R,4,L,10,R,10,        A           ,R,4,L,10,R,10,R,4,L,10,R,10,        A
        B       ,        A           ,        B       ,    C        ,      B         ,    C        ,        A           ,    C        ,    C        ,        A


Main:   B,A,B,C,B,C,A,C,C,A
A:      R,4,L,4,L,4,R,8,R,10
B:      L,4,L,4,L,10,R,4
C:      R,4,L,10,R,10
"""

