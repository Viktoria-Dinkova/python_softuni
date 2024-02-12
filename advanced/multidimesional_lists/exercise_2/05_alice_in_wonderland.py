'''
You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A".
•	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps into the rabbit hole or goes out of the territory,
 she can't return, and the program ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
•	On the first line, you will be given the integer n – the size of the square matrix
•	On the following n lines - matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will be given a move command
Output
•	On the first line:
o	If Alice steps into the rabbit hole or goes out of the territory, print:
"Alice didn't make it to the tea party."
o	If she collected at least 10 bags of tea, print:
"She did it! She went to the party."
•	On the following lines, print the matrix.
'''
def moves(row, col, to_where):
    new_row, new_col = row + directions[to_where][0], col + directions[to_where][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        return new_row, new_col

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
wonderland = []
alice_row, alice_col = 0, 0
tea = 0

for i in range(size):
    line = input().split()
    wonderland.append(line)
    if "A" in line:
        alice_row, alice_col = i, line.index("A")

while tea < 10:
    cell_value = wonderland[alice_row][alice_col]
    wonderland[alice_row][alice_col] = '*'

    if cell_value == "R":
        print("Alice didn't make it to the tea party.")
        break

    if cell_value not in [".", "*", "A"]:
        tea += int(cell_value)
        if tea >= 10:
            break

    direction = input()

    if moves(alice_row, alice_col, direction):
        alice_row, alice_col = moves(alice_row, alice_col, direction)
    else:
        print("Alice didn't make it to the tea party.")
        break


if tea >= 10:
    print("She did it! She went to the party.")

[print(*w) for w in wonderland]
