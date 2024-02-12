'''
On the first line, you will be given a number representing the size of the field. In the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right.
 If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction.
 The bunny can move within the field and cannot go outside its boundaries. Do not consider negative indices as valid ones. For more clarifications, see the examples below.
Note: In some directions, the collected eggs can happen to be zero or a negative number.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
'''
def valid_cell(row, col):
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        return new_row, new_col

size = int(input())
eastern_field = []
max_path = []
maximum_eggs = float('-inf')
max_direction = ''

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(size):
    line = input().split()
    eastern_field.append(line)
    if "B" in line:
        beginning = [i, line.index("B")]


for direction in directions:
    row, col = beginning
    total_eggs = 0
    path = []

    while valid_cell(row, col):
        row, col = valid_cell(row, col)
        cell = eastern_field[row][col]
        if cell == "X":
            break
        else:
            total_eggs += int(cell)
            path.append([row, col])

    if total_eggs >= maximum_eggs:
        maximum_eggs = total_eggs
        max_path = path
        max_direction = direction

print(max_direction)
[print(pos) for pos in max_path]
print(maximum_eggs)