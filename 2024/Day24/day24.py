import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.read()
    
    # Parse data
    initial_values, gates = lines.split("\n\n")
    
    # Add in all the initial values as known
    values = dict()
    initial_values = initial_values.split("\n")
    for string in initial_values:
        values[string[0:3]] = int(string[-1])

    # Parse the instructions
    z_num = 0
    instructions = dict()
    for expr in gates.strip().split("\n"):
        terms = expr.strip("\n").split(" ")
        instructions[terms[4]] = [terms[0], terms[2], terms[1]]
        if terms[4][0] =='z':
            if int(terms[4][1:]) > z_num:
                z_num = int(terms[4][1:])
    z_num += 1

    # Function to get values or recursively compute them if needed
    def get_value(wire):
        if wire not in values:
            a, b, gate = instructions[wire]
            aVal = get_value(a)
            bVal = get_value(b)
            match gate:
                case "AND":
                    values[wire] = aVal & bVal
            match gate:
                case "OR":
                    values[wire] = aVal | bVal
            match gate:
                case "XOR":
                    values[wire] = aVal ^ bVal

        return values[wire]

    # Get z{z_num} to z00
    bitlist = []
    for i in range(z_num):
        wire = f"z{i:02}"
        bitlist.append(get_value(wire))

    # Convert bitlist to decimal
    total = 0
    for i in range(len(bitlist)):
        total += bitlist[i]*(2**i)
    print(len(instructions))
    print(total)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.read()
    
    # Parse data
    initial_values, gates = lines.split("\n\n")
    
    # Add in all the initial values as known
    values = dict()
    initial_values = initial_values.split("\n")
    for string in initial_values:
        values[string[0:3]] = int(string[-1])

    # Parse the instructions
    z_num = 0
    instructions = dict()
    for expr in gates.strip().split("\n"):
        terms = expr.strip("\n").split(" ")
        instructions[terms[4]] = [terms[0], terms[2], terms[1]]
        if terms[4][0] =='z':
            if int(terms[4][1:]) > z_num:
                z_num = int(terms[4][1:])
    z_num += 1

    def find_output(wire1, wire2, gate):
        for output, (a, b, g) in instructions.items():
            if (wire1 in [a, "*"] and wire2 in [b, "*"]) or (wire1 in [b, "*"] and wire2 in [a, "*"]):
                if gate == g:
                    return output
        return None

    bad_wires = []

    def swap(wire1, wire2):
        # Swaps the instruction between these two wires
        temp = instructions[wire1]
        instructions[wire1] = instructions[wire2]
        instructions[wire2] = temp
        bad_wires.extend([wire1, wire2])

    # Function to verify correct full adder connections
    def verify_full_adder(n, carry_in):
        print("-"*20)
        # Verify zn
        z_instr = instructions[f"z{n:02}"]
        if not ("XOR" in z_instr and carry_in in z_instr):
            # Fix by swapping
            z_out = find_output("*", carry_in, "XOR")
            swap(z_out, f"z{n:02}")
            z_instr = instructions[f"z{n:02}"]
        print(f"{z_instr[0]} XOR {z_instr[1]} -> z{n:02}")

        # Verify a
        a = z_instr[0] if carry_in == z_instr[1] else z_instr[1]
        a_out = find_output(f"x{n:02}", f"y{n:02}", "XOR")
        if a_out != a:
            # Fix by swapping
            swap(a, a_out)
        print(f"x{n:02} XOR y{n:02} -> {a}    (a)")

        # Verify b and c
        b_out = find_output(a, carry_in, "AND")
        c_out = find_output(f"x{n:02}", f"y{n:02}", "AND")
        if find_output(b_out, c_out, "OR") is None:
            if find_output(b_out, "*", "OR") is None:
                if find_output(c_out, "*", "OR") is None:
                    # Both b_out and c_out are wrong
                    raise ValueError(f"""Both b and c cannot be found. Means both were swapped.""")
                else:
                    # b_out is wrong, c_out is right
                    carry_out = find_output(c_out, "*", "OR")
                    cout_instr = instructions[carry_out]
                    b = cout_instr[0] if c_out == cout_instr[1] else cout_instr[1]
                    c = c_out
                    raise ValueError(f"""Wrong 'b'.\nExpected ({a} AND {carry_in} -> {b})\
 but instead found ({a} AND {carry_in} -> {b_out})""")
            else:
                # b_out is right, c_out is wrong
                carry_out = find_output(b_out, "*", "OR")
                cout_instr = instructions[carry_out]
                b = b_out
                c = cout_instr[0] if b_out == cout_instr[1] else cout_instr[1]
                raise ValueError(f"""Wrong 'c'.\nExpected (x{n:02} AND y{n:02} -> {c})\
 but instead found (x{n:02} AND y{n:02} -> {c_out})""")
        else:
            carry_out = find_output(b_out, c_out, "OR")
            b = b_out
            c = c_out

        print(f"{a} AND {carry_in} -> {b}    (b)")
        print(f"x{n:02} AND y{n:02} -> {c}    (c)")
        print(f"{b} OR {c} -> {carry_out}    (cout)")
        print("-"*20)
        
        return carry_out
    
    carry_in = find_output("x00", "y00", "AND")
    for i in range(1, 45):
        carry_in = verify_full_adder(i, carry_in)

    bad_wires.sort()
    print("The bad wires:")
    for i in range(len(bad_wires)):
        if i == len(bad_wires) - 1:
            print(bad_wires[i])
        else:
            print(f"{bad_wires[i]},", end="")
    pass


if __name__ == "__main__":
    # part1()
    part2()