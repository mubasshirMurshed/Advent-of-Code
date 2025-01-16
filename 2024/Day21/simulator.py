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


sequence = "<vA<AA>>^AvA<^A>AAvA^A<vA<AA>>^AvAA<^A>Av<<A>A^>AAvA^A<A>A<vA^>A<A>A"

for _ in range(2):
    pos = [0, 2]
    new_sequence = ""
    for next_dir in sequence:
        if next_dir == "<":
            pos[1] -= 1
        elif next_dir == ">":
            pos[1] += 1
        elif next_dir == "^":
            pos[0] -= 1
        elif next_dir == "v":
            pos[0] += 1
        else:
            new_sequence += dirpad[pos[0]][pos[1]]
        if pos[0] == 0 and pos[1] == 0:
            print("ERROR")
            break
    sequence = new_sequence

pos = [3, 2]
new_sequence = ""
for next_dir in sequence:
    if next_dir == "<":
        pos[1] -= 1
    elif next_dir == ">":
        pos[1] += 1
    elif next_dir == "^":
        pos[0] -= 1
    elif next_dir == "v":
        pos[0] += 1
    else:
        new_sequence += numpad[pos[0]][pos[1]]

    if pos[0] == 3 and pos[1] == 0:
            print("ERROR")
            break

print(new_sequence)