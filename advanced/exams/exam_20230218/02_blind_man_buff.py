"""
You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive the rows of the playground, with M columns.
You will be marked with the letter 'B', and placed in a random position. In random positions, furniture or other obstacles will be marked with the letter 'O'.
The other players (opponents) will be marked with the letter 'P'. There will always be three other players participating in the game. All of the empty positions will be marked with '-'.
Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an obstacle.
On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing which direction you need to move.
The possible directions are "up", " down", "right", and "left". If the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move).
If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.
You need to keep track of the count of touched opponents and the moves you’ve made.
In case you step on a position marked with '-', increase the count of the moves made.
When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents and moves made), and this is your new position.
The game is over when you manage to touch all other opponents or the given command is "Finish". A game report is printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
Input
•	On the first line, you'll receive the dimensions of the playground in the format: "N M", where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
•	On the next N lines, you will receive a string representing the respective row of the playground. The positions in every string will be separated by a single space (" ").
•	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).
 
Output
•	When the game is over, the following output should be printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
"""
def valid_position(direction, *position):
    row, col = position
    next_row, next_col = row + directions[direction][0], col + directions[direction][1]
    if 0 <= next_row < rows and 0 <= next_col < cols:
        if house[next_row][next_col] == "O":
            return [row, col]
        else:
            return [next_row, next_col]
    else:
        return [row, col]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

house = []
curr_row, curr_col = [0, 0]
caught = 0
moves = 0

rows, cols = [int(x) for x in input().split()]
for cr in range(rows):
    line = input().split()
    house.append(line)
    if "B" in line:
        curr_row, curr_col = [cr, line.index("B")]

while True:
    command = input()
    if command == "Finish":
        break

    new_row, new_col = valid_position(command, curr_row, curr_col)
    if new_row != curr_row or new_col != curr_col:
        if house[new_row][new_col] == "P":
            caught += 1
            moves += 1
            if caught == 3:
                break
        elif house[new_row][new_col] == "-":
            moves += 1

    house[curr_row][curr_col] = "-"
    curr_row, curr_col = new_row, new_col

print(f"Game over!\nTouched opponents: {caught} Moves made: {moves}")