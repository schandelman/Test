import copy

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
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "S":
            current_row = i
            current_col = j

visited_grid = copy.deepcopy(grid)
current_direction = "north"
visited_grid[current_row][current_col] = "*"
current_row -= 1
#print(f"START: ({current_row, current_col})")
while grid[current_row][current_col] != "S":
    visited_grid[current_row][current_col] = "*"
    current_row, current_col, current_direction = travel_maze(grid, current_row, current_col, current_direction)
    #print(f"({current_row}, {current_col})")
grid[current_row][current_col] = "|"

counter = 0
for i, row in enumerate(grid):
    mode_top = "outside"
    mode_bottom = "outside"
    for j, cell in enumerate(row):
        if mode_top == "outside" and mode_bottom == "outside" and visited_grid[i][j] == "*":
            if cell == "|":
                mode_top = "inside"
                mode_bottom = "inside"
            elif cell == "L":
                mode_top =  "inside"
            elif cell == "F":
                mode_bottom = "inside"
        elif mode_top == "inside" and mode_bottom == "inside" and visited_grid[i][j] == "*":
            if cell == "|":
                mode_top = "outside"
                mode_bottom = "outside"
            elif cell == "L":
                mode_top = "outside"
            elif cell == "F":
                mode_bottom = "outside"
        elif mode_top == "inside" and mode_bottom == "outside" and visited_grid[i][j] == "*":
            if cell == "J":
                mode_top = "outside"
            elif cell == "7":
                mode_bottom = "inside"
        elif mode_top == "outside" and mode_bottom == "inside" and visited_grid[i][j] == "*":
            if cell == "J":
                mode_top = "inside"
            elif cell == "7":
                mode_bottom = "outside"
        if mode_top == "inside" and mode_bottom == "inside" and visited_grid[i][j] != "*":
            grid[i][j] = "I"
            counter += 1
        elif visited_grid[i][j] != "*":
            grid[i][j] = "O"

print(counter)