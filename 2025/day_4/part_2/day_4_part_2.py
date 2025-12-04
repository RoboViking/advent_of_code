grid = []
goodRolls = 0

def adjacentCellCheck(x, y):
    global grid
    adjacentRolls = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for ix, iy in directions:
        jx = x + ix
        jy = y + iy
        if 0 <= jx < len(grid) and 0 <= jy < len(grid[0]):
            if grid[jx][jy] == '@':
                adjacentRolls += 1
    
    return adjacentRolls
    
def main():
    global grid, goodRolls
    with open("day_4/input.txt", "r") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
            print(line)
    
    row = len(grid)
    col = len(grid[0])
    removedRolls = 0
    Running = True
    while Running:
        goodRollsList = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '@':
                    adjacentRolls = adjacentCellCheck(i, j)
                    if adjacentRolls < 4:
                        goodRollsList.append((i,j))
            
        if len(goodRollsList) == 0:
            Running = False
        else:
            for cell in goodRollsList:
                grid[cell[0]][cell[1]] = '.'
                removedRolls += 1
    
    print("Removed rolls:", removedRolls)
    

if __name__ == "__main__":
    main()