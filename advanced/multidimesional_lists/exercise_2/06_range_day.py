'''
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
•	Your position is marked with the symbol "A"
•	Targets marked with the symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
When you have shot a target, the field becomes an empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
•	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
              	       "Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
'''
def moves(row, col, to_wher, how_much=1):
    new_row, new_col = row + directions[to_wher][0] * how_much, col + directions[to_wher][1] * how_much
    if not (0 <= new_row < size and 0 <= new_col < size):
        return row, col
    if matrix[new_row][new_col] == "x":
        return row, col

    return new_row, new_col

def shoot(row, col, to_wher):
    new_row, new_col = row + directions[to_wher][0], col + directions[to_wher][1]
    while (0 <= new_row < size and 0 <= new_col < size):
        if matrix[new_row][new_col] == "x":
            matrix[new_row][new_col] == "."
            return new_row, new_col
        else:
            new_row += directions[to_wher][0]
            new_col += directions[to_wher][1]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = 5
matrix = []
my_row = 0
my_col = 0
targets_pos = []
total_targets = 0

for i in range(size):
    line = input().split()
    matrix.append(line)
    if "A" in line:
        my_row, my_col = i, line.index("A")
    if "x" in line:
        total_targets += line.count("x")
init_targets = total_targets

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        distance = int(command[2])
        next_row, next_col = moves(my_row, my_col, direction, distance)

    elif action == "shoot":
        if shoot(my_row, my_col, direction):
            next_row, next_col = shoot(my_row, my_col, direction)
            total_targets -= 1
            targets_pos.append([next_row, next_col])
            if total_targets == 0:
                print(f'Training completed! All {init_targets} targets hit.')

if total_targets > 0:
    print(f'Training not completed! {total_targets} targets left.')

for t in targets_pos:
    print(t)




