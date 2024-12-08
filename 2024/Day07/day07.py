import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    results = []
    numbers = []
    for line in lines:
        result_and_values = line.split(":")
        results.append(int(result_and_values[0]))
        numbers.append(list(map(int, result_and_values[1].strip().split(" "))))

    total = 0
    for i in range(len(results)):
        result = results[i]
        equation = numbers[i]
        if isPossible(result, equation):
            total += result

    print(total)
    pass

def isPossible(result, equation: list[int]):
    if len(equation) == 1:
        return result == equation[0]
    else:
        if isPossible(result - equation[-1], equation[:-1]) or isPossible(result/equation[-1], equation[:-1]):
            return True
        return False


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    results = []
    numbers = []
    for line in lines:
        result_and_values = line.split(":")
        results.append(int(result_and_values[0]))
        numbers.append(list(map(int, result_and_values[1].strip().split(" "))))

    total = 0
    for i in range(len(results)):
        result = results[i]
        equation = numbers[i]
        if isPossible2(result, equation):
            total += result

    print(total)
    pass


def isPossible2(result, equation: list[int]):
    if len(equation) == 1:
        return result == equation[0]
    else:
        if isPossible2(result - equation[-1], equation[:-1]):
            return True
        
        if result % equation[-1] == 0 and isPossible2(result//equation[-1], equation[:-1]):
            return True
        
        last_num_string = str(equation[-1])
        result_string = str(result)
        if len(result_string) >= len(last_num_string) and result_string[len(result_string) - len(last_num_string) : len(result_string)] == last_num_string:

            if len(result_string[:len(result_string) - len(last_num_string)]) > 0:
                if isPossible2(int(result_string[:len(result_string) - len(last_num_string)]), equation[:-1]):
                    return True
        return False



if __name__ == "__main__":
    part1()
    part2()