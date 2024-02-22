"""
You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented as some symbols separated by a single space:
•	Your position is marked with the symbol "Y"
•	Christmas decorations are marked with the symbol "D"
•	Gifts are marked with the symbol "G"
•	Cookies are marked with the symbol "C"
•	All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". The commands will be in the format "right/left/up/down-{steps}".
You should move in the given direction with the given steps and collect all the items that come across.
If you go out of the field, you should continue to traverse the field from the opposite side in the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry Christmas!".
Input
•	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
•	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
•	On the following lines, you will receive commands in the format described above until you receive the command "End" or until you collect all items.
Output
•	On the first line, if you have collected all items, print:
o	"Merry Christmas!"
o	Otherwise, skip the line
•	Next, print the number of collected items in the format:
o	"You've collected:
o	- {number_of_decoration} Christmas decorations
o	- {number_of_gifts} Gifts
o	- {number_of_cookies} Cookies"
•	Finally, print the field, as shown in the examples.
"""


def next_position(row, col, to_where):
    new_row, new_col = row + directions[to_where][0], col + directions[to_where][1]

    if new_row < 0:
        new_row = rows - 1
    if new_row >= rows:
        new_row = 0
    if new_col < 0:
        new_col = cols - 1
    if new_col >= cols:
        new_col = 0

    return [new_row, new_col]


rows, cols = [int(x) for x in input().split(', ')]

items = {
    "D": 0,
    "G": 0,
    "C": 0
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix = []
all_items = 0
curr_row, curr_col = 0, 0
for row in range(rows):
    row_data = input().split()
    matrix.append(row_data)
    for i in ["D", "G", "C"]:
        if i in row_data:
            all_items += row_data.count(i)
    if "Y" in row_data:
        curr_row, curr_col = row, row_data.index("Y")


direction, steps = '', 0
while True:

    if all_items == 0:
        break

    command = input()

    if command == "End":
        break

    direction, s = command.split('-')
    steps = int(s)

    for n in range(1, steps + 1):
        matrix[curr_row][curr_col] = "x"
        next_row, next_col = next_position(curr_row, curr_col, direction)
        symbol = matrix[next_row][next_col]

        if symbol in items:
            items[symbol] += 1
            all_items -= 1

        curr_row, curr_col = next_row, next_col
        matrix[curr_row][curr_col] = "Y"

        if all_items == 0:
            break

if all_items == 0:
    print("Merry Christmas!")

print("You've collected:")

for k, v in items.items():  # sorted(items.items(), key= lambda item: -item[1]):
    if k == "D":
        k = "Christmas decorations"
    elif k == "G":
        k = "Gifts"
    elif k == "C":
        k = "Cookies"
    print(f"- {v} {k}")

[print(*j, sep=' ') for j in matrix]
