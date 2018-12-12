import re

example = r'''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>'''

input='''position=<-40409, -50575> velocity=< 4,  5>
position=<-40416, -50576> velocity=< 4,  5>
position=<-20124, -50573> velocity=< 2,  5>
position=< 40720,  -9995> velocity=<-4,  1>
position=< 50896, -20148> velocity=<-5,  2>
position=<-40449, -50575> velocity=< 4,  5>
position=< 50864,  40716> velocity=<-5, -4>
position=<-40412,  40722> velocity=< 4, -4>
position=< 30609,  40720> velocity=<-3, -4>
position=<-20153, -40428> velocity=< 2,  4>
position=<-50551,  30572> velocity=< 5, -3>
position=< 20464, -50580> velocity=<-2,  5>
position=< 10303, -30286> velocity=<-1,  3>
position=< 50895, -40432> velocity=<-5,  4>
position=<-10009, -40436> velocity=< 1,  4>
position=< 40747,  10293> velocity=<-4, -1>
position=<-50545,  50861> velocity=< 5, -5>
position=< 20415,  40719> velocity=<-2, -4>
position=< 50895, -50575> velocity=<-5,  5>
position=< 50895,  10293> velocity=<-5, -1>
position=<-10016,  10284> velocity=< 1, -1>
position=< 30567,  -9997> velocity=<-3,  1>
position=< 30554, -40436> velocity=<-3,  4>
position=< 20432,  20428> velocity=<-2, -2>
position=<-40401, -50573> velocity=< 4,  5>
position=< 50880, -20144> velocity=<-5,  2>
position=< 40707, -20148> velocity=<-4,  2>
position=<-30297, -50578> velocity=< 3,  5>
position=< 10271, -20147> velocity=<-1,  2>
position=< 50879, -50577> velocity=<-5,  5>
position=< 10321,  50869> velocity=<-1, -5>
position=< 40706,  -9999> velocity=<-4,  1>
position=< 10276, -50579> velocity=<-1,  5>
position=< 10298,  10293> velocity=<-1, -1>
position=< 30561,  20437> velocity=<-3, -2>
position=<-10025, -50576> velocity=< 1,  5>
position=< 40751, -40427> velocity=<-4,  4>
position=< 10275,  -9999> velocity=<-1,  1>
position=< -9965, -10004> velocity=< 1,  1>
position=< 10308,  40716> velocity=<-1, -4>
position=< 30551,  20431> velocity=<-3, -2>
position=< 30587,  40725> velocity=<-3, -4>
position=<-50577, -30292> velocity=< 5,  3>
position=<-50556,  40717> velocity=< 5, -4>
position=< 50871,  50862> velocity=<-5, -5>
position=< 30578,  30576> velocity=<-3, -3>
position=<-40444, -30287> velocity=< 4,  3>
position=<-30273, -30290> velocity=< 3,  3>
position=< 40699, -30287> velocity=<-4,  3>
position=< 30602,  50860> velocity=<-3, -5>
position=< -9969, -20144> velocity=< 1,  2>
position=<-30256, -10004> velocity=< 3,  1>
position=<-30297, -40436> velocity=< 3,  4>
position=< 20460,  50861> velocity=<-2, -5>
position=< 30588, -30283> velocity=<-3,  3>
position=<-30265, -50579> velocity=< 3,  5>
position=< 10291,  30575> velocity=<-1, -3>
position=< 20412, -20143> velocity=<-2,  2>
position=<-30301, -40436> velocity=< 3,  4>
position=< 20458, -50571> velocity=<-2,  5>
position=< -9966,  50869> velocity=< 1, -5>
position=<-30280, -30283> velocity=< 3,  3>
position=<-20169, -20145> velocity=< 2,  2>
position=< 50895,  50860> velocity=<-5, -5>
position=<-30268, -30287> velocity=< 3,  3>
position=< 40754,  10284> velocity=<-4, -1>
position=< 20415, -30287> velocity=<-2,  3>
position=< 10268,  20436> velocity=<-1, -2>
position=<-50597,  10292> velocity=< 5, -1>
position=< 20407,  10289> velocity=<-2, -1>
position=<-50542, -40427> velocity=< 5,  4>
position=<-50598,  -9995> velocity=< 5,  1>
position=< 50888,  20437> velocity=<-5, -2>
position=<-20121,  -9996> velocity=< 2,  1>
position=<-30253, -30283> velocity=< 3,  3>
position=<-50585,  10284> velocity=< 5, -1>
position=<-40457,  10285> velocity=< 4, -1>
position=<-40452,  20435> velocity=< 4, -2>
position=<-20161,  -9998> velocity=< 2,  1>
position=< 20452,  20429> velocity=<-2, -2>
position=<-50593, -50579> velocity=< 5,  5>
position=< 40751,  30580> velocity=<-4, -3>
position=< 40719,  50867> velocity=<-4, -5>
position=<-20121, -50578> velocity=< 2,  5>
position=< 10321,  10284> velocity=<-1, -1>
position=<-50541, -30288> velocity=< 5,  3>
position=< 50847,  -9996> velocity=<-5,  1>
position=< 30555, -40431> velocity=<-3,  4>
position=< 10268,  20436> velocity=<-1, -2>
position=< 40711, -20143> velocity=<-4,  2>
position=< 10295, -50574> velocity=<-1,  5>
position=< 20464,  50869> velocity=<-2, -5>
position=<-40429,  50860> velocity=< 4, -5>
position=< 10271, -20141> velocity=<-1,  2>
position=<-40457,  -9998> velocity=< 4,  1>
position=< 20420,  20433> velocity=<-2, -2>
position=<-30254,  50864> velocity=< 3, -5>
position=< 30583, -50571> velocity=<-3,  5>
position=< 10308,  30578> velocity=<-1, -3>
position=< 40743, -20141> velocity=<-4,  2>
position=< 10311, -40430> velocity=<-1,  4>
position=< 10279, -20139> velocity=<-1,  2>
position=<-50541, -40436> velocity=< 5,  4>
position=<-30312, -40427> velocity=< 3,  4>
position=< 30608, -50571> velocity=<-3,  5>
position=< 50889,  40716> velocity=<-5, -4>
position=<-40452, -30285> velocity=< 4,  3>
position=<-40417, -20146> velocity=< 4,  2>
position=< 30593, -20144> velocity=<-3,  2>
position=< 50848,  50869> velocity=<-5, -5>
position=< 10263,  40722> velocity=<-1, -4>
position=<-30293,  20437> velocity=< 3, -2>
position=<-20124,  40723> velocity=< 2, -4>
position=<-50556, -20145> velocity=< 5,  2>
position=< 50857, -40427> velocity=<-5,  4>
position=<-30260,  30580> velocity=< 3, -3>
position=<-20156, -30286> velocity=< 2,  3>
position=<-40417,  30579> velocity=< 4, -3>
position=< -9993,  40721> velocity=< 1, -4>
position=< 30578, -50576> velocity=<-3,  5>
position=< 30556,  -9995> velocity=<-3,  1>
position=< -9977, -30291> velocity=< 1,  3>
position=< 20420, -50571> velocity=<-2,  5>
position=<-40428, -30291> velocity=< 4,  3>
position=< 40731,  10293> velocity=<-4, -1>
position=< 50855,  20434> velocity=<-5, -2>
position=<-20169, -50577> velocity=< 2,  5>
position=< 30575,  30579> velocity=<-3, -3>
position=< 10308,  50862> velocity=<-1, -5>
position=< 30578, -50571> velocity=<-3,  5>
position=<-40409, -40433> velocity=< 4,  4>
position=< 50884, -30284> velocity=<-5,  3>
position=< 50852, -50573> velocity=<-5,  5>
position=< 20439,  40719> velocity=<-2, -4>
position=<-40452,  10290> velocity=< 4, -1>
position=<-50597,  30572> velocity=< 5, -3>
position=< 10287,  40725> velocity=<-1, -4>
position=< 40743,  30577> velocity=<-4, -3>
position=<-30257, -40429> velocity=< 3,  4>
position=< -9969,  40721> velocity=< 1, -4>
position=<-20137, -50571> velocity=< 2,  5>
position=< 40695, -50576> velocity=<-4,  5>
position=< 40716, -50571> velocity=<-4,  5>
position=<-50593,  50864> velocity=< 5, -5>
position=< 10324,  50860> velocity=<-1, -5>
position=< 10296,  -9995> velocity=<-1,  1>
position=<-50561,  40722> velocity=< 5, -4>
position=< -9967,  30576> velocity=< 1, -3>
position=< -9985,  30579> velocity=< 1, -3>
position=<-20140, -30292> velocity=< 2,  3>
position=<-50569, -30291> velocity=< 5,  3>
position=< 30593,  10288> velocity=<-3, -1>
position=<-40425, -20145> velocity=< 4,  2>
position=< 10311,  40719> velocity=<-1, -4>
position=< -9985,  10287> velocity=< 1, -1>
position=< 30553, -50580> velocity=<-3,  5>
position=< 40743, -50572> velocity=<-4,  5>
position=< 50857, -30283> velocity=<-5,  3>
position=< 30591,  20428> velocity=<-3, -2>
position=< 30567,  30576> velocity=<-3, -3>
position=<-20137, -40436> velocity=< 2,  4>
position=< 10288,  50860> velocity=<-1, -5>
position=< 10312, -50580> velocity=<-1,  5>
position=<-50596,  20429> velocity=< 5, -2>
position=<-30303, -30292> velocity=< 3,  3>
position=< 50867,  20437> velocity=<-5, -2>
position=<-30302, -50575> velocity=< 3,  5>
position=< 20423,  20430> velocity=<-2, -2>
position=< -9985, -30284> velocity=< 1,  3>
position=< 50873, -40427> velocity=<-5,  4>
position=< -9969,  10287> velocity=< 1, -1>
position=< -9968,  50864> velocity=< 1, -5>
position=< 20433, -50571> velocity=<-2,  5>
position=<-30257,  50869> velocity=< 3, -5>
position=<-20142, -30283> velocity=< 2,  3>
position=<-20156,  40721> velocity=< 2, -4>
position=< 10280,  30581> velocity=<-1, -3>
position=< 30562,  30572> velocity=<-3, -3>
position=< 30583,  -9999> velocity=<-3,  1>
position=< 40723,  30572> velocity=<-4, -3>
position=<-40447, -10004> velocity=< 4,  1>
position=< 10263, -50572> velocity=<-1,  5>
position=< 50900,  10293> velocity=<-5, -1>
position=<-20129, -20140> velocity=< 2,  2>
position=<-50556, -20146> velocity=< 5,  2>
position=<-30255, -40436> velocity=< 3,  4>
position=< 50850,  -9999> velocity=<-5,  1>
position=<-40417, -30284> velocity=< 4,  3>
position=<-10025,  10292> velocity=< 1, -1>
position=<-30253,  50869> velocity=< 3, -5>
position=<-10017, -40435> velocity=< 1,  4>
position=<-40417,  50863> velocity=< 4, -5>
position=<-10020,  40722> velocity=< 1, -4>
position=< 50839, -50575> velocity=<-5,  5>
position=< 30585, -20139> velocity=<-3,  2>
position=<-50600, -20148> velocity=< 5,  2>
position=< 20407, -30285> velocity=<-2,  3>
position=<-20142, -30292> velocity=< 2,  3>
position=< 40711,  10292> velocity=<-4, -1>
position=< 40722,  50869> velocity=<-4, -5>
position=< 30607, -20140> velocity=<-3,  2>
position=<-10015, -40436> velocity=< 1,  4>
position=<-30257,  50863> velocity=< 3, -5>
position=<-30273, -30288> velocity=< 3,  3>
position=< 20436, -20148> velocity=<-2,  2>
position=<-40397, -10000> velocity=< 4,  1>
position=<-30305, -40434> velocity=< 3,  4>
position=<-20129,  40723> velocity=< 2, -4>
position=< 50887,  20436> velocity=<-5, -2>
position=< 20457,  30581> velocity=<-2, -3>
position=<-50582,  30581> velocity=< 5, -3>
position=< 50895, -30288> velocity=<-5,  3>
position=<-40449,  50867> velocity=< 4, -5>
position=<-10001,  30580> velocity=< 1, -3>
position=<-20145,  20436> velocity=< 2, -2>
position=< 20439,  40716> velocity=<-2, -4>
position=< 20420, -40428> velocity=<-2,  4>
position=< 10311, -40431> velocity=<-1,  4>
position=< -9996,  50861> velocity=< 1, -5>
position=< -9972, -30291> velocity=< 1,  3>
position=< 30580,  10284> velocity=<-3, -1>
position=< -9969, -30290> velocity=< 1,  3>
position=< 40698,  -9999> velocity=<-4,  1>
position=<-30300,  -9995> velocity=< 3,  1>
position=<-50593, -50573> velocity=< 5,  5>
position=<-20153,  20434> velocity=< 2, -2>
position=<-40397,  40725> velocity=< 4, -4>
position=< -9980, -40431> velocity=< 1,  4>
position=< 30575, -50572> velocity=<-3,  5>
position=<-50542,  40720> velocity=< 5, -4>
position=<-30287,  30572> velocity=< 3, -3>
position=<-50569,  -9997> velocity=< 5,  1>
position=<-50601, -30287> velocity=< 5,  3>
position=< 40740, -20142> velocity=<-4,  2>
position=< 20407,  50862> velocity=<-2, -5>
position=<-20113, -50574> velocity=< 2,  5>
position=< 40715, -30283> velocity=<-4,  3>
position=<-30265,  10288> velocity=< 3, -1>
position=<-40441,  20431> velocity=< 4, -2>
position=< -9991,  50869> velocity=< 1, -5>
position=< 40721, -50580> velocity=<-4,  5>
position=< -9985, -30286> velocity=< 1,  3>
position=< 10289,  -9995> velocity=<-1,  1>
position=< 10308, -40432> velocity=<-1,  4>
position=<-20137, -10004> velocity=< 2,  1>
position=<-40457, -30288> velocity=< 4,  3>
position=<-30281,  -9996> velocity=< 3,  1>
position=< 50895, -20145> velocity=<-5,  2>
position=< 30599,  50867> velocity=<-3, -5>
position=< 10303,  10289> velocity=<-1, -1>
position=<-40440, -40427> velocity=< 4,  4>
position=<-20152, -30283> velocity=< 2,  3>
position=< 50876,  30581> velocity=<-5, -3>
position=<-10023,  50869> velocity=< 1, -5>
position=< 20417,  30581> velocity=<-2, -3>
position=< 40724, -50578> velocity=<-4,  5>
position=< 20452, -40436> velocity=<-2,  4>
position=<-50585,  40721> velocity=< 5, -4>
position=< 30610,  30572> velocity=<-3, -3>
position=<-20157,  30577> velocity=< 2, -3>
position=< 30577, -30287> velocity=<-3,  3>
position=<-30265, -30291> velocity=< 3,  3>
position=<-40445, -20140> velocity=< 4,  2>
position=< 40751,  30572> velocity=<-4, -3>
position=< 40727, -50577> velocity=<-4,  5>
position=< 30596,  10286> velocity=<-3, -1>
position=<-30289,  30572> velocity=< 3, -3>
position=< 50887, -20146> velocity=<-5,  2>
position=<-30313,  -9997> velocity=< 3,  1>
position=< 40703,  30574> velocity=<-4, -3>
position=< -9982, -30288> velocity=< 1,  3>
position=< 30596, -30291> velocity=<-3,  3>
position=< 10319,  30572> velocity=<-1, -3>
position=< 40708,  -9997> velocity=<-4,  1>
position=< 50871,  10286> velocity=<-5, -1>
position=< 10308, -30283> velocity=<-1,  3>
position=< 30591, -40435> velocity=<-3,  4>
position=< 50847, -50575> velocity=<-5,  5>
position=< 40720,  40722> velocity=<-4, -4>
position=< 30556,  40723> velocity=<-3, -4>
position=<-20113, -20143> velocity=< 2,  2>
position=< 20423,  10290> velocity=<-2, -1>
position=< -9985, -40431> velocity=< 1,  4>
position=<-50557, -30288> velocity=< 5,  3>
position=< 20442,  20437> velocity=<-2, -2>
position=< 30567,  30577> velocity=<-3, -3>
position=< 20459, -10004> velocity=<-2,  1>
position=< 40745,  30572> velocity=<-4, -3>
position=<-40399, -50580> velocity=< 4,  5>
position=< 30556, -20143> velocity=<-3,  2>
position=<-50561,  10293> velocity=< 5, -1>
position=< 40740, -40433> velocity=<-4,  4>
position=<-50577, -50573> velocity=< 5,  5>
position=<-30281, -20139> velocity=< 3,  2>
position=< 40724,  40725> velocity=<-4, -4>
position=< -9973,  40725> velocity=< 1, -4>
position=< 50867,  10293> velocity=<-5, -1>
position=<-20137, -40432> velocity=< 2,  4>
position=<-40441,  50861> velocity=< 4, -5>
position=< -9966,  50864> velocity=< 1, -5>
position=<-40401, -20140> velocity=< 4,  2>
position=<-10000,  20434> velocity=< 1, -2>
position=< 30564, -40429> velocity=<-3,  4>
position=<-30302,  10293> velocity=< 3, -1>'''

RE_LINE = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>', re.IGNORECASE)


class Point:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return '<{:2};{:2}@{:2};{:2}>'.format(self.px, self.py, self.vx, self.vy)

    def move(self):
        self.px += self.vx
        self.py += self.vy


def day10(inp):
    points = [Point(*map(int, RE_LINE.match(l).groups())) for l in inp.splitlines() if len(l)]

    i = 0
    min_size = None

    while True:
        min_x = min(points, key=lambda x: x.px).px
        min_y = min(points, key=lambda x: x.py).py
        max_x = max(points, key=lambda x: x.px).px
        max_y = max(points, key=lambda x: x.py).py
        size = (max_x-min_x) * (max_y-min_y)

        if min_size and size > min_size:
            grid = [[' ' for x in range(min_x - 1, max_x + 1)] for y in range(min_y - 1, max_y + 1)]
            for p in points:
                grid[-min_y + p.py-p.vy][-min_x + p.px-p.vx] = '#'
            print('After', i-1, 'seconds')
            print(*(''.join(line) for line in grid), sep='\n')
            break

        min_size = size
        for p in points:
            p.move()
        i += 1

    return points, i


if __name__ == '__main__':
    print(day10(example))
    print(day10(input))