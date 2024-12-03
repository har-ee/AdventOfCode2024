f = open("input")

raw = f.readlines()

def parse_lists(input_str):
    left_right = [line.strip().split('   ') for line in input_str]

    left = [int(l) for [l,_] in left_right]
    right = [int(r) for [_,r] in left_right]

    return left, right

left, right = parse_lists(raw)

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i]-right[i])

print(dist)
