import sys

def part1() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    safe_count = 0
    for report_str in lines:
        report = report_str.strip().split(" ")
        report = [int(level) for level in report]
        safe = True
        for i in range(1, len(report)):
            current_level = report[i]
            prev_level = report[i-1]

            if current_level == prev_level:
                safe = False
                break

            if i == 1:
                if current_level > prev_level:
                    change = 1
                elif current_level < prev_level:
                    change = -1
            
            if current_level > prev_level and change == -1:
                safe = False
                break

            if current_level < prev_level and change == 1:
                safe = False
                break

            if abs(current_level - prev_level) > 3:
                safe = False
                break
        
        if safe:
            safe_count += 1

    print(safe_count)
    pass


def part2() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    safe_count = 0
    for report_str in lines:
        report = report_str.strip().split(" ")
        report = [int(level) for level in report]

        # Determine if report is safe or not safe
        safe = True
        bad_count = 0
        i = 1
        j = 0
        prev_change = report[i] - report[j]
        while i < len(report):
            change = report[i] - report[j]

            if change*prev_change <= 0:
                bad_count += 1
                if i == 1:
                    change = report[2] - report[1]
                    prev_change = change
                else:
                    change = report[i] - report[j-1]
                if change*prev_change <= 0 or abs(change) > 3 or bad_count == 2:
                    safe = False
                    break

            elif abs(change) > 3:
                bad_count += 1
                if i == 1:
                    change = report[2] - report[1]
                    prev_change = change
                else:
                    i += 1
                    if i == len(report):
                        break
                    change = report[i] - report[j]
                    j += 1
                if change*prev_change <= 0 or abs(change) > 3 or bad_count == 2:
                    safe = False
                    break

            prev_change = change

            i += 1
            j += 1
        
        if safe:
            # print(report, end=" ")
            # print("is safe")

            safe_count += 1

    print(safe_count)
    pass


def part2_brute_force() -> None:
    # Read input file
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    safe_count = 0
    for report_str in lines:
        report = report_str.strip().split(" ")
        report = [int(level) for level in report]

        # Determine if report is safe or not safe
        safe = False
        if isSafe(report):
            safe = True
        else:
            for i in range(len(report)):
                # Construct report without the level, report[i]
                new_report = [report[j] for j in range(len(report)) if j != i]
                if isSafe(new_report):
                    safe = True
                    break

        if safe:
            safe_count += 1

    print(safe_count)
    pass


def isSafe(report):
    safe = True
    for i in range(1, len(report)):
        current_level = report[i]
        prev_level = report[i-1]

        if current_level == prev_level:
            safe = False
            break

        if i == 1:
            if current_level > prev_level:
                change = 1
            elif current_level < prev_level:
                change = -1
        
        if current_level > prev_level and change == -1:
            safe = False
            break

        if current_level < prev_level and change == 1:
            safe = False
            break

        if abs(current_level - prev_level) > 3:
            safe = False
            break
    return safe

if __name__ == "__main__":
    part1()
    part2_brute_force()