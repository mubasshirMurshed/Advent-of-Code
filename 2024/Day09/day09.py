import sys
from tqdm import tqdm

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        line = list(map(int,f.read().strip()))
    
    # Decode the blocks
    decoded = []
    for i in range(0, len(line), 2):
        decoded.extend([i//2]*line[i])
        if i + 1 < len(line):
            decoded.extend(['.']*line[i+1])
    
    # Move blocks into free space
    start_pointer = 0
    end_pointer = len(decoded) - 1
    while start_pointer < end_pointer:
        # Have start pointer point to next available free space
        while decoded[start_pointer] != ".":
            start_pointer += 1

        # Have end pointer point to actual number
        while decoded[end_pointer] == ".":
            end_pointer -= 1

        if start_pointer >= end_pointer:
            break

        # Swap
        decoded[start_pointer], decoded[end_pointer] = decoded[end_pointer], decoded[start_pointer]

    # Calculate checksum
    total = 0
    for i in range(len(decoded)):   
        if decoded[i] != ".": 
            total += i*decoded[i]
        else:
            break
    print(total)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        line = list(map(int,f.read().strip()))
    
    # Decode the blocks
    decoded = []
    files = []
    empty = []
    for i in range(0, len(line), 2):
        files.append((len(decoded), line[i]))
        decoded.extend([i//2]*line[i])
        
        if i + 1 < len(line):
            empty.append((len(decoded), line[i+1]))
            decoded.extend(['.']*line[i+1])

    # Move blocks into free space
    for block_pointer in tqdm(range(len(files) - 1, -1, -1)):
        file_idx = files[block_pointer][0]
        file_size = files[block_pointer][1]

        # Attempt to move files[block_pointer] into any available space
        for i, (idx, size) in enumerate(empty):
            # Only if empty space is left side of file block
            if idx >= file_idx:
                break
            
            # Only move if enough space
            if file_size > size:
                continue

            # Do the swap
            for t in range(file_size):
                decoded[idx + t] = decoded[file_idx + t]
                decoded[file_idx + t] = "."

            empty[i] = (idx + file_size, size - file_size)
            break

    # Calculate checksum
    total = 0
    for i in range(len(decoded)):   
        if decoded[i] != ".": 
            total += i*decoded[i]
    print(total)
    pass


if __name__ == "__main__":
    part1()
    part2()