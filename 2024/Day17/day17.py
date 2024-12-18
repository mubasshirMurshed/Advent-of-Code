import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Parse information
    regA = int(lines[0][12:].strip())
    regA = (8**15)*5 + (8**14)*3 + (8**13)*2 + (8**12)*5 + (8**11)*3 + \
    (8**10)*7 + (8**9)*6 + (8**8)*6 + (8**7)*4 + (8**6)*6 + (8**5)*2 + (8**4)*3 + \
    (8**3)*6 + (8**2)*0 + (8**1) + (8**0)*7
    print(regA)
    regB = int(lines[1][12:].strip())
    regC = int(lines[2][12:].strip())
    program = list(map(int, lines[4][9:].strip().split(',')))
    ip = 0

    # Define combo operand returns
    def combo_operand(number):
        match number:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return regA
            case 5:
                return regB
            case 6:
                return regC
            case _:
                raise ValueError("Incorrect combo operand")

    output = []
    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]
        match opcode:
            case 0:
                regA //= 1 << combo_operand(operand)
            case 1:
                regB ^= operand
            case 2:
                regB = combo_operand(operand) % 8
            case 3:
                if regA != 0:
                    ip = operand
                    ip -= 2
            case 4:
                regB ^= regC
            case 5:
                output.append(combo_operand(operand) % 8)
            case 6:
                regB = regA // (1 << combo_operand(operand))
            case 7:
                regC = regA // (1 << combo_operand(operand))
            case _:
                raise ValueError("Incorrect opcode")
            
        # Increment instruction pointer
        ip += 2

    # Print the output
    for i, out in enumerate(output):
        if i < len(output) - 1:
            print(out, end=",")
        else:
            print(out)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    
    # Parse information
    regA = int(lines[0][12:].strip())
    regB = int(lines[1][12:].strip())
    regC = int(lines[2][12:].strip())
    program = list(map(int, lines[4][9:].strip().split(',')))
    
    # Define combo operand returns
    def combo_operand(number):
        match number:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return regA
            case 5:
                return regB
            case 6:
                return regC
            case _:
                raise ValueError("Incorrect combo operand")

    ip = 0
    output = []
    A = 8**(len(program) - 1)
    regA = A
    regB = 0
    regC = 0
    while A < 8**len(program):
        print(A)
        while ip < len(program) - 1:
            opcode = program[ip]
            operand = program[ip + 1]
            match opcode:
                case 0:
                    regA //= 1 << combo_operand(operand)
                case 1:
                    regB ^= operand
                case 2:
                    regB = combo_operand(operand) % 8
                case 3:
                    if regA != 0:
                        ip = operand
                        ip -= 2
                case 4:
                    regB ^= regC
                case 5:
                    output.append(combo_operand(operand) % 8)
                case 6:
                    regB = regA // (1 << combo_operand(operand))
                case 7:
                    regC = regA // (1 << combo_operand(operand))
                case _:
                    raise ValueError("Incorrect opcode")
                
            # Increment instruction pointer
            ip += 2

        if output == program:
            print(f"Found number: {A}!!!!!")
            break
        
        A += 1
        regA = A
        regB = 0
        regC = 0
        ip = 0
        output = []
        

    # Print the output
    for i, out in enumerate(output):
        if i < len(output) - 1:
            print(out, end=",")
        else:
            print(out)
    pass


if __name__ == "__main__":
    part1()
    # part2()