import sys
from collections import deque


def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Parse information
    grid = [list(line.strip()) for line in lines]
    height = len(grid)
    width = len(grid[0])
    
    # Find S and E tile positions
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "S":
                S = (i, j)
            if grid[i][j] == "E":
                E = (i, j)

    # Establish direction steps
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]

    # Call bfs to get fastest time to every cell w.r.t start
    def bfs(start):
        # Have dictionary of distances for each possible index (i, j)
        distances = dict()
        distances[start] = 0

        # Create queue of (distance, (i, j))
        queue = deque()
        queue.append((0, start))

        # Begin loop until queue is empty
        while len(queue) > 0:
            # Pop latest element
            dist, (i, j) = queue.popleft()

            # Iterate over every edge and relax
            for d in directions:
                next_pos = (i + d[0], j + d[1])
                if grid[next_pos[0]][next_pos[1]] in ['.', 'S', 'E']:
                    if next_pos not in distances:
                        distances[next_pos] = dist + 1
                        queue.append((distances[next_pos], next_pos))

        # Return the distances dictionary
        return distances
    
    def inBounds(i, j):
        return 0 <= i < height and 0 <= j < width

    # Get the fastest times from start and end 
    start_to_node = bfs(S)
    node_to_end = bfs(E)

    # Establish best possible time with no cheats
    best_time_no_cheats = start_to_node[E]

    # Go over every cell and apply cheat if possible
    cheats = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "#":
                # Iterate over every possible pair of directions to apply cheat
                for u in directions:
                    # Establish entry position of the cheat
                    entry = (i + u[0], j + u[1])
                    if (not inBounds(*entry)) or grid[entry[0]][entry[1]] == '#':
                        continue

                    for v in directions:
                        # Establish exit position of the cheat
                        exit = (i + v[0], j + v[1])
                        if (not inBounds(*exit)) or grid[exit[0]][exit[1]] == '#':
                            continue

                        # Get the new time by applying cheat and compare if better
                        cheated_time = start_to_node[entry] + 2 + node_to_end[exit]
                        if cheated_time < best_time_no_cheats:
                            cheats.append((entry, exit, best_time_no_cheats - cheated_time))

    count = 0
    for cheat in cheats:
        if cheat[2] >= 100:
            count += 1

    print(count)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Parse information
    grid = [list(line.strip()) for line in lines]
    height = len(grid)
    width = len(grid[0])
    
    # Find S and E tile positions
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "S":
                S = (i, j)
            if grid[i][j] == "E":
                E = (i, j)

    # Establish direction steps
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]

    # Call bfs to get fastest time to every cell w.r.t start
    def bfs(start):
        # Have dictionary of distances for each possible index (i, j)
        distances = dict()
        distances[start] = 0

        # Create queue of (distance, (i, j))
        queue = deque()
        queue.append((0, start))

        # Begin loop until queue is empty
        while len(queue) > 0:
            # Pop latest element
            dist, (i, j) = queue.popleft()

            # Iterate over every edge and relax
            for d in directions:
                next_pos = (i + d[0], j + d[1])
                if grid[next_pos[0]][next_pos[1]] in ['.', 'S', 'E']:
                    if next_pos not in distances:
                        distances[next_pos] = dist + 1
                        queue.append((distances[next_pos], next_pos))

        # Return the distances dictionary
        return distances
    
    def inBounds(i, j):
        return 0 <= i < height and 0 <= j < width

    # Get the fastest times from start and end 
    start_to_node = bfs(S)
    node_to_end = bfs(E)

    # Establish best possible time with no cheats
    best_time_no_cheats = start_to_node[E]

    def getValidCells(cell):
        # Get any cell that has Manhattan distance <= 20 to start
        valid = []
        for i in range(-20, 21):
            for j in range(-(20 - abs(i)), 20-abs(i) + 1):
                new_pos = (cell[0] + i, cell[1] + j)
                if inBounds(*new_pos) and grid[new_pos[0]][new_pos[1]] in ['.', 'S', 'E']:
                    valid.append(new_pos)
        return valid

    # Go over every cell and apply cheat if possible
    cheats = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] in ['.', 'S', 'E']:
                # Get all valid exit points w.r.t (i, j)
                entry = (i, j)
                valid_cells = getValidCells(entry)

                # Iterate over every possible exit
                for exit in valid_cells:
                    # Get the new time by applying cheat and compare if better
                    cheat_time = abs(entry[0] - exit[0]) + abs(entry[1] - exit[1])
                    cheated_time = start_to_node[entry] + cheat_time + node_to_end[exit]
                    if cheated_time < best_time_no_cheats:
                        cheats.append((entry, exit, best_time_no_cheats - cheated_time))

    # counts = dict()
    # for _, _, time in cheats:
    #     if time in counts:
    #         counts[time] += 1
    #     else:
    #         counts[time] = 1

    # num_cheats_per_time = []
    # for time, freq in counts.items():
    #     num_cheats_per_time.append((time, freq))

    # num_cheats_per_time = list(filter(lambda x: x[0] >= 50, num_cheats_per_time))
    # num_cheats_per_time.sort(key=lambda x: x[0])
    # print(*num_cheats_per_time, sep="\n")

    count = 0
    for cheat in cheats:
        if cheat[2] >= 100:
            count += 1

    print(count)
    pass



if __name__ == "__main__":
    # part1()
    part2()