import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    total = 0
    # Search horizontal ones
    for line in lines:
        total += line.count("XMAS")
        total += line.count("SAMX")

    # Search vertical ones
    for i in range(len(lines[0])):
        column = "".join([lines[j][i] for j in range(len(lines))])
        total += column.count("XMAS")
        total += column.count("SAMX")

    # Search diagonals
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                # Search NW
                if i >= 3 and j >= 3 and lines[i-1][j-1] == "M" and lines[i-2][j-2] == "A" and lines[i-3][j-3] == "S":
                    total += 1

                # Search NE
                if i >= 3 and j < len(lines[i])-3 and lines[i-1][j+1] == "M" and lines[i-2][j+2] == "A" and lines[i-3][j+3] == "S":
                    total += 1

                # Search SW
                if i < len(lines)-3 and j >= 3 and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                    total += 1

                # Search SE
                if i < len(lines)-3 and j < len(lines[i])-3 and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                    total += 1

    print(total)
    
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    total = 0

    # Search diagonals
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "A":
                count = 0
                
                if 1 <= i < len(lines)-1 and 1 <= j < len(lines[i])-1:
                    # Search NW-SE diagonal is MAS or SAM
                    if lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S":
                        count += 1
                    elif lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M":
                        count += 1

                    # Search NE-SW diagonal is MAS or SAM
                    if lines[i+1][j-1] == "M" and lines[i-1][j+1] == "S":
                        count += 1
                    elif lines[i+1][j-1] == "S" and lines[i-1][j+1] == "M":
                        count += 1
                
                    if count == 2:
                        total += 1

    print(total)
    pass


if __name__ == "__main__":
    part1()
    part2()