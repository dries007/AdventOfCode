passcode = "vwbaicqe" # actual input

# passcode = "hijkl"    # explanation
# passcode = "ihgpwlah" # example 1
# passcode = "kglvqrro" # example 2
# passcode = "ulqzkmiv" # example 3

from hashlib import md5

# shortestPath = '*'*99999
longestPath = ''

def path(prev, x, y):
    # global shortestPath
    global longestPath

    hashin = passcode + prev[1:]
    hashout = md5(hashin.encode("ascii")).hexdigest()[:4]
    u, d, l, r = map(lambda i: i in 'bcdef', hashout)
    doors = (u, d, l, r)
    u = u and y < 3
    d = d and y > 0
    l = l and x > 0
    r = r and x < 3

    print((x, y), hashout, doors, (u, d, l, r), hashin, prev)

    if x == 3 and y == 0:
        print("FOUND A PATH: ", len(prev), prev)
        # if len(prev) < len(shortestPath):
        #     shortestPath = prev
        if len(prev) > len(longestPath):
            longestPath = prev[1:]
        return True

    # if len(prev) > len(longestPath):
    #     print("There is a shorter path already. Aborting here.")
    #     return False
    #

    if not any((u, d, l, r)):
        print("Stuck")
        return False

    if u: path(prev + 'U', x, y + 1)
    if d: path(prev + 'D', x, y - 1)
    if l: path(prev + 'L', x - 1, y)
    if r: path(prev + 'R', x + 1, y)

path(' ', 0, 3)

print("Solutions", len(longestPath), longestPath)

