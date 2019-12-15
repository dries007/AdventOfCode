import functools
import math
from collections import namedtuple, defaultdict


example1 = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

example2 = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''

example3 = '''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''

example4 = '''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF'''

example5 = '''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''

Ingredient = namedtuple('Ingredient', ('name', 'quantity'))
Recipe = namedtuple('Recipe', ('output', 'input'))


def read_ingredient(text: str) -> Ingredient:
    q, n = text.split(' ')
    return Ingredient(n, int(q))


def read_recipes(text):
    recipes = {}
    for line in text.splitlines(keepends=False):
        inp, out = line.split(" => ")
        out = read_ingredient(out)
        recipes[out.name] = Recipe(out, [read_ingredient(x) for x in inp.split(', ')])
    return recipes


def part1(recipes, n=1):
    leftovers = defaultdict(lambda: 0)

    def resolve_recipe(name, quantity):
        # print('Resolve', quantity, name)
        if leftovers[name] >= quantity:
            # print('    Enough leftovers of', name, 'to cover', quantity)
            leftovers[name] -= quantity
            # print('    Leftovers:', *(f'{k}={v}' for k, v in leftovers.items() if v))
            return 0

        quantity -= leftovers[name]
        leftovers[name] = 0

        r: Recipe = recipes[name]
        mult = math.ceil(quantity / r.output.quantity)

        total = 0
        # print('    Resolved', quantity, name, '->', *((x.name, mult * x.quantity) for x in r.input))
        for x in r.input:
            if x.name == 'ORE':
                total += mult * x.quantity
            else:
                total += resolve_recipe(x.name, mult * x.quantity)
        # print('    Resolved', quantity, name, '->', total, 'ORE')
        leftovers[name] += (mult * r.output.quantity) - quantity
        # print('    Leftovers:', *(f'{k}={v}' for k, v in leftovers.items() if v))
        return total

    return resolve_recipe('FUEL', n)


def part2(recipes, ore):
    stepsize = 100000
    n = 1
    required_ore_old = None
    while True:
        required_ore = part1(recipes, n)
        if required_ore_old == required_ore:
            return n, required_ore
        required_ore_old = required_ore
        # print(n, required_ore)
        if required_ore > ore:
            n -= stepsize
            stepsize //= 2
        else:
            n += stepsize


if __name__ == '__main__':
    print('PART1')
    print(part1(read_recipes(example1)))
    print(part1(read_recipes(example2)))
    print(part1(read_recipes(example3)))
    print(part1(read_recipes(example4)))
    print(part1(read_recipes(example5)))
    with open('in14.txt') as f:
        recipes = read_recipes(f.read())
    print(part1(recipes))
    print('PART2')
    print(part2(read_recipes(example3), 1000000000000))
    print(part2(read_recipes(example4), 1000000000000))
    print(part2(read_recipes(example5), 1000000000000))
    print(part2(recipes, 1000000000000))

