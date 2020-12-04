import re


example = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

example2 = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

example3 = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


def check1(inp):
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    missing = fields - inp.keys()
    return missing == set() or missing == {'cid'}


def check2(inp):
    fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: 150 <= int(x[:-2]) <= 193 if x.endswith('cm') else 59 <= int(x[:-2]) <= 76 if x.endswith('in') else False,
        'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: re.fullmatch(r'[0-9]{9}', x),
    }
    return fields.keys() - inp.keys() == set() and all(v(inp[k]) for k, v in fields.items())


def part1(inp):
    values = {}
    count = 0
    for line in inp.splitlines():
        if not line:
            if check1(values):
                count += 1
            values = {}
            continue
        for pair in line.split(' '):
            k, v = pair.split(':')
            values[k] = v
    if check1(values):
        count += 1
    return count


def part2(inp):
    values = {}
    count = 0
    for line in inp.splitlines():
        if not line:
            if check2(values):
                count += 1
            values = {}
            continue
        for pair in line.split(' '):
            k, v = pair.split(':')
            values[k] = v
    if check2(values):
        count += 1
    return count


def _main():
    assert part1(example) == 2
    assert part2(example2) == 0
    assert part2(example3) == 4
    print(part1(open('in4.txt').read()))
    print(part2(open('in4.txt').read()))


if __name__ == '__main__':
    _main()
