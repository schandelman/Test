def travel_maze(grid, i, j, direction):
    if grid[i][j] == "|":
        if direction == "north":
            return i-1, j, "north"
        else:
            return i+1, j, "south"
    elif grid[i][j] == "-":
        if direction == "east":
            return i, j+1, "east"
        else:
            return i, j-1, "west"
    elif grid[i][j] == "L":
        if direction == "south":
            return i, j+1, "east"
        else:
            return i-1, j, "north"
    elif grid[i][j] == "J":
        if direction == "south":
            return i, j-1, "west"
        else:
            return i-1, j, "north"
    elif grid[i][j] == "7":
        if direction == "east":
            return i+1, j, "south"
        else:
            return i, j-1, "west"
    elif grid[i][j] == "F":
        if direction == "north":
            return i, j+1, "east"
        else:
            return i+1, j, "south"
    else:
        return i,j, direction

grid = []

with open("input10.txt") as f:
    for line in f:
        grid.append(line.strip())


for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "S":
            current_row = i
            current_col = j


current_direction = "north"
current_row -= 1
counter = 1
#print(f"START: ({current_row, current_col})")
while grid[current_row][current_col] != "S":
    current_row, current_col, current_direction = travel_maze(grid, current_row, current_col, current_direction)
    #print(f"({current_row}, {current_col})")
    counter += 1

print(counter/2)