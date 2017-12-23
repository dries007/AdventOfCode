input = """The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant."""
target_floor = 4

input = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
target_floor = 4

import re

class Floor:
    def __init__(self, floor):
        self.floor = floor
        self.chips = []
        self.generators = []

    def __repr__(self):
        return '<Floor %d>' % self.floor

    def dump(self):
        print('\tChips: ', self.chips)
        print('\tGenerators: ', self.generators)
        pass

    def parse(self, input):
        for item in re.split(r', |,? and ', input):
            if item == 'nothing relevant':
                return
            match = re.match(r'a (\w+)-compatible microchip', item)
            if match:
                self.chips.append(match.group(1))
                continue
            match = re.match(r'a (\w+) generator', item)
            if match:
                self.generators.append(match.group(1))
                continue
            raise ValueError(item)

def dump():
    for name, floor in floors.items():
        print(name, 'floor:')
        floor.dump()
    print()

floors = {'first' : Floor(1), 'second': Floor(2), 'third': Floor(3), 'fourth': Floor(4)}
elevator = 1

for line in input.split('\n'):
    floor, content = re.match(r'^The (\w+) floor contains (.*)\.$', line).groups()
    floors[floor].parse(content)

dump()
