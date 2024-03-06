'''You will be given an integer n for the size of the fishing area with a square shape. On the next n lines, you will receive the rows of the fishing area.
You will be placed in a random position, marked with the letter 'S'. There will be fishing passages on random positions, marked with a single digit.
There will be whirlpools marked with 'W'. All of the empty positions will be marked with '-'.
Each turn until the "collect the nets" command is received you will be given commands for your movement. Move commands will be: "up", "down", "left", and "right".
•	If you move to a fish passage, you collect the amount equal to the digit there, the passage disappears and should be replaced by '-'.
•	If you fall into a whirlpool – the ship sinks and loses its catch, the program ends.
•	If you leave the fishing area (go out of the boundaries of the matrix) depending on the move command you will be moved to the opposite side of the one you were on.
/Example: In a 3x3 matrix you are at position [1,2] and receive the command "right" you will be moved to position [1,0]./
 You need at least 20 tons of fish to be considered a successful season. Keep in mind that even if the quota is reached the ship continues to move.
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a move command.
Output
•	On the first line:
	If the ship falls into a whirlpool, print only this message and stop the program:
o	"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [n,n]"
	If the ship reaches the quota:
o	"Success! You managed to reach the quota!"
	If the ship did not reach the quota:
o	"You didn't catch enough fish and didn't reach the quota!
You need {lack of fish} tons of fish more."
•	On the next lines.
	If the catch quantity is bigger than zero, print:
o	"Amount of fish caught: {quantity} tons."
else: do not print anything.
	If you didn't get into a whirlpool, print the matrix.
'''

def valid_position(position, to_where):
    row, col = position[0], position[1]
    next_row, next_col = row + directions[to_where][0], col + directions[to_where][1]

    if next_row < 0:
        next_row = size-1
    elif next_row >= size:
        next_row = 0

    if next_col < 0:
        next_col = size-1
    elif next_col >= size:
        next_col = 0

    return [next_row, next_col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
fishing_area = []
ship_position = []

quota = 0
is_waved = False

for r in range(size):
    c_r = [x for x in input()]
    if "S" in c_r:
        ship_position = [r, c_r.index("S")]
    fishing_area.append(c_r)

fishing_area[ship_position[0]][ship_position[1]] = '-'

while True:
    direction = input()
    if direction == "collect the nets":
        break

    new_position = valid_position(ship_position, direction)
    new_row, new_col = new_position[0], new_position[1]
    if fishing_area[new_row][new_col] == "W":
        is_waved = True
        quota = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]")
        break

    elif fishing_area[new_row][new_col] == "-":
        ship_position = new_position
        continue

    else:
        quota += int(fishing_area[new_row][new_col])
        fishing_area[new_row][new_col] = '-'
        ship_position = new_position

fishing_area[ship_position[0]][ship_position[1]] = "S"

if not is_waved:
    if quota >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quota} tons of fish more.")

    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")


    [print(*row, sep='') for row in fishing_area]
