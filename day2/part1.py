from typing import List

def is_safe(line: List[int]) -> bool:

    direction = ""
    for i in range(1, len(line)):

        if abs(line[i] - line[i-1]) > 3:
            return False

        if abs(line[i] - line[i-1]) < 1:
            return False

        if line[i] > line[i-1]:
            if direction == "down":
                return False
            direction = "up"

        if line[i] < line[i-1]:
            if direction == "up":
                return False
            direction = "down"

    return True

def main():
    with open("input1.txt", "r") as f:
        lines = []
        for line in f:
            lines.append([int(n) for n in line.split()])

    safe = 0
    for line in lines:
        print(is_safe(line), line)
        if is_safe(line):
            safe += 1

    print(safe)

if __name__ == "__main__":
    main()