import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    grid = [list(map(int, line.strip())) for line in lines]

    total = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                nines = set()
                getScore(grid, i, j, 0, nines)
                total.append(len(nines))
    print(total)
    print(sum(total))
    pass


def getScore(grid, i, j, level, nines:set):
    if level == 9:
        nines.add((i, j))
    else:
        if i+1 < len(grid) and grid[i+1][j] == level + 1:
            getScore(grid, i+1, j, level+1, nines)
        
        if i-1 >= 0 and grid[i-1][j] == level + 1:
            getScore(grid, i-1, j, level+1, nines)

        if j+1 < len(grid[0]) and grid[i][j+1] == level + 1:
            getScore(grid, i, j+1, level+1, nines)

        if j-1 >= 0 and grid[i][j-1] == level + 1:
            getScore(grid, i, j-1, level+1, nines)


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    grid = [list(map(int, line.strip())) for line in lines]

    total = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                total.append(getScore2(grid, i, j, 0))
    print(total)
    print(sum(total))
    pass


def getScore2(grid, i, j, level):
    if level == 9:
        return 1
    else:
        total = 0
        if i+1 < len(grid) and grid[i+1][j] == level + 1:
            total += getScore2(grid, i+1, j, level+1)
        
        if i-1 >= 0 and grid[i-1][j] == level + 1:
            total += getScore2(grid, i-1, j, level+1)

        if j+1 < len(grid[0]) and grid[i][j+1] == level + 1:
            total += getScore2(grid, i, j+1, level+1)

        if j-1 >= 0 and grid[i][j-1] == level + 1:
            total += getScore2(grid, i, j-1, level+1)
        return total


if __name__ == "__main__":
    part1()
    part2()