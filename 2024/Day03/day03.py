import sys
import re

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    memory = ""
    for line in lines:
        memory += line

    x = re.findall("mul\([0-9]+,[0-9]+\)", memory)
    total = 0
    for operation in x:
        comma_idx = operation.find(",")
        first_num = int(operation[4:comma_idx])
        second_num = int(operation[comma_idx+1: len(operation)-1])
        total += first_num*second_num

    print(total)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    memory = ""
    for line in lines:
        memory += line

    # Get indices of each expression of interest
    muls = list(re.finditer("mul\([0-9]+,[0-9]+\)", memory))
    enables = list(re.finditer("do\(\)", memory))
    disables = list(re.finditer("don't\(\)", memory))
    
    # Create an ordering of each instruction based on their location
    instructions = [0]*len(memory)
    for a in muls:
        instructions[a.span()[0]] = a.group()

    for a in enables:
        instructions[a.span()[0]] = 1

    for a in disables:
        instructions[a.span()[0]] = 2

    # Sum up the valid muls
    total = 0
    enabled = True
    for operation in instructions:
        if operation == 0:
            continue
        elif operation == 1:
            enabled = True
        elif operation == 2:
            enabled = False
        else:
            if enabled:
                comma_idx = operation.find(",")
                first_num = int(operation[4:comma_idx])
                second_num = int(operation[comma_idx+1: len(operation)-1])
                total += first_num*second_num
    print(total)
    pass

def part2_alt() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        memory = f.read()

    # Get indices of each expression of interest
    instructions = list(re.finditer("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", memory))
    instructions = [match.group() for match in instructions]

    # Sum up the valid muls
    total = 0
    enabled = True
    for operation in instructions:
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            enabled = False
        else:
            if enabled:
                comma_idx = operation.find(",")
                first_num = int(operation[4:comma_idx])
                second_num = int(operation[comma_idx+1: len(operation)-1])
                total += first_num*second_num
    print(total)
    pass


if __name__ == "__main__":
    part1()
    part2()
    part2_alt()