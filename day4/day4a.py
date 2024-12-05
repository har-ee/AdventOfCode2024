import numpy as np

f = open("input")
grid = [list(l.strip()) for l in f.readlines()]

def get_diagonal(grid):
    diags = list()
    xmax = len(grid)
    ymax = len(grid[0])

    for i in range(xmax):
        d1 = list()
        d2 = list()

        for z in range(i+1):
            d1.append(grid[i-z][z])
            d2.append(grid[xmax-1-(i-z)][ymax - 1 - z])

        diags.append(d1)
        if i != xmax-1:
            diags.append(d2)
    return diags

def find_word(word, line_list):
    line_str = ''.join(line_list)
    return line_str.count(word) + line_str.count(word[::-1])

# Generate all lines of text in the grid
horizontal = grid
vertical = np.transpose(grid).tolist()
diagonal = get_diagonal(vertical)
diagonal += get_diagonal(np.rot90(vertical))

all_lines = diagonal + vertical + horizontal

print(sum(find_word("XMAS", l) for l in all_lines))
