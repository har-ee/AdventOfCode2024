f = open("input")

raw = f.readlines()

parsed = [[int(n) for n in line.strip().split(' ')] for line in raw]

def check(line):
    for i in range(len(line) - 1):
        cur = line[i]
        nex = line[i+1]
        if i == 0:
            incrementing = cur < nex
        diff = cur - nex
        if diff == 0:
            return False
        if abs(diff) > 3:
            return False
        elif incrementing != (cur < nex):
            return False
    return True

checked = [l for l in parsed if check(l)]

num_valid = len(checked)

print(num_valid)