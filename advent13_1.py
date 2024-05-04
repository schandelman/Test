def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()
    print()

def find_horizontal_symmetry(grid):
    #print_grid(grid)
    for i, row in enumerate(grid):
        grid[i] = list(row)
    for rownum, row in enumerate(grid[:-1]):
        i = rownum
        j = i + 1
        differences = []
        while i >= 0 and j < len(grid):
            for k in range(len(grid[0])):
                if grid[i][k] != grid[j][k]:
                    differences.append([i,j,k])
            i -= 1
            j += 1
        if len(differences) == 1:
            a,b,c = differences[0]
            print(a,b,c)
            print(type(grid))
            grid[a][c], grid[b][c] = grid[b][c], grid[a][c]
            return rownum+1
    return -1

def find_vertical_symmetry(grid):
    return find_horizontal_symmetry(list(zip(*grid)))

def count_differences(row1, row2):
    return sum(1 for x,y in zip(row1, row2) if x != y)

grid = []
total = 0
with open("input13.txt") as f:
    for line in f:
        if line.strip() != "":
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
        else:
            column = find_vertical_symmetry(grid)
            if column > -1:
                total += column
            else:
                row = find_horizontal_symmetry(grid)
                if row > -1:
                    total += (100*row)
            grid = []
column = find_vertical_symmetry(grid)
if column > -1:
    total += column
else:
    row = find_horizontal_symmetry(grid)
    if row > -1:
        total += (100*row)

print(total)

