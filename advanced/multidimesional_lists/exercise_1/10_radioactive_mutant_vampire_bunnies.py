'''
First, you will receive a line holding integers N and M, representing the lair's rows and columns.
Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There will be only one player.
The bunnies are marked with "B", the player is marked with "P", and everything else is free space, marked with a dot ".".
Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:
•	L - the player should move one position to the left
•	R - the player should move one position to the right
•	U - the player should move one position up
•	D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny cell or a bunny reaches the player, the player dies.
If the player goes out of the lair without encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the bunnies spread normally), but there are no more turns.
There will be no cases where the moves of the player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. On the last line, print either "dead: {row} {col}" or "won: {row} {col}".
"Row" and "col" are the cell coordinates where the player has died or the last cell he has been in before escaping the lair.
Input
•	On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
•	On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P". All strings will be the same length. There will be only one "P" for all the input
•	On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
Output
•	On the first N lines, print the final state of the bunny lair
•	On the last line, print:
o	If the player won - "won: {row} {col}"
o	If the player dies - "dead: {row} {col}"
'''
def find_player_position():
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'P':
                return r, c

def valid_index(r, c, player = False):
    global wins
    if 0 <= r < rows and 0 <= c < cols:
        return True
    if player:
        wins = True

def check_player_alive(row, col):
    if matrix[row][col] == "B":
        results('dead')
def bunnies_positions():
    positions = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                positions.append([r, c])
    return positions

def bunnies_move(bunnies_pos):
    for row, col in bunnies_pos:
         for bunnie_move in directions.values():
             new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

             if valid_index(new_row, new_col):
                 matrix[new_row][new_col] = 'B'

def results(status='won'):
    [print(*row, sep='') for row in matrix]
    print(f'{status}: {player_row} {player_col}')

    raise SystemExit


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

player_row, player_col = find_player_position()
matrix[player_row][player_col] = '.'

wins = False
commands = input()

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

for command in commands:
    player_next_row, player_next_col = player_row + directions[command][0], player_col + directions[command][1]

    if valid_index(player_next_row, player_next_col, True):
        player_row, player_col = player_next_row, player_next_col

    bunnies_move(bunnies_positions())

    if wins:
        results()

    check_player_alive(player_row, player_col)