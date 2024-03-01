"""
The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
You get as input the size of the field, which will be always a square shape.
After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up" in a sequence, each value separated by a comma and a space (", ").
On the next rows, you will receive the field.
Possible characters in the field:
•	s - represents the squirrel's position.
•	h – represents a hazelnut.
•	* – the asterisk represents an empty position.
•	t – represents a trap.
The squirrel starts from the s - position.
•	If the squirrel steps on a hazelnut, you have to increase them by 1. The position should be marked with an asterisk (*).
o	If the squirrel collects all 3 hazelnuts, the game ends.
•	Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
•	If it steps on a trap, the game ends.
•	If the squirrel moves out of the field, the game ends.
After all commands you will have 4 possible results:
•	You win if the squirrel collects 3 of the hazelnuts.
•	The squirrel collects less than 3 hazelnuts.
•	The squirrel steps on a trap.
•	The squirrel moves out of the field.
Input
•	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
•	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
•	In the next N lines, you will receive the values for every row.
Output
•	On the first line:
o	If the squirrel goes out of the field - "The squirrel is out of the field.".
o	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
o	If the squirrel hasn’t collected all hazelnuts - "There are more hazelnuts to collect.".
o	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
•	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
"""
from collections import deque


def valid_position(position, direction):
    row, col = position
    next_row, next_col = row + directions[direction][0], col + directions[direction][1]
    if 0 <= next_row < size and 0 <= next_col < size:
        return [next_row, next_col]


size = int(input())
action = input().split(", ")
field = []
squirrel = []
hazelnuts = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for rf in range(size):
    line = [s for s in input()]
    field.append(line)
    if "s" in line:
        squirrel = [rf, line.index("s")]

field[squirrel[0]][squirrel[1]] = '*'
curr_position = squirrel

for to_where in action:

    if not valid_position(curr_position, to_where):
        print("The squirrel is out of the field.")
        break
    else:
        new_row, new_col = valid_position(curr_position, to_where)
        if field[new_row][new_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        elif field[new_row][new_col] == "h":
            hazelnuts += 1
            if hazelnuts >= 3:
                print("Good job! You have collected all hazelnuts!")
                break
        field[curr_position[0]][curr_position[1]] = '*'
        curr_position = [new_row, new_col]
else:
     print("There are more hazelnuts to collect.")


print(f"Hazelnuts collected: {hazelnuts}")