import sys
from tqdm import tqdm
import math
import time

sys.setrecursionlimit(50000)

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        line = list(map(int, f.read().strip().split(" ")))

    # print(f"Initial arrangement:\n{line}\n")
    digits_dict = dict()
    first_halves = dict()
    second_halves = dict()
    
    for iteration in tqdm(range(int(sys.argv[2]))):
        new_line = []
        
        for number in line:
            if number == 0:
                new_line.append(1)
                continue

            if number not in digits_dict:
                digits = math.floor(math.log10(number) + 1)
                digits_dict[number] = digits
            else:
                digits = digits_dict[number]
            if not (digits & 1):
                if number not in first_halves:
                    half_digits = digits//2
                    power = 10**half_digits
                    first_half = number // power
                    second_half = number - first_half*power
                    first_halves[number] = first_half
                    second_halves[number] = second_half
                else:
                    first_half = first_halves[number]
                    second_half = second_halves[number]
                new_line.append(first_half)
                new_line.append(second_half)
            else:
                new_line.append(number*2024)

        line = new_line
        # print(f"After {iteration+1} blink:\n{line}\n")

    print(len(line))
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        line = list(map(int, f.read().strip().split(" ")))

    digits_dict = dict()
    first_halves = dict()
    second_halves = dict()

    def update(line: list):
        for i, element in enumerate(line):
            if type(element) == int:
                if element == 0:
                    line[i] = 1
                    continue

                if element not in digits_dict:
                    digits = math.floor(math.log10(element) + 1)
                    digits_dict[element] = digits
                else:
                    digits = digits_dict[element]

                if not (digits & 1):
                    if element not in first_halves:
                        half_digits = digits//2
                        power = 10**half_digits
                        first_half = element // power
                        second_half = element - first_half*power
                        first_halves[element] = first_half
                        second_halves[element] = second_half
                    else:
                        first_half = first_halves[element]
                        second_half = second_halves[element]
                    line[i] = [first_half, second_half]
                else:
                    line[i] = element*2024
            else:
                update(element)

    def length(line: list):
        total = 0
        for element in line:
            if type(element) == int:
                total += 1
            else:
                total += length(element)
        return total
    
    for iteration in tqdm(range(int(sys.argv[2]))):
        update(line)

    print(length(line))
    pass


def part2_alt() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        line = list(map(int, f.read().strip().split(" ")))

    digits_dict = dict()
    first_halves = dict()
    second_halves = dict()
    number_of_stones = dict()

    def process(number: int, remainingBlinks: int):
        # Check if already in dict
        if (number, remainingBlinks) in number_of_stones:
            return number_of_stones[(number, remainingBlinks)]

        # Calculate the number of stones this number gives rise to
        if remainingBlinks == 0:
            number_of_stones[(number, remainingBlinks)] = 1
        else:
            if number == 0:
                number_of_stones[(0, remainingBlinks)] = process(1, remainingBlinks-1)
            else:
                # Get number of digits of number
                if number not in digits_dict:
                    digits = math.floor(math.log10(number) + 1)
                    digits_dict[number] = digits
                else:
                    digits = digits_dict[number]

                # If even number of digits, split in halves
                if not (digits & 1):
                    if number not in first_halves:
                        half_digits = digits // 2
                        power = 10**half_digits
                        first_half = number // power
                        second_half = number - first_half*power
                        first_halves[number] = first_half
                        second_halves[number] = second_half
                    else:
                        first_half = first_halves[number]
                        second_half = second_halves[number]
                    
                    number_of_stones[(number, remainingBlinks)] = process(first_half, remainingBlinks-1) + process(second_half, remainingBlinks-1)

                else:
                    number_of_stones[(number, remainingBlinks)] = process(number*2024, remainingBlinks-1)

        return number_of_stones[(number, remainingBlinks)]
    
    
    total = 0
    for element in line:
        total += process(element, int(sys.argv[2]))

    print(total)
    pass


if __name__ == "__main__":
    # part1()
    # part2()
    start = time.perf_counter()
    part2_alt()
    end = time.perf_counter()
    print(f"Took {end - start} seconds.")