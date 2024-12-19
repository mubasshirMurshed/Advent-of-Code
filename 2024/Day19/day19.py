import sys
from tqdm import tqdm
from functools import cache

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    towels = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:]]

    @cache
    def isPossible(design, idx):
        # Determine if design[idx:] is possible
        if idx == len(design):
            return True
        
        for towel in towels:
            if idx == 0 and towel == design:
                continue
            
            if idx + len(towel) <= len(design) and towel == design[idx:idx + len(towel)]:
                if isPossible(design, idx + len(towel)):
                    return True

        return False
    
    # Filter towels that can already be made of smaller towels (optimisation)
    new_towels = []
    for towel in towels:
        if not isPossible(towel, 0):
            new_towels.append(towel)
    towels = new_towels

    count = 0
    for design in tqdm(designs):
        if isPossible(design, 0):
            count += 1

    print(count)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    towels = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:]]
    results = dict()

    def isPossible(design, idx):
        if (design, idx) in results:
            return results[(design, idx)]
        
        # Determine number of possible ways to make design[idx:]
        if idx == len(design):
            # Base case, only 1 way to make empty string
            results[(design, idx)] = 1
        else:
            # Start with 0 ways
            results[(design, idx)] = 0
            for towel in towels:
                if idx + len(towel) <= len(design) and towel == design[idx:idx + len(towel)]:
                    results[(design, idx)] += isPossible(design, idx + len(towel))
        return results[(design, idx)]
    
    count = 0
    for design in tqdm(designs):
        count += isPossible(design, 0)

    print(count)
    pass


if __name__ == "__main__":
    part1()
    # part2()