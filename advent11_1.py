import copy

def expand_rows(grid):
    new_grid = []
    for row in grid:
        if all(x == "." for x in row):
            new_grid.append(row)
        new_grid.append(row)
    return new_grid

def expand_cols(grid):
    transposed = zip(*grid)
    transposed = expand_rows(transposed)
    return zip(*transposed)

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2-x1) + abs(y2-y1)

grid = []
with open("input11.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

grid = expand_rows(grid)
grid = expand_cols(grid)

galaxies = []

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "#":
            galaxies.append((i, j))

total = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i:]:
        total += manhattan_distance(galaxy1, galaxy2)

print(total)




