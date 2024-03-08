"""
The jetfighter will start at a random position, marked with the letter 'J'. In random positions also, enemy aircraft will be marked with the letter 'E'. There will also be repair points marked with the letter 'R'. All of the empty positions will be marked with the symbol'-'.
The jetfighter has an initial armor value of 300 units. When it receives a command, it moves one position towards the given direction.
The program will end when аll enemy planes are shot down or the jetfighter’s armor becomes 0. The final state of the airspace must always be printed on the console at the end.
On each turn, you will be guiding the jetfighter and giving it the direction, to move towards. The commands will be "up", "down", "left" and "right".
	If a position with '-' (dash) is reached, it means that the field is empty and the jetfighter awaits its next direction.
	If it encounters an enemy aircraft marked with 'E', a battle begins:
	The jetfighter shoots down the enemy plane (the position of the destroyed enemy plane will be marked with '-' (dash)
	In case this is the last enemy, the program ends and the following message should be displayed on the console: "Mission accomplished, you neutralized the aerial threat!"
o	Do not forget the final state of the airspace.
	In case this is not the last enemy, the jetfighter takes damage – its armor loses 100 units.
o	If its armor reaches zero, it crashes and the mission fails. The program ends and the following message should be displayed on the console: "Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!"
o	Do not forget the final state of the airspace.
	If a position marked with 'R' is reached your plane is repaired and restores its armor to 300 units.
o	The position must be marked with '-' (dash).
Input
•	On the first line, you are given the integer n – the size of the matrix (airspace).
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a direction command.
Output
•	If all enemy planes are shot down, print:
o	"Mission accomplished, you neutralized the aerial threat!"
•	If your jetfighter is hit by an enemy plane three times, print:
o	"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!".
•	At the end, print the final state of the matrix (airspace) with the last known position of your jetfighter on it.
"""


def next_position(curr_row, curr_col, to_where):
    new_row, new_col = curr_row + directions[to_where][0], curr_col + directions[to_where][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        return [new_row, new_col]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
armor = 300

airspace = []
enemy = 0

for d in range(size):
    data = list(input())
    airspace.append(data)
    if "E" in data:
        enemy += data.count("E")
    if "J" in data:
        row, col = d, data.index("J")

airspace[row][col] = "-"

while True:
    direction = input()
    next_row, next_col = next_position(row, col, direction)

    if airspace[next_row][next_col] == "E":
        enemy -= 1
        airspace[next_row][next_col] = "-"

        if enemy == 0:
            airspace[next_row][next_col] = "J"
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            if armor == 0:
                airspace[next_row][next_col] = "J"
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break

    elif airspace[next_row][next_col] == "R":
        armor = 300
        airspace[next_row][next_col] = "-"

    airspace[row][col] = "-"
    row, col = next_row, next_col

[print(*a, sep='') for a in airspace]