import copy

directions = {"east":{".":"east", "/":"north", "\\":"south","-":"east","|":"split"},
              "west":{".":"west", "/":"south", "\\":"north","-":"west","|":"split"},
              "north":{".":"north", "/":"east","\\":"west","-":"split","|":"north"},
              "south":{".":"south","/":"west","\\":"east","-":"split","|":"south"}}

grid = []
with open("input16.txt") as f:
    for line in f:
        row = []
        for c in line.strip():
            row.append(c)
        grid.append(row)

def print_grid(grid):
    for row in grid:
        for cell in row:
            if len(cell) != 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def make_energy_grid():
    energy_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            new_row.append([])
        energy_grid.append(new_row)
    return energy_grid

instruction_list = [["east",0,0]]

def move_beam(direction, x, y):
    #print_grid(energy_grid)
    #print(direction, x, y)
    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and direction not in energy_grid[x][y]:
        next_direction=directions[direction][grid[x][y]]
        energy_grid[x][y].append(direction)
        if next_direction == "east":
            instruction_list.append([next_direction, x, y+1])
        elif next_direction == "west":
            instruction_list.append([next_direction, x, y-1])
        elif next_direction == "north":
            instruction_list.append([next_direction, x-1, y])
        elif next_direction == "south":
            instruction_list.append([next_direction, x+1, y])
        elif next_direction == "split" and (direction == "east" or direction == "west"):
            instruction_list.append(["north", x-1, y])
            instruction_list.append(["south", x+1, y])
        elif next_direction == "split" and (direction == "north" or direction == "south"):
            instruction_list.append(["east", x, y+1])
            instruction_list.append(["west", x, y-1])


starts = []
for i, row in enumerate(grid):
    starts.append(["east",i,0])
    starts.append(["west",i,len(grid)-1])
    starts.append(["south",0,i])
    starts.append(["north",len(grid)-1,i])

totals = []
for start in starts:
    energy_grid = make_energy_grid()
    instruction_list = [start]
    while len(instruction_list) > 0:
        move_beam(*instruction_list.pop(0))
    total = 0
    for row in energy_grid:
        for cell in row:
            if len(cell) != 0:
                total += 1
    totals.append(total)

print(max(totals))