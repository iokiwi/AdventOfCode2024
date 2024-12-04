from typing import Tuple

# Path to the file you want to search
file_path = 'input.txt'

# Open the file and read its contents
with open(file_path, 'r') as file:
    file_contents = [list(line.strip()) for line in file.readlines()]

def get_adjacent(file_contents, position, direction):

    x = position[0] + direction[0]
    y = position[1] + direction[1]

    x_lim = len(file_contents[0])
    y_lim = len(file_contents)

    if x not in range(0, x_lim) or y not in range(0, y_lim):
        return ""

    return file_contents[y][x]

def check_diagonals(file_contents, position, pair):
    adjacent = (
        get_adjacent(file_contents, position, pair[0]),
        get_adjacent(file_contents, position, pair[1]),
    )
    if "S" in adjacent and "M" in adjacent:
        return True
    return False

total = 0
for y, row in enumerate(file_contents):
    for x, col in enumerate(row):
        if col == "A":
            directions = (
                ((-1, -1), (1, 1)),
                ((-1, 1), (1, -1)),
            )

            position = (x,y)

            is_xmas = True
            for pair in directions:
                if not check_diagonals(file_contents, position, pair):
                    is_xmas = False

            if is_xmas:
                total += 1

print(total)