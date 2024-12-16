import sys
import matplotlib.pyplot as plt

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Parse information
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    robots = []
    for line in lines:
        pv = line.strip().split(" ")
        p = pv[0]
        v = pv[1]
        p = p[2:]
        v = v[2:]

        # Parse position
        position = list(map(int, p.split(",")))
        velocity = list(map(int, v.split(",")))
        robots.append((position, velocity))

    # Simulate the robot by updating their position
    for _ in range(100):
        for i in range(len(robots)):
            robot = robots[i]
            pos, vel = robot

            # Update the position by the velocity using modulo wrapper
            new_pos = [(pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height]

            robots[i] = (new_pos, vel)

    quadrants = [0]*4
    for (x, y), _ in robots:
        # Count number of robots in top-left quadrant
        if x < width//2 and y < height//2:
            quadrants[0] += 1

        # Count number of robots in top-right quadrant
        elif x > width//2 and y < height//2:
            quadrants[1] += 1

        # Count number of robots in bottom-left quadrant
        elif x < width//2 and y > height//2:
            quadrants[2] += 1
            
        # Count number of robots in bottom-right quadrant
        elif x > width//2 and y > height//2:
            quadrants[3] += 1

    print(quadrants)
    print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
    pass




def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Parse information
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    robots = []
    for line in lines:
        pv = line.strip().split(" ")
        p = pv[0]
        v = pv[1]
        p = p[2:]
        v = v[2:]

        # Parse position
        position = list(map(int, p.split(",")))
        velocity = list(map(int, v.split(",")))
        robots.append((position, velocity))

    # Initial grid
    init_grid = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(len(robots)):
        robot = robots[i]
        pos, vel = robot

        # Fill grid with robot position
        init_grid[pos[1]][pos[0]] += 1


    # Simulate the robot by updating their position
    for time in range(1, 10404):
        print(f"After {time} seconds:\n")
        
        # Make grid
        grid = [[0 for _ in range(width)] for _ in range(height)]

        for i in range(len(robots)):
            robot = robots[i]
            pos, vel = robot

            # Update the position by the velocity using modulo wrapper
            new_pos = [(pos[0] + vel[0]) % width, (pos[1] + vel[1]) % height]
            robots[i] = (new_pos, vel)

            # Fill grid with robot position
            grid[new_pos[1]][new_pos[0]] = 1
        
        # Print grid
        if (time - 57) % 103 == 0 and (time - 86) % 101 == 0:
            print_grid(grid)
            input()
    pass


def print_grid(grid):
    # with open("out.txt", 'w') as f:
    #     for row in grid:
    #         print(row, file=f)
    plt.imsave("out.png", grid)
    


if __name__ == "__main__":
    part1()
    part2()