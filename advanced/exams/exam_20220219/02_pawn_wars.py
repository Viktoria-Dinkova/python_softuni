"""
A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H.
We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
	White (w) moves from the 1st rank to the 8th rank direction.
	Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:
When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
o	Empty positions are marked with "-".
o	White pawn is marked with "w"
o	Black pawn is marked with "b"
Output
Print either one of the following:
•	If a pawn captures the other, print:
o	"Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
"""


def next_pos(row, collor):
    next_row = row + moves[collor]
    return next_row


dic = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'e'}

moves = {
    'move_withe': 1,
    'move_black': -1
}

chessboard = []
size = 8
for ch_r in range(8, 0, -1):
    data_row = input().split()
    chessboard.append(data_row)
    if "w" in data_row:
        withe_row, withe_col = ch_r, data_row.index("w")
    if "b" in data_row:
        black_row, black_col = ch_r, data_row.index("b")

while True:
    withe_row = next_pos(withe_row, 'move_withe')
    if withe_row == 8:
        square = dic[withe_col] + str(withe_row)
        print(f"Game over! White pawn is promoted to a queen at {square}.")
        break

    elif withe_row == black_row and abs(withe_col - black_col) == 1:
        withe_row, withe_col = black_row, black_col
        square = dic[withe_col] + str(withe_row)
        print(f"Game over! White win, capture on {square}.")
        break

    black_row = next_pos(black_row, 'move_black')
    if black_row == 1:
        square = dic[black_col] + str(black_row)
        print(f"Game over! Black pawn is promoted to a queen at {square}.")
        break

    elif withe_row == black_row and abs(withe_col - black_col) == 1:
        black_row, black_col = withe_row, withe_col
        square = dic[black_col] + str(black_row)
        print(f"Game over! Black win, capture on {square}.")
        break