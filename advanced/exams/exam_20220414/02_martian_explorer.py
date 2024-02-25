"""
You will receive a 6x6 field on separate lines with:
•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
•	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
•	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in the same direction. Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
Stop the program if you run out of commands or the rover gets broken.
Input
•	On the first 6 lines, you will receive the matrix.
•	On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
•	For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete} deposit found at ({data}, {col})"
•	If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({data}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
•	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
•	Otherwise, print on the console: "Area not suitable to start the colony."
See examples for more clarification.
"""


def next_position(row, col, to_where):
    new_row, new_col = row + directions[to_where][0], col + directions[to_where][1]

    if new_row < 0:
        new_row = size - 1
    if new_row >= size:
        new_row = 0
    if new_col < 0:
        new_col = size - 1
    if new_col >= size:
        new_col = 0

    return [new_row, new_col]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

deposit = {
    "W": 'Water',
    "M": 'Metal',
    "C": 'Concrete'
}

size = 6
mars = []


for s in range(size):
    data = input().split()
    mars.append(data)

    if "E" in data:
        rover = [s, data.index("E")]

curr_row, curr_col = rover
mars[curr_row][curr_col] = "-"
commands = input().split(', ')

find_deposit = set()

for command in commands:
    next_row, next_col = next_position(curr_row, curr_col, command)

    if mars[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    elif mars[next_row][next_col] == "-":
        curr_row, curr_col = next_row, next_col
        continue

    else:
        find_deposit.add(deposit[mars[next_row][next_col]])
        print(f"{deposit[mars[next_row][next_col]]} deposit found at ({next_row}, {next_col})")

    curr_row, curr_col = next_row, next_col


if len(find_deposit) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
