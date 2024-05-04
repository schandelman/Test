grid = []
for i in range(4):
    row = []
    for j in range(4):
        row.append("")
    grid.append(row)

def valid_square(grid, i, j):
    if grid[i][j] == "K":
        return False
    if i > 0 and j > 0 and grid[i-1][j-1] == "K":
        return False
    if i > 0 and grid[i-1][j] == "K":
        return False
    if i > 0 and j < len(grid[i])-1 and grid[i-1][j+1] == "K":
        return False
    if j > 0 and grid[i][j-1] == "K":
        return False
    if j < len(grid[i])-1 and grid[i][j+1] == "K":
        return False
    if i < len(grid)-1 and j > 0 and grid[i+1][j-1] == "K":
        return False
    if i < len(grid)-1 and grid[i+1][j] == "K":
        return False
    if i < len(grid)-1 and j < len(grid[row])-1 and grid[i+1][j+1] == "K":
        return False
    return True

