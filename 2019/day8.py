def decode_sif(width, height, data):
    layers = []
    i = iter(data)
    while True:
        try:
            layers.append([
                [int(next(i)) for _ in range(width)]
                for _ in range(height)
            ])
        except StopIteration:
            break
    return layers


def part1(width, height, data):
    layers = decode_sif(width, height, data)
    layers_str = ['\n'.join(''.join(str(x) for x in row) for row in layer) for layer in layers]
    fewest_0 = min(layers_str, key=lambda x: x.count('0'))
    solution = fewest_0.count('1') * fewest_0.count('2')
    print(solution)
    return solution


def part2(width, height, data):
    layers = decode_sif(width, height, data)
    layers_str = ['\n'.join(''.join(str(x) for x in row) for row in layer) for layer in layers]
    # print('', *layers_str, sep='\nLAYER\n')
    buffer = layers.pop(0)
    for layer in layers:
        for y, row in enumerate(layer):
            for x, val in enumerate(row):
                if buffer[y][x] == 2:
                    buffer[y][x] = val
    print('OUT')
    out = '\n'.join(''.join(str(x) for x in row) for row in buffer)
    print(out.replace('0', ' ').replace('1', '#'))


if __name__ == '__main__':
    # part1(3, 2, '123456789012')
    # with open('in8.txt') as f:
    #     part1(25, 6, f.read())
    part2(2, 2, '0222112222120000')
    with open('in8.txt') as f:
        part2(25, 6, f.read())
