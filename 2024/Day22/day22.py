import sys
from collections import deque
import re

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    def simulate_generation(initial, n):
        secret = initial
        for _ in range(n):
            secret = next_secret_number(secret)
        return secret


    def next_secret_number(secret_number):
        # Step 1
        result = secret_number * 64
        secret_number ^= result
        secret_number %= 16777216

        # Step 2
        result = secret_number // 32
        secret_number ^= result
        secret_number %= 16777216

        # Step 3
        result = secret_number * 2048
        secret_number ^= result
        secret_number %= 16777216

        return secret_number
    
    total = 0
    for line in lines:
        total += simulate_generation(int(line.strip()), 2000)
    print(total)
    pass



def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()


    def get_lists(initial, n):
        # Set up lists
        change_list = []
        banana_list = []

        # Generate n secret numbers and keep track of the change and banana count
        current = initial
        for _ in range(n):
            next = next_secret_number(current)
            change = (next % 10) - (current % 10)
            change_list.append(f",{change}")
            if change < 0:
                banana_list.append(None)
                banana_list.append(None)
                banana_list.append(next % 10)
            else:
                banana_list.append(None)
                banana_list.append(next % 10)
            current = next
        
        # Change into string for easy regex matching
        change_list = "".join(change_list)
        return change_list, banana_list


    def next_secret_number(secret_number):
        # Step 1
        result = secret_number * 64
        secret_number ^= result
        secret_number %= 16777216

        # Step 2
        result = secret_number // 32
        secret_number ^= result
        secret_number %= 16777216

        # Step 3
        result = secret_number * 2048
        secret_number ^= result
        secret_number %= 16777216

        return secret_number
    

    def optimal_bananas(change_table, banana_table, sequence):
        total = 0
        for i, changestr in enumerate(change_table):
            # Search the changestr for sequence
            x = re.search(sequence, changestr)

            # If a match was found, get corresponding bananas
            if x is not None:
                position = x.span()[1] - 1
                total += banana_table[i][position]
        return total
        

    def trial_all_sequences():
        # Setup sequence tracking (heuristics)
        low = [-2, -2, -2, 0]
        high = [5, 5, 5, 5]
        bestScore = 0
        bestSequence = None

        # Set up table of known (change, banana) per buyer
        change_table = [0]*len(lines)
        banana_table = [0]*len(lines)
        for i in range(len(lines)):
            change_table[i], banana_table[i] = get_lists(int(lines[i].strip()), 2000)
        
        # Go over every possible sequence
        for a in range(low[0], high[0] + 1):
            for b in range(low[1], high[1] + 1):
                for c in range(low[2], high[2] + 1):
                    for d in range(low[3], high[3] + 1):
                        # Search for sequence in table per buyer
                        sequence = f",{a},{b},{c},{d}"
                        print([a, b, c, d])
                        total = optimal_bananas(change_table, banana_table, sequence)
                        if total > bestScore:
                            bestScore = total
                            bestSequence = sequence

        return bestScore, bestSequence
    
    bananas, sequence = trial_all_sequences()
    print(f"{bananas} bananas w/ sequence {sequence}")
    pass


if __name__ == "__main__":
    part1()
    part2()