def get_numbers(grid, row, col):
    numbers = []
    if col > 0:
        if grid[row][col-1].isdigit():
            start = find_number_start(grid, row, col-1)
            number = parse_number(grid, row, start)
            numbers.append(number)
    if col < len(grid[0])-1:
        if grid[row][col+1].isdigit():
            number = parse_number(grid, row, col+1)
            numbers.append(number)
    if row > 0:
        if grid[row-1][col].isdigit():
            start = find_number_start(grid, row-1, col)
            number = parse_number(grid, row-1, start)
            numbers.append(number)
        else:
            if col > 0 and grid[row-1][col-1].isdigit():
                start = find_number_start(grid, row-1, col-1)
                number = parse_number(grid, row-1, start)
                numbers.append(number)
            if col < len(grid[0])-1 and grid[row-1][col+1].isdigit():
                number = parse_number(grid, row-1, col+1)
                numbers.append(number)
    if row < len(grid) - 1:
        if grid[row+1][col].isdigit():
            start = find_number_start(grid, row+1, col)
            number = parse_number(grid, row+1, start)
            numbers.append(number)
        else:
            if col > 0 and grid[row+1][col-1].isdigit():
                start = find_number_start(grid, row+1, col-1)
                number = parse_number(grid, row+1, start)
                numbers.append(number)
            if col < len(grid[0])-1 and grid[row+1][col+1].isdigit():
                number = parse_number(grid, row+1, col+1)
                numbers.append(number)
    return numbers

def find_number_start(grid, row, col):
    while col >= 0 and grid[row][col].isdigit():
        col -= 1
    return col+1

def parse_number(grid, row, col):
    number = ""
    print(f"Finding number at ({row}, {col})")
    while col <= len(grid[row])-1 and grid[row][col].isdigit():
        number += grid[row][col]
        col += 1
    print(f"Found: {number}")
    return int(number)

grid = []
with open("input3.txt") as f:
    for line in f:
        grid.append(line.strip())

total = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "*":
            numbers = get_numbers(grid, i, j)
            if len(numbers) == 2:
                total += (numbers[0]*numbers[1])

print(total)