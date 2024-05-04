import copy

def manhattan_distance(point1, point2, big_rows, big_cols, expansion):
    x1, y1 = point1
    x2, y2 = point2
    distance = abs(x2-x1) + abs(y2-y1)
    for big_row in big_rows:
        if x1 <= big_row <= x2 or x2 <= big_row <= x1:
            distance += (expansion - 1)
    for big_col in big_cols:
        if y1 <= big_col <= y2 or y2 <= big_col <= y1:
            distance += (expansion - 1)
    return distance

grid = []
with open("input11.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

expanded_rows = []
for i, row in enumerate(grid):
    if all(x=="." for x in row):
        expanded_rows.append(i)

expanded_cols = []
transposed = zip(*grid)
for i, row in enumerate(transposed):
    if all(x=="." for x in row):
        expanded_cols.append(i)

print(expanded_rows, expanded_cols)

galaxies = []

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "#":
            galaxies.append((i, j))

total = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i:]:
        total += manhattan_distance(galaxy1, galaxy2, expanded_rows, expanded_cols, 1000000)

print(total)