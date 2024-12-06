import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    # Get dimensions of map
    width = len(lines[0])
    height = len(lines)

    # Locate guard (pointing up)
    found = False
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                guard_pos = [x, y]
                found = True
                break
        if found:
            break
    
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]

    current_dir_idx = 0
    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        # Get direction
        current_dir = directions[current_dir_idx]

        # Check next spot
        next_pos = [guard_pos[0] + current_dir[0], guard_pos[1] + current_dir[1]]

        # If next pos is beyond border, exit loop
        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
            break

        # Check if obstacle there and rotate if needed
        if lines[next_pos[1]][next_pos[0]] == "#":
            current_dir_idx = (current_dir_idx + 1) % len(directions)
        # Free spot
        else:
            # Mark guard pos with 'X'
            string = list(lines[guard_pos[1]])
            string[guard_pos[0]] = 'X'
            lines[guard_pos[1]] = "".join(string)

            # Update guard position
            guard_pos = next_pos

    # Count number of 'X'
    total = 1
    for line in lines:
        total += line.count('X')

    print(total)

    pass




def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]

    # Get dimensions of map
    width = len(lines[0])
    height = len(lines)

    # Locate guard (pointing up)
    found = False
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                initial_guard_pos = [x, y]
                found = True
                break
        if found:
            break
    
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]

    direction_symbols = [
        "$",
        ">",
        "v",
        "<"
    ]

    # Try every position as potential obstacle placement
    count = 0
    for x in range(width):
        for y in range(height):
            # Create the initial guard pos
            guard_pos = [initial_guard_pos[0], initial_guard_pos[1]]

            # Skip if obstacle is on the guard pos or any existing obstacles
            if (guard_pos[0] == x and guard_pos[1] == y) or lines[y][x] == "#":
                continue

            # Create duplicate map
            map = lines[:]
            obstacle_pos = [x, y]

            # Run simulation until you visit a cell that has the same direction registered
            current_dir_idx = 0
            counter = 0
            while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height and counter < width*height:
                # Get direction
                current_dir = directions[current_dir_idx]

                # Check next spot
                next_pos = [guard_pos[0] + current_dir[0], guard_pos[1] + current_dir[1]]

                # If next pos is beyond border, exit loop
                if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
                    break

                # If current pos has same direction marked already as current direction, update cycle count and exit loop 
                if map[guard_pos[1]][guard_pos[0]] == direction_symbols[current_dir_idx]:
                    count += 1
                    break

                # Check if obstacle there and rotate if needed
                if map[next_pos[1]][next_pos[0]] == "#" or next_pos == obstacle_pos:
                    current_dir_idx = (current_dir_idx + 1) % len(directions)
                else:
                    # Mark guard pos with direction traversed
                    string = list(map[guard_pos[1]])
                    string[guard_pos[0]] = direction_symbols[current_dir_idx]
                    map[guard_pos[1]] = "".join(string)

                    # Update guard position
                    guard_pos = next_pos
                counter += 1
            
            # This counter mechanism is purely for safety
            if counter >= width*height:
                count += 1


    print(count)
    
    pass


if __name__ == "__main__":
    part1()
    part2()