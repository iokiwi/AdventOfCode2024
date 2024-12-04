from typing import Tuple

# Path to the file you want to search
file_path = 'input.txt'

# Open the file and read its contents
with open(file_path, 'r') as file:
    file_contents = [list(line.strip()) for line in file.readlines()]


def search(file_contents, position: Tuple[int], direction: Tuple[int]):

    letters = ""
    x_lim = len(file_contents[0])
    y_lim = len(file_contents)

    x, y = position
    dx, dy = direction

    count = 0
    while x in range(0, x_lim) and y in range(0, y_lim) and count < 4:
        letters += file_contents[y][x]
        x += dx
        y += dy
        count += 1

    return letters


total = 0
for y, row in enumerate(file_contents):
    for x, col in enumerate(row):
        if col == "X":

            directions = (
                (0, -1), # UP
                (0, 1), # DOWN
                (-1, 0), # LEFT
                (1, 0), # RIGHT
                (1, 1), # RIGHT, DOWN
                (-1, 1), # DOWN, LEFT
                (1, -1), # RIGHT, UP
                (-1, -1), # LEFT, UP
            )

            for direction in directions:
                result = search(file_contents, (x, y), direction)
                if "XMAS" in result:
                    print(result)
                    total += 1

print(total)