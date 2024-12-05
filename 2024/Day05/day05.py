import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    rules = []
    updates = []
    parsing_rules = True
    for line in lines:
        if line == '\n':
            parsing_rules = False
        elif parsing_rules:
            rules.append(list(map(int, line.strip().split("|"))))
        else:
            updates.append(list(map(int, line.strip().split(","))))
    
    # Iterate over each update and determine if correctly ordered
    correct = []
    for update in updates:
        if isOrdered(update, rules):
            correct.append(update)
    
    # Find sum of middle number of each
    total = 0
    for update in correct:
        total += update[len(update)//2]
    
    print(total)
    pass


def isOrdered(update, rules):
    for i in range(len(update) - 1):
        number = update[i]
        for rule in rules:
            if rule[0] == number and rule[1] in update:
                if rule[1] not in update[i:]:
                    return False
                
    # Do specific case for last number
    number = update[-1]
    for rule in rules:
        if rule[0] == number and rule[1] in update:
            return False

    return True


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    rules = []
    updates = []
    parsing_rules = True
    for line in lines:
        if line == '\n':
            parsing_rules = False
        elif parsing_rules:
            rules.append(list(map(int, line.strip().split("|"))))
        else:
            updates.append(list(map(int, line.strip().split(","))))
    
    # Iterate over each update and determine if correctly ordered
    incorrect = []
    for update in updates:
        if not isOrdered(update, rules):
            incorrect.append(update)

    # Fix these to be correct
    fixed = []
    for update in incorrect:
        fixed.append(fixUpdate(update, rules))
    
    # Find sum of middle number of each
    total = 0
    for update in fixed:
        total += update[len(update)//2]
    
    print(total)
    pass


def fixUpdate(update, rules):
    # Create adj list of nodes involved in the update
    adj_list = dict()
    for element in update:
        adj_list[element] = []

    # Connect edges based on rules a|b only if a and b are in the update
    for a, b in rules:
        if a in update and b in update:
            adj_list[a].append(b)
    
    # Perform a dfs on the adj list to obtain a reverse topological order
    visited = dict()
    for element in update:
        visited[element] = False

    result = []
    for vertex in adj_list:
        if visited[vertex] == False:
            dfs(vertex, result, adj_list, visited)

    # Reverse the reverse topological order
    result.reverse()

    return result



def dfs(u, array, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, array, graph, visited)
    array.append(u)
    return


if __name__ == "__main__":
    part1()
    part2()