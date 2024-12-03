f = open("input")

raw = f.readlines()

parsed = [[int(n) for n in line.strip().split(' ')] for line in raw]

# Calculate & number of violations
def check(line):
    vios = 0
    skipped = False
    for i in range(len(line) - 1):
        cur = line[i]
        nex = line[i+1]

        if(skipped):
            cur = line[i-1]
            skipped = False

        if i == 0:
            incrementing = cur < nex

        diff = cur - nex
        if diff == 0:
            skipped = True
            vios += 1
        elif abs(diff) > 3:
            skipped = True
            vios += 1
        elif incrementing != (cur < nex):
            skipped = True
            vios += 1
        if vios > 1:
            return False
    return True

# Checking reversed list as well handles case of misidentifing as incrementing from first 2 elems
valid = [l for l in parsed if check(l) or check(list(reversed(l)))]

num_valid = len(valid)

print(num_valid)
