input = "ugkcyxxp"
# input = "abc"

from hashlib import md5

zeros = 5
char = 5
index = 0

password = ['$'] * 8

print(password)

while True:
    hashin = input + ('%d' % index)
    index += 1
    hash = md5(hashin.encode("ascii")).hexdigest()

    if hash[:zeros] == '0' * zeros:
        try:
            i = int(hash[5], base=10)
        except ValueError:
            print(hash, hashin, hash[5], hash[6], "Skipped. Not base 10")
            continue
        if i > 7:
            print(hash, hashin, hash[5], hash[6], "Skipped.", i, "> 7")
            continue

        if password[i] != '$':
            print(hash, hashin, hash[5], hash[6], "Already has pos", i)
            continue

        l = list(password)

        password[i] = hash[6]

        if password.count('$') == 0:
            break


    #
    # if index == 1000:
    #     break

print(password, ''.join(password))
