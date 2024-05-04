grid =  []

with open("input17.txt") as f:
    for line in f:
        row = [int(x) for x in line.strip()]
        grid.append(row)

total_grid = []
for r in grid:
    row = []
    for c in r:
        row.append(100000)
    total_grid.append(row)

instruction_list = [["east",0,1,1,0], ["south",1,0,1,0]]

def update_cell(direction, x, y, steps, total):
    total = total + grid[x][y]
    #print(x,y,total_grid[x][y])
    if total < total_grid[x][y]:
        total_grid[x][y] = total
        if direction == "east":
            if x > 0:
                instruction_list.append(["north", x-1, y, 0, total])
            if x < len(grid)-1:
                instruction_list.append(["south", x+1, y, 0, total])
            if steps < 3 and y < len(grid[0])-1:
                instruction_list.append(["east", x, y+1, steps + 1, total])
        elif direction == "west":
            if x > 0:
                instruction_list.append(["north", x-1, y, 0, total])
            if x < len(grid)-1:
                instruction_list.append(["south", x+1, y, 0, total])
            if steps < 3 and y > 0:
                instruction_list.append(["west", x, y-1, steps+1, total])
        elif direction == "north":
            if y > 0:
                instruction_list.append(["west", x, y-1, 0, total])
            if y < len(grid[0])-1:
                instruction_list.append(["east", x, y+1, 0, total])
            if steps < 3 and x > 0:
                instruction_list.append(["north", x-1, y, steps+1, total])
        elif direction == "south":
            if y > 0:
                instruction_list.append(["west", x, y-1, 0, total])
            if y < len(grid[0])-1:
                instruction_list.append(["east", x, y+1, 0, total])
            if steps < 3 and x < len(grid)-1:
                instruction_list.append(["south", x+1, y, steps + 1, total])

while instruction_list != []:
    instruction = instruction_list.pop(0)
    update_cell(*instruction)

print(total_grid[-1][-1])
print()
for row in total_grid:
    for cell in row:
        print(cell, end="\t")
    print()
