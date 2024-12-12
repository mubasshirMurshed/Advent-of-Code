import sys
from collections import deque

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    grid = [list(line.strip()) for line in lines]

    width = len(grid[0])
    height = len(grid)
    processed = set()

    def process(i, j):
        # Do a BFS at position grid[i, j] to count area and perimeter
        queue = deque()
        queue.append((i, j))
        visited = set()
        visited.add((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        area = 0
        perimeter = 0

        while len(queue) > 0:
            # Get garden cell to analyse
            u = queue.popleft()
            
            # Update area
            area += 1
            processed.add(u)

            # Add all viable neighbour garden cells to bfs search queue
            for dir in directions:
                v = (u[0] + dir[0], u[1] + dir[1])
                if v not in visited:
                    if 0 <= v[0] < height and 0 <= v[1] < width:
                        if grid[v[0]][v[1]] == grid[i][j]:
                            visited.add(v)
                            queue.append(v)
                        else:
                            perimeter += 1
                    else:
                        perimeter += 1
        
        return area*perimeter


    total = 0
    for i in range(height):
        for j in range(width):
            if (i, j) not in processed:
                comp = process(i, j)
                total += comp

    print(total)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    grid = [list(line.strip()) for line in lines]

    width = len(grid[0])
    height = len(grid)
    processed = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def process(i, j):
        # Do a BFS at position grid[i, j] to count area and perimeter
        queue = deque()
        queue.append((i, j))
        visited = set()
        visited.add((i, j))
        region = set()

        area = 0
        sides = 0

        while len(queue) > 0:
            # Get garden cell to analyse
            u = queue.popleft()
            
            # Update area
            area += 1
            processed.add(u)
            region.add(u)

            # Add all viable neighbour garden cells to bfs search queue
            for dir in directions:
                v = (u[0] + dir[0], u[1] + dir[1])
                if v not in visited:
                    if 0 <= v[0] < height and 0 <= v[1] < width and grid[v[0]][v[1]] == grid[i][j]:
                        visited.add(v)
                        queue.append(v)
                            
        # Count number of sides
        for dir in directions:
            sides += count_sides(region, dir)

        return area*sides


    def count_sides(garden_idxs, dir):
        # Create a graph based on only the indices that have a change in symbol based on dir
        idxs = set()
        for i, j in garden_idxs:
            v = (i + dir[0], j + dir[1])
            if not(0 <= v[0] < height) or not(0 <= v[1] < width) or grid[i][j] != grid[v[0]][v[1]]:
                # Cell (i, j) must have difference in dir direction
                idxs.add((i, j))

        # Count the number of connected components
        return connected_components(idxs)
    

    def connected_components(nodes):
        # Given the nodes with position (i, j) find the number of connected components. Assume 4-connectivity.
        def dfs(u, id):
            component[u] = id
            for d in directions:
                v = (u[0] + d[0], u[1] + d[1])
                if v in nodes:
                    if component[v] is None:
                        dfs(v, id)

        component = {u: None for u in nodes}
        num_components = 0
        for u in nodes:
            if component[u] is None:
                num_components += 1
                dfs(u, num_components)

        return num_components


    total = 0
    for i in range(height):
        for j in range(width):
            if (i, j) not in processed:
                comp = process(i, j)
                total += comp

    print(total)
    pass



if __name__ == "__main__":
    # part1()
    part2()