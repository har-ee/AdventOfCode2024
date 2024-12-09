f = open("input")

raw_input = f.read().split("\n")

freq_to_pos = dict()

for x in range(len(raw_input)):
    for y in range((len(raw_input[0]))):
        elem = raw_input[x][y]
        if elem != '.':
            if elem not in freq_to_pos:
                freq_to_pos[elem] = set([(x,y)])
            else:
                freq_to_pos[elem] = freq_to_pos[elem].union(set([(x,y)]))

def get_pairs(l):
    pairs = set()

    for i in range(len(l)):
        for j in l[i+1:len(l)]:
            pairs.add((l[i], j))
    return pairs

def in_range(coords, grid):
    (x, y) = coords
    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False
    return True

def generate_antifreq(x0, y0, x1, y1):
    xdiff = x1 - x0
    ydiff = y1 - y0

    a0 = (x0 - xdiff, y0 - ydiff)
    a1 = (x1 + xdiff, y1 + ydiff)

    antifreqs = set()

    last_antifreq = x0, y0

    while(in_range(last_antifreq, raw_input)):
        antifreqs.add(last_antifreq)
        last_antifreq = last_antifreq[0] - xdiff, last_antifreq[1] - ydiff

    last_antifreq = x1, y1
    while(in_range(last_antifreq, raw_input)):
        antifreqs.add(last_antifreq)
        last_antifreq = last_antifreq[0] + xdiff, last_antifreq[1] + ydiff

    return antifreqs

def generate_antifreqs():
    antifreqs = set()
    for freq in freq_to_pos.keys():
        coords_set = freq_to_pos[freq]
        pairs = get_pairs(list(coords_set))
        for ((x0, y0), (x1, y1) ) in pairs:
            antifreqs = antifreqs.union(generate_antifreq(x0, y0, x1, y1))
    return antifreqs

print(len([coord for coord in generate_antifreqs() if in_range(coord, raw_input)]))