import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.read()

    # Parse information
    items = lines.strip().split("\n\n")
    items = [item.split("\n") for item in items]
    keys = []
    locks = []
    for item in items:
        if item[0] == ".....":
            keys.append(item)
        else:
            locks.append(item)
    
    # Get key pins
    for idx, key in enumerate(keys):
        # Make space for heights of key
        keyheights = [0]*len(key[0])

        # Go over each column
        for j in range(len(key[0])):
            # Determine height of the column for a key
            for i in range(1, len(key)):
                if key[i][j] == "#":
                    keyheights[j] = 6 - i
                    break
        
        # Replace key with the heights
        keys[idx] = keyheights

    # Get lock pins
    for idx, lock in enumerate(locks):
        # Make space for heights of lock
        lockheights = [0]*len(lock[0])

        # Go over each column
        for j in range(len(lock[0])):
            # Determine height of the column for a lock
            for i in range(1, len(lock)):
                if lock[i][j] == ".":
                    lockheights[j] = i - 1
                    break
        
        # Replace lock with the heights
        locks[idx] = lockheights


    def fits(key, lock):
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                return False
        return True

    # Try every key
    count = 0
    for key in keys:
        # Try to fit this key with a lock
        for lock in locks:
            if fits(key, lock):
                count += 1
    print(count)
    pass

if __name__ == "__main__":
    part1()