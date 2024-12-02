from typing import List

# def _recurse(line, i):
#     opt_2 = line[:i-1] + line[i:]
#     print(f"Trying without line[{i-1}]({line[i-1]}): {opt_2}")
#     r2 = is_safe(opt_2, depth=1)
#     opt_1 = line[:i] + line[i+1:]
#     print(f"Trying without line[{i}]({line[i]}): {opt_1}")
#     r1 = is_safe(opt_1, depth=1)
#     return r2 or r1

def remove_one(line):
    for i in range(len(line)):
        if is_safe(line[:i] + line[i+1:]):
            return (i, True)
    return 0, False

def is_safe(line: List[int], depth=0) -> bool:
    direction = ""

    for i in range(1, len(line)):
        diff = abs(line[i] - line[i-1])
        if diff > 3 or diff < 1:
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
        result = is_safe(line)
        if result:
            safe += 1
            print(f"{str(line):<50} Safe without removing any level")
        else:
            i, result_2 = remove_one(line)
            if result_2:
                print(f"{str(line):<50} Safe by removing {i}, {line[i]}")
                safe += 1
            else:
                print(f"{str(line):<50} Unsafe regardless of which level is removed.")
        print(safe)

    print(safe)

if __name__ == "__main__":
    main()