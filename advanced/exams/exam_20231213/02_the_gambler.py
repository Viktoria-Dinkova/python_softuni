'''You will be given an integer n for the size of the game board (square shape). On the next n lines, you will receive the rows of the board.
The gambler will start at a random position, marked with the letter 'G' and have an initial 'entering the game' amount of 100$.
On each turn, until command 'end' is received, you will receive commands for the direction, in which the gambler should move.
The commands will be "up", "down", "left" and "right".
•	If a position with '-' (dash) is reached, it means that the field is empty and the gambler awaits its next direction.
•	If the position marked with the letter 'W' is reached the gambler takes it and adds 100$ to his amount
•	If the position marked with the letter 'P' (penalty) is reached decrease the gambler's total amount by 200$
•	If the position marked with the letter 'J' is reached the gambler wins the jackpot and adds 100000$ to his amount and the game ends.
•	If the gambler leaves the boundaries of the board or his total amount becomes equal to or drops below 0 (zero), he loses everything and you should stop the program.
The current gambler position should be marked with 'G'
When the gambler leaves a position marked with a letter it should be replaced by '-' (dash)
The program ends when one of these four events occurs:
•	the gambler leaves the board boundaries
•	command 'end' is received
•	the gambler's total winning amount is equal to or drops below 0(zero)
•	the position marked with 'J' is reached
Input
•	On the first line, you are given the integer n – the size of the matrix (board).
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a direction command.
Output
•	If you win the jackpot on the first and second lines print:
o	"You win the Jackpot!
End of the game. Total amount: {amount}$"
•	If you do not win the jackpot print:
o	"End of the game. Total amount: {amount}$"
•	If you leave the boundaries of the matrix or the gambler's amount becomes 0(zero) or below print:
o	"Game over! You lost everything!"
'''
def valid_position(pos: list, act: str) -> list:
    row, col = pos
    row += directions[act][0]
    col += directions[act][1]

    if 0 <= row <= size and 0 <= col <= size:
        return [row, col]


size = int(input())
board = []

gambler_position = []
amount = 100

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    in_row = [x for x in input()]
    board.append(in_row)
    if 'G' in in_row:
        gambler_position = [r, in_row.index('G')]

board[gambler_position[0]][gambler_position[1]] = '-'
curr_position = gambler_position

while True:
    command = input()
    if command == 'end':
        print(f"End of the game. Total amount: {amount}$")
        if amount > 0:
            [print(*row, sep='') for row in board]
        break

    else:
        if valid_position(curr_position, command):
            board[curr_position[0]][curr_position[1]] = '-'
            curr_position = valid_position(curr_position, command)

            if board[curr_position[0]][curr_position[1]] == 'J':
                amount += 100000
                print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
                [print(*row, sep='') for row in board]
                break

            elif board[curr_position[0]][curr_position[1]] == 'W':
                amount += 100

            elif board[curr_position[0]][curr_position[1]] == 'P':
                amount -= 200
                if amount <= 0:
                    print("Game over! You lost everything!")
                    break

            board[curr_position[0]][curr_position[1]] = 'G'







