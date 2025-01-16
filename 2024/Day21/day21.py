import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    # Create helpful structures
    numpad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A']
    ]

    dirpad = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]

    optimal_sequences = dict()

    def getShortestSequence(sequence, level):
        # Get the directions on the numeric keypad
        sequence = processNumPad(sequence)
        level -= 1

        # Keep getting the optimal sequence for the direction keypads
        while level > 0:
            sequence = processDirPad(sequence)
            level -= 1
        return sequence


    def getPosition(key, keypad):
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                if keypad[i][j] == key:
                    return (i, j)
    
    
    def processNumPad(sequence):
        next_sequence = []
        current = 'A'
        for next in sequence:
            # Check if current -> next optimal sequence exists
            if (current, next) in optimal_sequences:
                next_sequence.append(optimal_sequences[(current, next)])
            else:
                # Determine the optimal sequence to go from current -> next
                iCurr, jCurr = getPosition(current, numpad)
                iNext, jNext = getPosition(next, numpad)

                # Determine movements
                vert = iCurr - iNext
                hori = jNext - jCurr
                if vert > 0:
                    vert_movement = "^"*vert
                elif vert < 0:
                    vert_movement = "v"*(vert*-1)
                else:
                    vert_movement = ""
                
                if hori > 0:
                    hori_movement = ">"*hori
                elif hori < 0:
                    hori_movement = "<"*(hori*-1)
                else:
                    hori_movement = ""

                if (iCurr == 3 and jNext == 0) or (hori > 0 and jCurr >= 1):
                    movement = vert_movement + hori_movement + "A"
                else:
                    movement = hori_movement + vert_movement + "A"
                    
                # Save result in dictionary
                optimal_sequences[(current, next)] = movement
                next_sequence.append(movement)
                
            # Change current
            current = next

        # Return final sequence
        sequence = "".join(next_sequence)
        return sequence


    def processDirPad(sequence):
        next_sequence = []
        current = 'A'
        for next in sequence:
            # Check if current -> next optimal sequence exists
            if (current, next) in optimal_sequences:
                next_sequence.append(optimal_sequences[(current, next)])
            else:
                # Determine the optimal sequence to go from current -> next
                iCurr, jCurr = getPosition(current, dirpad)
                iNext, jNext = getPosition(next, dirpad)

                # Determine movements
                vert = iCurr - iNext
                hori = jNext - jCurr
                if vert > 0:
                    vert_movement = "^"*vert
                elif vert < 0:
                    vert_movement = "v"*(vert*-1)
                else:
                    vert_movement = ""
                
                if hori > 0:
                    hori_movement = ">"*hori
                elif hori < 0:
                    hori_movement = "<"*(hori*-1)
                else:
                    hori_movement = ""

                if (iCurr == 0 and jNext == 0) or (hori > 0 and jCurr >= 1):
                    movement = vert_movement + hori_movement + "A"
                else:
                    movement = hori_movement + vert_movement + "A"

                # Save result in dictionary
                optimal_sequences[(current, next)] = movement
                next_sequence.append(movement)
                
            # Change current
            current = next

        # Return final sequence
        sequence = "".join(next_sequence)
        return sequence


    # Compute complexity of each code
    total = 0
    for line in lines:
        sequence = getShortestSequence(line, int(sys.argv[2]))
        complexity = int(line[0:3])*len(sequence)
        print(f"{len(sequence)} x {int(line[0:3])} = {complexity}")
        total += complexity

    print(total)
    print()
    pass



def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    # Create helpful structures
    numpad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A']
    ]

    dirpad = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]

    optimal_sequences = dict()
    number_of_steps = dict()

    def getShortestSequence(sequence, level):
        # Get the directions on the numeric keypad
        sequence = processNumPad(sequence)
        level -= 1

        # Keep getting the optimal length sequence for the direction keypads
        total = 0
        current = 'A'
        for next in sequence:
            total += process(current, next, level)
            current = next
        return total


    def getPosition(key, keypad):
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                if keypad[i][j] == key:
                    return (i, j)
    
    
    def processNumPad(sequence):
        next_sequence = []
        current = 'A'
        for next in sequence:
            # Check if current -> next optimal sequence exists
            if (current, next) in optimal_sequences:
                next_sequence.append(optimal_sequences[(current, next)])
            else:
                # Determine the optimal sequence to go from current -> next
                iCurr, jCurr = getPosition(current, numpad)
                iNext, jNext = getPosition(next, numpad)

                # Determine movements
                vert = iCurr - iNext
                hori = jNext - jCurr
                if vert > 0:
                    vert_movement = "^"*vert
                elif vert < 0:
                    vert_movement = "v"*(vert*-1)
                else:
                    vert_movement = ""
                
                if hori > 0:
                    hori_movement = ">"*hori
                elif hori < 0:
                    hori_movement = "<"*(hori*-1)
                else:
                    hori_movement = ""

                if (iCurr == 3 and jNext == 0) or (hori > 0 and jCurr >= 1):
                    movement = vert_movement + hori_movement + "A"
                else:
                    movement = hori_movement + vert_movement + "A"
                    
                # Save result in dictionary
                optimal_sequences[(current, next)] = movement
                next_sequence.append(movement)
                
            # Change current
            current = next

        # Return final sequence
        sequence = "".join(next_sequence)
        return sequence


    def process(current, next, remainingRobots):
        if remainingRobots == 0:
            return 1
        
        if (current, next, remainingRobots) not in number_of_steps:
            # This has not been computed before
            if (current, next) not in optimal_sequences:
                # Determine the optimal sequence to go from current -> next
                iCurr, jCurr = getPosition(current, dirpad)
                iNext, jNext = getPosition(next, dirpad)

                # Determine movements
                vert = iCurr - iNext
                hori = jNext - jCurr
                if vert > 0:
                    vert_movement = "^"*vert
                elif vert < 0:
                    vert_movement = "v"*(vert*-1)
                else:
                    vert_movement = ""
                
                if hori > 0:
                    hori_movement = ">"*hori
                elif hori < 0:
                    hori_movement = "<"*(hori*-1)
                else:
                    hori_movement = ""

                if (iCurr == 0 and jNext == 0) or (hori > 0 and jCurr >= 1):
                    movement = vert_movement + hori_movement + "A"
                else:
                    movement = hori_movement + vert_movement + "A"

                # Save result in dictionary
                optimal_sequences[(current, next)] = movement
            
            sequence = optimal_sequences[(current, next)]
            total = 0
            newCurrent = 'A'
            for newNext in sequence:
                total += process(newCurrent, newNext, remainingRobots-1)
                newCurrent = newNext

            number_of_steps[(current, next, remainingRobots)] = total

        return number_of_steps[(current, next, remainingRobots)]
    

    # Compute complexity of each code
    total = 0
    for line in lines:
        length = getShortestSequence(line, int(sys.argv[2]))
        complexity = int(line[0:3])*length
        print(f"{length} x {int(line[0:3])} = {complexity}")
        total += complexity

    print(total)
    print()
    pass


if __name__ == "__main__":
    # part1()
    part2()