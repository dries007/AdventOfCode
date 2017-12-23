row = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
#
# row = '..^^.'
# row = '.^^.^.^^^^'

def nextRow(row):
    new = ''
    for i in range(len(row)):
        tmp = ''
        tmp += row[i-1] if i > 0 else '.'
        tmp += row[i]
        tmp += row[i+1] if i < len(row)-1 else '.'
        t = '^' if tmp == '^^.' or tmp == '.^^' or tmp == '^..' or tmp == '..^' else '.'
        new += t
    return new

safe = 0
for i in range(400000):
    safe += row.count('.')
    print(i, row, row.count('.'), safe)
    row = nextRow(row)

