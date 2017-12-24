
def strength(bridge):
    return sum(sum(c) for c in bridge)


def find_component(last: int, ports: list, chain: list, combinations: list):
    combinations.append((len(chain), strength(chain)))
    for port in ports:
        if last in port:
            new_last = port[1] if last == port[0] else port[0]
            new_ports = ports[:]
            new_ports.remove(port)
            new_chain = chain[:]
            new_chain.append(port)
            find_component(new_last, new_ports, new_chain, combinations)


def part12(data):
    ports = [(*map(int, x.split('/')), ) for x in data.splitlines()]
    combinations = []

    find_component(0, ports, [], combinations)

    combinations.sort(key=lambda x: x[0] * 1000000 + x[1])
    combinations.reverse()

    # print(*combinations, sep='\n')

    return max(map(lambda x: x[1], combinations)), combinations[0][1]


if __name__ == '__main__':
    example_data = r'''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''
    print("example1:", part12(example_data))
    input_data = r'''42/37
28/28
29/25
45/8
35/23
49/20
44/4
15/33
14/19
31/44
39/14
25/17
34/34
38/42
8/42
15/28
0/7
49/12
18/36
45/45
28/7
30/43
23/41
0/35
18/9
3/31
20/31
10/40
0/22
1/23
20/47
38/36
15/8
34/32
30/30
30/44
19/28
46/15
34/50
40/20
27/39
3/14
43/45
50/42
1/33
6/39
46/44
22/35
15/20
43/31
23/23
19/27
47/15
43/43
25/36
26/38
1/10'''
    print("part12:", part12(input_data))
