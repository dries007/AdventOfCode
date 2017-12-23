
def both(data):
    groups = 0
    garbage = False
    escaped = False
    score = 0
    count = 0
    for c in data:
        if escaped:
            escaped = False
            continue
        if c == '!':
            escaped = True
            continue
        if garbage:
            if c == '>':
                garbage = False
                continue
            count += 1
            continue
        if c == '<':
            garbage = True
        elif c == '}':
            groups -= 1
        elif c == ',':
            continue
        elif c == '{':
            groups += 1
            score += groups
        else:
            raise ValueError(c)

        # print(c, 'groups', groups, 'garbage', garbage, 'escaped', escaped)
    if garbage or escaped or groups != 0:
        raise ValueError
    # print('score', score)
    return score, count


if __name__ == '__main__':
    example_data = open('day9_example.txt').read()
    for line in example_data.splitlines():
        print("example input", line)
        print("example1:", both(line.strip()))
    input_data = open('day9_input.txt').read().strip()
    print("part1, part2:", both(input_data))
