grid = []

def get_neighbors(grid, row, start, end):
    neighbors = []
    if start == 0:
        s = 0
    else:
        s = start-1
    if end == len(grid[0])-1:
        e = end
    else:
        e = end + 1
    if row != 0:
        for i in range(s, e+1):
            neighbors.append(grid[row-1][i])
    if start != 0:
        neighbors.append(grid[row][s])
    if end != len(grid[0])-1:
        neighbors.append(grid[row][e])
    if row != len(grid)-1:
        for i in range(s, e+1):
            neighbors.append(grid[row+1][i])
    return neighbors

def is_label(grid, row, start, end):
    return not all((x== "." or x.isdigit()) for x in get_neighbors(grid, row, start, end))


with open("input3.txt") as f:
    for line in f:
        grid.append(line.strip())

total = 0
for i, row in enumerate(grid):
    number = ""
    for j, cell in enumerate(row):
        if cell.isdigit():
            number += cell
        elif len(number) > 0:
            end = j - 1
            start = end + 1 - len(number)
            print(f"Checking row {i} from {start} to {end}")
            if is_label(grid, i, start, end):
                print(f"{number} is valid!")
                total += int(number)
            else:
                print(f"{number} is NOT VALID")
            number = ""
    if len(number) > 0:
        end = j
        start = end + 1 - len(number)
        if is_label(grid, i, start, end):
            print(f"{number} is valid!")
            total += int(number)
            number = ""
        else:
            print(f"{number} is NOT VALID")
print(total)