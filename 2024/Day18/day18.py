import sys
from collections import deque


def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    height = int(sys.argv[2])
    width = int(sys.argv[2])
    drops = [list(map(int, line.strip().split(","))) for line in lines]

    # Make grid
    grid = [['.' for _ in range(width)] for _ in range(height)]

    # Add the first 1024 bytes
    for i in range(1024):
        x, y = drops[i]
        grid[y][x] = '#'

    # Find shortest path to end using bfs at (0, 0)
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    start = (0, 0)
    visited = set()
    visited.add(start)
    distances = dict()
    queue = deque()
    queue.append(start)
    distances[start] = 0
    def inBounds(x, y):
        return 0 <= x < width and 0 <= y < height
    while len(queue) > 0:
        u = queue.popleft()
        for d in directions:
            v = (u[0] + d[0], u[1] + d[1])
            if v not in visited and inBounds(*v) and grid[v[1]][v[0]] == '.':
                distances[v] = distances[u] + 1
                visited.add(v)
                queue.append(v)
    
    print(distances[(width-1, height-1)])
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    height = int(sys.argv[2])
    width = int(sys.argv[2])
    drops = [list(map(int, line.strip().split(","))) for line in lines]

    # Make grid
    grid = [['.' for _ in range(width)] for _ in range(height)]

    # Add the first 1024 bytes
    for i in range(1024):
        x, y = drops[i]
        grid[y][x] = '#'

    # Find shortest path to end using bfs at (0, 0)
    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    # Helper function
    def inBounds(x, y):
        return 0 <= x < width and 0 <= y < height

    for i in range(1024, len(drops)):
        x, y = drops[i]
        grid[y][x] = '#'
        start = (0, 0)
        visited = set()
        visited.add(start)
        distances = dict()
        queue = deque()
        queue.append(start)
        distances[start] = 0
        
        while len(queue) > 0:
            u = queue.popleft()
            for d in directions:
                v = (u[0] + d[0], u[1] + d[1])
                if v not in visited and inBounds(*v) and grid[v[1]][v[0]] == '.':
                    distances[v] = distances[u] + 1
                    visited.add(v)
                    queue.append(v)
        
        if (width-1, height-1) not in distances:
            print(x,y)
            break
    pass

if __name__ == "__main__":
    part1()
    part2()