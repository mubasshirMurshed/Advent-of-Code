import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        info = f.read()

    # Parse file contents 
    grid, movements = info.split("\n\n")
    movements = movements.strip().split('\n')
    movements = "".join(movements)
    grid = grid.split("\n")
    grid = [list(line) for line in grid]
    height = len(grid)
    width = len(grid[0])
    step = {
        '^': [-1, 0],
        '>': [0, 1],
        'v': [1, 0],
        '<': [0, -1],
    }

    # Find robot '@' position
    def get_robot_pos():
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '@':
                    return [i, j]            
    robot_pos = get_robot_pos()

    # Run simulation of robot
    def simulate_move(move):
        # Determine if there is a '.' in given direction before a '#'
        dir = step[move]
        space_exists = True
        i = 1
        while space_exists:
            pos = [robot_pos[0] + i*dir[0], robot_pos[1] + i*dir[1]]
            if grid[pos[0]][pos[1]] == '.':
                break
            elif grid[pos[0]][pos[1]] == '#':
                space_exists = False
            i += 1
        
        if space_exists:
            # Vacate the robot
            grid[robot_pos[0]][robot_pos[1]] = '.'

            # Move objects until '.' is filled
            temp1 = '@'
            for j in range(1, i + 1):
                pos = [robot_pos[0] + j*dir[0], robot_pos[1] + j*dir[1]]
                temp2 = grid[pos[0]][pos[1]]
                grid[pos[0]][pos[1]] = temp1
                temp1 = temp2
            
            # Update robot position
            robot_pos[0] = robot_pos[0] + dir[0]
            robot_pos[1] = robot_pos[1] + dir[1]

    for move in movements:
        simulate_move(move)

    # print(*grid, sep='\n')

    # Get final GPS aggregate
    total = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'O':
                total += 100*i + j

    print(total)
    pass
                    

def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        info = f.read()

    # Parse file contents 
    pregrid, movements = info.split("\n\n")
    movements = movements.strip().split('\n')
    movements = "".join(movements)
    pregrid = pregrid.split("\n")
    pregrid = [list(line) for line in pregrid]
    height = len(pregrid)
    width = len(pregrid[0])
    step = {
        '^': [-1, 0],
        '>': [0, 1],
        'v': [1, 0],
        '<': [0, -1],
    }

    # Create new grid based on width transformation
    grid = [[0]*width*2 for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if pregrid[i][j] == '#':
                grid[i][2*j] = '#'
                grid[i][2*j + 1] = '#'
            elif pregrid[i][j] == 'O':
                grid[i][2*j] = '['
                grid[i][2*j + 1] = ']'
            elif pregrid[i][j] == '.':
                grid[i][2*j] = '.'
                grid[i][2*j + 1] = '.'
            elif pregrid[i][j] == '@':
                grid[i][2*j] = '@'
                grid[i][2*j + 1] = '.'
    width *= 2

    # Find robot '@' position
    def get_robot_pos():
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '@':
                    return [i, j]            
    robot_pos = get_robot_pos()

    # Run simulation of robot
    def simulate_move(move):
        dir = step[move]
        if move in ['<', '>']:
            # Determine if there is a '.' in given direction before a '#'
            space_exists = True
            i = 1
            while space_exists:
                pos = [robot_pos[0] + i*dir[0], robot_pos[1] + i*dir[1]]
                if grid[pos[0]][pos[1]] == '.':
                    break
                elif grid[pos[0]][pos[1]] == '#':
                    space_exists = False
                i += 1
            
            if space_exists:
                # Vacate the robot
                grid[robot_pos[0]][robot_pos[1]] = '.'

                # Move objects until '.' is filled
                temp1 = '@'
                for j in range(1, i + 1):
                    pos = [robot_pos[0] + j*dir[0], robot_pos[1] + j*dir[1]]
                    temp2 = grid[pos[0]][pos[1]]
                    grid[pos[0]][pos[1]] = temp1
                    temp1 = temp2
                
                # Update robot position
                robot_pos[0] += dir[0]
                robot_pos[1] += dir[1]
        else:
            # Determine if vertical movement is possible
            next_pos = [robot_pos[0] + dir[0], robot_pos[1] + dir[1]]
            if grid[next_pos[0]][next_pos[1]] == '.':
                grid[robot_pos[0]][robot_pos[1]] = '.'
                grid[next_pos[0]][next_pos[1]] = '@'
                robot_pos[0] += dir[0]
                robot_pos[1] += dir[1]
            elif grid[next_pos[0]][next_pos[1]] == '[':
                if canBoxMoveVertical(next_pos[0], next_pos[1], move):
                    moveBoxVertical(next_pos[0], next_pos[1], move)
                    grid[robot_pos[0]][robot_pos[1]] = '.'
                    grid[next_pos[0]][next_pos[1]] = '@'
                    robot_pos[0] += dir[0]
                    robot_pos[1] += dir[1]
            elif grid[next_pos[0]][next_pos[1]] == ']':
                if canBoxMoveVertical(next_pos[0], next_pos[1]-1, move):
                    moveBoxVertical(next_pos[0], next_pos[1]-1, move)
                    grid[robot_pos[0]][robot_pos[1]] = '.'
                    grid[next_pos[0]][next_pos[1]] = '@'
                    robot_pos[0] += dir[0]
                    robot_pos[1] += dir[1]


    def canBoxMoveVertical(i, j, move):
        # i, j refers to '[' of box
        i_ = i + 1 if move == 'v' else i - 1

        if grid[i_][j] == '#' or grid[i_][j+1] == '#':
            return False
        
        if grid[i_][j] == '.' and grid[i_][j+1] == '.':
            return True

        if grid[i_][j] == '[' and grid[i_][j+1] == ']':
            return canBoxMoveVertical(i_, j, move)
        
        if grid[i_][j] == ']' and grid[i_][j+1] == '.':
            return canBoxMoveVertical(i_, j-1, move)
        
        if grid[i_][j] == '.' and grid[i_][j+1] == '[':
            return canBoxMoveVertical(i_, j+1, move)
        
        if grid[i_][j] == ']' and grid[i_][j+1] == '[':
            return canBoxMoveVertical(i_, j-1, move) and canBoxMoveVertical(i_, j+1, move)
        
    
    def moveBoxVertical(i, j, move):
        # i, j refers to '[' of box
        i_ = i + 1 if move == 'v' else i - 1

        if grid[i_][j] == '#' or grid[i_][j+1] == '#':
            return
        
        elif grid[i_][j] == '.' and grid[i_][j+1] == '.':
            grid[i_][j] = '['
            grid[i_][j+1] = ']'

        elif grid[i_][j] == '[' and grid[i_][j+1] == ']':
            moveBoxVertical(i_, j, move)
            grid[i_][j] = '['
            grid[i_][j+1] = ']'
        
        elif grid[i_][j] == ']' and grid[i_][j+1] == '.':
            moveBoxVertical(i_, j-1, move)
            grid[i_][j] = '['
            grid[i_][j+1] = ']'
        
        elif grid[i_][j] == '.' and grid[i_][j+1] == '[':
            moveBoxVertical(i_, j+1, move)
            grid[i_][j] = '['
            grid[i_][j+1] = ']'
        
        elif grid[i_][j] == ']' and grid[i_][j+1] == '[':
            moveBoxVertical(i_, j-1, move)
            moveBoxVertical(i_, j+1, move)
            grid[i_][j] = '['
            grid[i_][j+1] = ']'

        grid[i][j] = '.'
        grid[i][j+1] = '.'

        return


    for move in movements:
        simulate_move(move)
        # print(*grid, sep='\n')
        # print()

    # Get final GPS aggregate
    total = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '[':
                total += 100*i + j

    print(total)
    pass


if __name__ == "__main__":
    part1()
    part2()