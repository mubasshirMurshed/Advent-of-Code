import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    map = [list(line.strip()) for line in lines]

    # Process map by finding each type of antenna and a list of their locations
    antennas = dict()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ".":
                continue
            if map[i][j] not in antennas:
                antennas[map[i][j]] = [[i, j]]
            else:
                antennas[map[i][j]].append([i, j])

    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            # Check if tile map[i, j] is an antinode
            if isAntinode(antennas, i, j):
                count += 1

    print(count)
    pass


def isAntinode(antennas, i, j):
    # Iterate over each type of antenna and their positions
    for _, positions in antennas.items():
        # Iterate over each position
        for x in range(len(positions)):
            # Compare this to every other position
            for y in range(x + 1, len(positions)):
                i1, j1 = positions[x]
                i2, j2 = positions[y]

                # Check if the squared distances of one of these positions is 4x the other
                dist1 = (i-i1)**2 + (j-j1)**2
                dist2 = (i-i2)**2 + (j-j2)**2
                if not (dist1 == 4*dist2 or dist2 == 4*dist1):
                    continue

                # Check if these are in line (using vector dot product)
                vec1 = (i1 - i, j1 - j)
                vec2 = (i2 - i, j2 - j)
                if (vec1[0]*vec2[0] + vec1[1]*vec2[1])**2 == dist1*dist2:
                    return True

    return False




def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    map = [list(line.strip()) for line in lines]

    # Process map by finding each type of antenna and a list of their locations
    antennas = dict()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ".":
                continue
            if map[i][j] not in antennas:
                antennas[map[i][j]] = [[i, j]]
            else:
                antennas[map[i][j]].append([i, j])

    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            # Check if tile map[i, j] is an antinode
            if isAntinode2(antennas, i, j):
                count += 1

    print(count)
    pass


def isAntinode2(antennas, i, j):
    # Iterate over each type of antenna and their positions
    for _, positions in antennas.items():
        # Iterate over each position
        for x in range(len(positions)):
            # Compare this to every other position
            for y in range(x + 1, len(positions)):
                i1, j1 = positions[x]
                i2, j2 = positions[y]

                # Get squared distance
                dist1 = (i-i1)**2 + (j-j1)**2
                dist2 = (i-i2)**2 + (j-j2)**2

                # Check if these are in line (using vector dot product)
                vec1 = (i1 - i, j1 - j)
                vec2 = (i2 - i, j2 - j)
                if (vec1[0]*vec2[0] + vec1[1]*vec2[1])**2 == dist1*dist2:
                    return True

    return False


if __name__ == "__main__":
    part1()
    part2()