import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    list1 = []
    list2 = []
    for line in lines:
        numbers_str = line.strip().split("   ")
        list1.append(int(numbers_str[0]))
        list2.append(int(numbers_str[1]))

    list1.sort()
    list2.sort()
    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    print(total)


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    list1 = []
    list2 = []
    for line in lines:
        numbers_str = line.strip().split("   ")
        list1.append(int(numbers_str[0]))
        list2.append(int(numbers_str[1]))

    score = 0
    for i in range(len(list1)):
        number = list1[i]
        count = 0
        for num in list2:
            if num == number:
                count += 1
        score += number*count
        
    print(score)


if __name__ == "__main__":
    part1()
    part2()