def part1():
    total = 0
    with open('in1.txt') as f:
        for line in f.readlines():
            mass = int(line)
            fuel = mass // 3 - 2
            total += fuel
    print('part 1:', total)
    return total


def fuel_for_fuel(mass):
    total = 0
    while True:
        mass = mass // 3 - 2
        print('    add', mass)
        if mass > 0:
            total += mass
        else:
            break
    print('fuel_for_fuel:', total)
    return total


def part2():
    total = 0
    with open('in1.txt') as f:
        for line in f.readlines():
            mass = int(line)
            fuel = mass // 3 - 2
            total += fuel
            total += fuel_for_fuel(fuel)
    print('part 2:', total)
    return total


if __name__ == '__main__':
    part1()
    fuel_for_fuel(14)
    fuel_for_fuel(1969)
    fuel_for_fuel(100756)
    part2()

