def solution(H):
    print("INPUT", H)

    def thing_do(a, b):
        print("Thing DO: ", a, b)

        current = a[0]
        del a[0]
        steps = 1

        while True:
            print('STEP a->b', current, a, b)

            while b[0] < current:
                del b[0]
                if not b:
                    print("No more higher nests on B: ", steps)
                    return steps

            steps += 1
            current = b[0]
            del b[0]

            print('STEP b->a', current, a, b)

            if not a:
                print("Last step was a A", steps)
                return steps

            while a[0] < current:
                del a[0]
                if not a:
                    print("No more higher nests on A: ", steps)
                    return steps

            steps += 1
            current = a[0]
            del a[0]

            if not b:
                print("Last step was a B", steps)
                return steps



    def thing(left, right):
        return max(thing_do(left[:], right[:]), thing_do(right[:], left[:]))

    longest = 0

    for pos in range(1, len(H)):
        print()
        x = thing(sorted(H[pos:]), sorted(H[:pos]))
        longest = x if x > longest else longest
        print("Nest", x , "Longest:", longest)

    return longest % ((10 ** 9) + 7)


print("SOLUTION: ", solution([13, 2, 5]))
print()
print()
print()
print()
print("SOLUTION: ", solution([4, 6, 2, 1, 5]))
