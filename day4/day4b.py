f = open("input")
grid = [list(l.strip()) for l in f.readlines()]

def is_x_mas(x, y, grid):
    if grid[x][y] == 'A':
        diag1 = grid[x-1][y-1] + 'A' + grid[x+1][y+1]
        diag2 = grid[x-1][y+1] + 'A' + grid[x+1][y-1]
        return diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}
    return False

num_valid = sum(
    is_x_mas(x, y, grid)
    for x in range(1, len(grid) - 1)
    for y in range(1, len(grid[0]) - 1)
)

print(num_valid)