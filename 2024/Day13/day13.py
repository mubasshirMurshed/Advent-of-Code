import sys
import re

class Machine:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx + 10000000000000
        self.Cy = Cy + 10000000000000

    def __repr__(self):
        return f"\n[Button A: {self.Ax}, {self.Ay}\nButton B: {self.Bx}, {self.By}\nPrize: {self.Cx}, {self.Cy}]\n"
    
    def min_tokens(self):
        # Determine if impossible (bug that infinite solutions can still count)
        det = self.Ax*self.By - self.Bx*self.Ay
        if det == 0:
            return 0
        
        # Get the number of A and B presses
        A = (self.By*self.Cx - self.Bx*self.Cy)/det
        B = (-self.Ay*self.Cx + self.Ax*self.Cy)/det

        # Decline non-integer presses
        if A % 1 != 0 and B % 1 != 0:
            return 0

        A = int(A)
        B = int(B)

        # Return number of tokens
        return 3*A + B

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.read()
    
    machines_string = lines.split("\n\n")
    machines = []
    for machine in machines_string:
        instructions = machine.split('\n')
        
        # Parse Button A
        Ax, Ay = list(map(int, re.findall('\d+', instructions[0])))

        # Parse Button B
        Bx, By = list(map(int, re.findall('\d+', instructions[1])))

        # Parse Prize
        Cx, Cy = list(map(int, re.findall('\d+', instructions[2])))

        # Add machine to list
        machines.append(Machine(Ax, Ay, Bx, By, Cx, Cy))

    # For each machine find the minimum number of tokens required
    min_tokens = 0
    for machine in machines:
        min_tokens += machine.min_tokens()

    print(min_tokens)
    pass




def part2() -> None:
    
    pass


if __name__ == "__main__":
    part1()
    part2()