'''
Chess is the oldest game, but it is still popular these days. You will use only one chess piece for this task - the Knight.
A chess knights has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal.
(e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
The knights game is played on a board with dimensions N x N.
You will receive a board with a "K" for knights and a "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.
Always remove the knights who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.
'''

def valid_psition(row_position, col_position):
    if 0 <= row_position < size and 0 <= col_position < size:
        return True

moves = {
    'ul_move': (-2, -1),
    'ur_move': (-2, 1),
    'lu_move': (-1, -2),
    'ld_move': (1, -2),
    'ru_move': (-1, 2),
    'rd_move': (1, 2),
    'dl_move': (2, -1),
    'dr_move': (2, 1),
}

def knight_moves(position_row, position_col):
    loc_damage = 0
    for curr_move in moves.values():
        new_row, new_col = position_row + curr_move[0], position_col + curr_move[1]
        if valid_psition(new_row, new_col):
            if matrix[new_row][new_col] == 'K':
                loc_damage += 1
    return loc_damage


size = int(input())
knights = []
matrix = []
for i in range(size):
    one_row = list(input())
    matrix.append(one_row)
    for j in range(size):
        if one_row[j] == 'K':
            knights.append([i, j])

knight_damage = 0
max_damage = 0
removed = 0
worst_knight_position = []

while True:

    for cur_knight in knights:
        if knight_moves(cur_knight[0], cur_knight[1]) > max_damage:
            max_damage = knight_moves(cur_knight[0], cur_knight[1])
            worst_knight_position = cur_knight

    if max_damage > 0:
        matrix[worst_knight_position[0]][worst_knight_position[1]] = 'O'
        knights.remove(worst_knight_position)
        removed += 1
        max_damage = 0
        worst_knight_position = []
    else:
        break

print(removed)
