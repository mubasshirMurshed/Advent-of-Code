import sys
import heapq

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Parse information
    grid = [list(line.strip()) for line in lines]
    height = len(grid)
    width = len(grid[0])
    
    # Establish S tile position
    S = (height - 2, 1, '>')

    # Establish directions and a map for the steps to search for each
    directions = ['>', '<', 'v', '^']
    forward_map = {
        '>': [0, 1],
        '<': [0, -1],
        'v': [1, 0],
        '^': [-1, 0]
    }
    left_rotate = {
        '>': '^',
        '<': 'v',
        'v': '>',
        '^': '<'
    }
    right_rotate = {
        '>': 'v',
        '<': '^',
        'v': '<',
        '^': '>'
    }

    # Call dijkstra to get shortest scores to every cell
    def dijkstra():
        # Have dictionary of distances for each possible index (i, j, dir)
        distances = dict()
        for i in range(height):
            for j in range(width):
                if grid[i][j] in ['.', 'S', 'E']:
                    for d in directions:
                        distances[(i, j, d)] = float("inf")

        # Set distance of start to 0
        distances[S] = 0

        # Create priority queue of (distance, (i, j, dir))
        queue = []
        heapq.heappush(queue, (0, S))

        # Begin loop until queue is empty
        while len(queue) > 0:
            # Pop latest element
            dist, (i, j, d) = heapq.heappop(queue)

            # Skip out of date entries
            if dist > distances[(i, j, d)]:
                continue

            # Relax forward movement
            next_pos = (i + forward_map[d][0], j + forward_map[d][1], d)
            if grid[next_pos[0]][next_pos[1]] in ['.', 'S', 'E']:
                if distances[next_pos] > dist + 1:
                    distances[next_pos] = dist + 1
                    heapq.heappush(queue, (distances[next_pos], next_pos))

            # Relax left rotation
            next_pos = (i, j, left_rotate[d])
            if distances[next_pos] > dist + 1000:
                distances[next_pos] = dist + 1000
                heapq.heappush(queue, (distances[next_pos], next_pos))

            # Relax right rotation
            next_pos = (i, j, right_rotate[d])
            if distances[next_pos] > dist + 1000:
                distances[next_pos] = dist + 1000
                heapq.heappush(queue, (distances[next_pos], next_pos))

        # Return the distances dictionary
        return distances

    scores = dijkstra()

    # Return the smallest score to reach E
    print(min([scores[(1, width-2, d)] for d in directions]))
    pass



def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Parse information
    grid = [list(line.strip()) for line in lines]
    height = len(grid)
    width = len(grid[0])
    
    # Establish S tile position
    S = (height - 2, 1, '>')

    # Establish directions and a map for the steps to search for each
    directions = ['>', '<', 'v', '^']
    forward_map = {
        '>': [0, 1],
        '<': [0, -1],
        'v': [1, 0],
        '^': [-1, 0]
    }
    left_rotate = {
        '>': '^',
        '<': 'v',
        'v': '>',
        '^': '<'
    }
    right_rotate = {
        '>': 'v',
        '<': '^',
        'v': '<',
        '^': '>'
    }

    # Call dijkstra to get shortest scores to every cell
    def dijkstra():
        # Have dictionary of distances for each possible index (i, j, dir)
        distances = dict()
        pred = dict()
        for i in range(height):
            for j in range(width):
                if grid[i][j] in ['.', 'S', 'E']:
                    for d in directions:
                        distances[(i, j, d)] = float("inf")
                        pred[(i, j, d)] = []

        # Set distance of start to 0
        distances[S] = 0

        # Create priority queue of (distance, (i, j, dir))
        queue = []
        heapq.heappush(queue, (0, S))

        # Begin loop until queue is empty
        while len(queue) > 0:
            # Pop latest element
            dist, (i, j, d) = heapq.heappop(queue)

            # Skip out of date entries
            if dist > distances[(i, j, d)]:
                continue

            # Relax forward movement
            next_pos = (i + forward_map[d][0], j + forward_map[d][1], d)
            if grid[next_pos[0]][next_pos[1]] in ['.', 'S', 'E']:
                if distances[next_pos] > dist + 1:
                    distances[next_pos] = dist + 1
                    pred[next_pos] = [(i, j, d)]
                    heapq.heappush(queue, (distances[next_pos], next_pos))
                elif distances[next_pos] == dist + 1:
                    pred[next_pos].append((i, j, d))

            # Relax left rotation
            next_pos = (i, j, left_rotate[d])
            if distances[next_pos] > dist + 1000:
                distances[next_pos] = dist + 1000
                pred[next_pos] = [(i, j, d)]
                heapq.heappush(queue, (distances[next_pos], next_pos))
            elif distances[next_pos] == dist + 1000:
                pred[next_pos].append((i, j, d))

            # Relax right rotation
            next_pos = (i, j, right_rotate[d])
            if distances[next_pos] > dist + 1000:
                distances[next_pos] = dist + 1000
                pred[next_pos] = [(i, j, d)]
                heapq.heappush(queue, (distances[next_pos], next_pos))
            elif distances[next_pos] == dist + 1000:
                pred[next_pos].append((i, j, d))

        # Return the distances dictionary
        return distances, pred

    # Get best score
    scores, pred = dijkstra()
    best_score = min([scores[(1, width-2, d)] for d in directions])

    # Go over the predecessor array to mark cells belonging to any possible best path
    def mark_tiles():
        tiles = set()

        def process_tile(i, j, d):
            tiles.add((i, j))
            if (i, j, d) == S:
                return
            if (i, j, d) not in pred:
                return
            for node in pred[(i, j, d)]:
                process_tile(*node)
        
        # Consider backtracking from all the possible ways to reach E at a best score
        for d in directions:
            if scores[(1, width-2, d)] == best_score:
                process_tile(1, width-2, d)
        return tiles

    tiles = mark_tiles()
    print(len(tiles))
    pass


if __name__ == "__main__":
    part1()
    part2()