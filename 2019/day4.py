
def part1(start, end):
    codes = set()
    for code in range(start, end+1):
        code_str = str(code)
        digits = [int(x) for x in code_str]

        if any(digits[i] > digits[i+1] for i in range(5)):
            continue

        if any(digits[i] == digits[i+1] for i in range(5)):
            codes.add(code)

    print(len(codes), codes)
    return len(codes)


def part2(start, end):
    codes = set()
    for code in range(start, end+1):
        code_str = str(code)
        digits = [int(x) for x in code_str]

        if any(digits[i] > digits[i+1] for i in range(5)):
            continue

        pair = False
        group_digit = None
        group_count = 0
        # print(code, code_str, digits)

        for i in range(5):
            if digits[i] == digits[i+1]:
                if group_digit == digits[i]:
                    # print('same group', code, i)
                    group_count += 1
                else:
                    if group_count == 2:
                        # print('pair after', code, i)
                        pair = True
                    group_count = 2
                    group_digit = digits[i]
                    # print('other digit', code, i)
            else:
                if group_count == 2:
                    # print('pair before', code, i)
                    pair = True
                group_count = 0
                group_digit = None
        if group_count == 2:
            # print('pair end', code)
            pair = True

        if pair:
            codes.add(code)
    print(len(codes), codes)
    return len(codes)


if __name__ == '__main__':
    part1(387638, 919123)
    part2(387638, 919123)
