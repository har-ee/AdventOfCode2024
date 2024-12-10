f = open("input")
grid = [[int(i) for i in list(l.strip())] for l in f.readlines()]

def get_neighbours(x, y, grid):
    neighbours = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x1, y1 = x+dx, y+dy
        if  0 <= x1 and x1 < len(grid) and 0 <= y1 and y1 < len(grid[0]):
            neighbours.append((x1, y1))
    return neighbours


def bfs(start_x, start_y, grid):
    to_visit = [(start_x, start_y)]
    ends = []

    while len(to_visit) > 0:
        x, y = to_visit.pop()
        height = grid[x][y]
        if height == 9:
            ends.append((x, y))
        else:
            neighbours = get_neighbours(x, y, grid)
            to_visit.extend([(nx, ny) for nx, ny in neighbours if grid[nx][ny] - height == 1])

    return ends

starts = [(x, y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == 0]

total = sum([len(set(bfs(x, y, grid))) for x, y in starts])

print(total)
