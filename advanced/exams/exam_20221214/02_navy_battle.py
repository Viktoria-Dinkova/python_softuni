"""You will be given an integer n for the size of the battlefield (square shape). On the next n lines, you will receive the rows of the battlefield.
The submarine will start at a random position, marked with the letter 'S'. The submarine surveys the surrounding area through its periscope,
so it has to climb up to periscope depth, where it might run across naval mines.
When the submarine receives direction, it goes deep and moves one position toward the given direction.
On each turn, you will be guiding the submarine and giving it the direction, in which it should move. The commands will be "up", "down", "left" and "right".
When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
•	If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
•	    If it runs across a naval mine ('*'), the submarine takes serious damage.
        When a mine is blown, the position of the mine will be marked with '-' (dash).
        U-9 can withstand two hits from naval mines.  The third time the submarine is hit by a mine, it disappears and the mission is failed.
        The battle is over and the following message should be printed on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row_num}, {col}]!"
•	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be marked with '-' (dash).
•	If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should be printed on the Console:
        "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).
Input
•	On the first line, you are given the integer n – the size of the matrix (wall).
•	The next n lines hold the values for every row_num (NOT separated by anything).
•	On each of the next lines you will get a direction command.
Output
•	If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
•	If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! Last known coordinates [{row_num}, {col}]!".
•	At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.
"""


def valid_position(row, col, to_where):
    new_row, new_col = row + directions[to_where][0], col + directions[to_where][1]

    if 0 <= new_row < size and 0 <= new_col < size:
        return new_row, new_col
    else:
        return row, col


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
battlefield = []
submarine_pos = []
damage = 0
cruise = 0

for row_num in range(size):
    in_row = [*input()]
    battlefield.append(in_row)
    if "S" in in_row:
        submarine_pos = [row_num, in_row.index("S")]

battlefield[submarine_pos[0]][submarine_pos[1]] = "-"
old_row, old_col = submarine_pos
while True:
    direction = input()
    cur_row, cur_col = valid_position(old_row, old_col, direction)

    if battlefield[cur_row][cur_col] == "*":
        battlefield[cur_row][cur_col] = "-"
        damage += 1
        if damage == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{cur_row}, {cur_col}]!")
            break

    if battlefield[cur_row][cur_col] == "C":
        battlefield[cur_row][cur_col] = "-"
        cruise += 1
        if cruise == 3:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break


    old_row, old_col = cur_row, cur_col

battlefield[cur_row][cur_col] = "S"
for r in battlefield:
    print(''.join(r))
