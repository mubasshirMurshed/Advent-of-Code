import sys
from tqdm import tqdm

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Get all computers
    computers = set()
    for line in lines:
        computers.add(line[0:2])
        computers.add(line[3:5])

    # Store all connections in dictionary
    connections = {elem: set() for elem in computers}
    for line in lines:
        connections[line[0:2]].add(line[3:5])
        connections[line[3:5]].add(line[0:2])

    # For each triplet, check if they have 1 to 1
    connected_sets = []
    for c1 in computers:
        for c2 in computers:
            if c1 == c2:
                continue
            for c3 in computers:
                if c1 == c3 or c2 == c3:
                    continue

                if c1 in connections[c2] and c1 in connections[c3] and c2 in connections[c3]:
                    if set([c1, c2, c3]) not in connected_sets:
                        connected_sets.append(set([c1, c2, c3]))
    
    # Filter the list for sets containing letter t
    def set_contains_t(s):
        for elem in s:
            if 't' == elem[0]:
                return True
        return False
    
    final_list = list(filter(set_contains_t, connected_sets))
    print(final_list)
    print(len(final_list))
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Get all computers
    computers = set()
    for line in lines:
        computers.add(line[0:2])
        computers.add(line[3:5])

    # Store all connections in adj list dictionary
    connections = {elem: set() for elem in computers}
    for line in lines:
        connections[line[0:2]].add(line[3:5])
        connections[line[3:5]].add(line[0:2])
    
    # Function that finds the largest complete subgraph starting at given node
    def largest_complete_subgraph(node):
        # Setup the set of vertices
        current_subgraph = set()
        best_subgraph = set()

        # dfs helper
        def dfs(u):
            # Determine if u connects with everything in current subgraph
            if current_subgraph.issubset(connections[u]):
                # Add to subgraph and replace best if needed
                current_subgraph.add(u)
                if len(current_subgraph) > len(best_subgraph):
                    best_subgraph.clear()
                    best_subgraph.update(current_subgraph)

                # Go over all unvisited neighbours
                for v in connections[u]:
                    if v not in current_subgraph:
                        dfs(v)
                
                # Remove from current subgraph
                current_subgraph.remove(u)

        # Identify set of vertices making largest complete subgraph
        dfs(node)

        return best_subgraph

    max_set = set()
    for node in tqdm(computers):
        subgraph = largest_complete_subgraph(node)
        x = list(subgraph)
        x.sort()
        print(x)
        if len(subgraph) > len(max_set):
            max_set = subgraph.copy()

    print(max_set)
    pass


def part2_alt() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Get all computers
    computers = set()
    for line in lines:
        computers.add(line[0:2])
        computers.add(line[3:5])

    # Store all connections in adj list dictionary
    connections = {elem: set() for elem in computers}
    for line in lines:
        connections[line[0:2]].add(line[3:5])
        connections[line[3:5]].add(line[0:2])
    
    # Function that finds the largest complete subgraph starting at given node
    def largest_complete_subgraph(node):
        # Set up list of cliques
        cliques = [set([node])]

        # Go over the neighbours of the node
        for neighbour in connections[node]:
            # Determine if neighbour connects to any of the cliques, otherwise make new one
            flag = True
            for clique in cliques:
                if clique.issubset(connections[neighbour]):
                    clique.add(neighbour)
                    flag = False

            if flag:
                # No clique allowed neighbour, make new one
                cliques.append(set([node, neighbour]))

        # Return the largest sized clique
        return max(cliques, key=len)


    max_set = []
    for node in tqdm(computers):
        subgraph = largest_complete_subgraph(node)
        x = list(subgraph)
        x.sort()
        print(x)
        if len(subgraph) > len(max_set):
            max_set = x

    print(list(max_set))
    pass


if __name__ == "__main__":
    # part1()
    # part2()
    part2_alt()