'''
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down".
In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
•	* - a regular position on the field
•	e - the end of the route
•	c - coal
•	s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction.
If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal.
In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
•	If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
•	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
•	If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
•	Field size - an integer number
•	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
•	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
'''
size = int(input())
comands = input().split()
matrix = []
coal = 0

for i in range(size):
    income = input().split()
    coal += income.count('c')
    if 's' in income:
        start = [i, income.index('s')]
    matrix.append(income)

matrix[start[0]][start[1]] = '*'    #заменямае s със * за да не зацикли някога
def valid_indices(action: str, indices: list):
    curr_row = indices[0]
    curr_col = indices[1]
    if action == 'up' and curr_row - 1 >= 0:
        curr_row -= 1
    elif action == 'down' and curr_row + 1 < size:
        curr_row += 1
    elif action == 'left' and curr_col - 1 >= 0:
        curr_col -= 1
    elif action == 'right' and curr_col + 1 < size:
        curr_col += 1
    return [curr_row, curr_col]

curr_cordinates = start
for _ in range(len(comands)):
    for cur_command in comands:
        if curr_cordinates != valid_indices(cur_command, curr_cordinates):
            curr_cordinates = valid_indices(cur_command, curr_cordinates)
            if matrix[curr_cordinates[0]][curr_cordinates[1]] == "e":
                print(f"Game over! ({curr_cordinates[0]}, {curr_cordinates[1]})")
                exit()
            elif matrix[curr_cordinates[0]][curr_cordinates[1]] == "c":
                coal -= 1
                matrix[curr_cordinates[0]][curr_cordinates[1]] = '*'
                if coal == 0:
                    print(f"You collected all coal! ({curr_cordinates[0]}, {curr_cordinates[1]})")
                    exit()

else:
    print(f"{coal} pieces of coal left. ({curr_cordinates[0]}, {curr_cordinates[1]})")

