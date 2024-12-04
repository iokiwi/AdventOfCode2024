import re

# Define the pattern to search for
pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

# Path to the file you want to search
file_path = 'input.txt'

# Open the file and read its contents
with open(file_path, 'r') as file:
    file_contents = file.read()

# Perform a global search (find all matches) in the file contents
matches = re.findall(pattern, file_contents)

# Check if any matches were found
if matches:
    print("Found matches:")
    total = 0
    for match in matches:
        print(match)
        f = [int(x) for x in match[4:-1].split(",")]
        subtotal = f[0] * f[1]
        print(f"{f[0]} * {f[1]} = {subtotal}")
        print(f"{total} + {subtotal} = {total+subtotal}")
        total += subtotal
    print(total)
else:
    print("No matches found.")