'''
You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape.
On the following lines, you will receive the matrix, which represents the neighborhood.
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
If the cell has an "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked with "V".
There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
Santa can move "up", "down", "left", and "right" with one position each time. These will be the commands that you receive.
If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present.
If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him*
(meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
Keep in mind that you should check whether all the nice kids received presents.
Input
•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
Output
•	On the first line:
o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
•	Next, print the matrix.
•	In the end, print one of these messages:
o	If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o	Otherwise, print:
"No presents for {count nice kids} nice kid/s."
'''
def moves(row, col):
    new_row, new_col = row + directions[command][0], col + directions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        return [new_row, new_col]
    return [row,col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

presents = int(input())
size = int(input())
matrix = []
santa = []
nice = 0

for l in range(size):
    line = input().split()
    matrix.append(line)

    if 'S' in line:
        santa = [l, matrix[l].index("S")]
        matrix[santa[0]][santa[1]] = '-'

    if "V" in line:
        nice += line.count("V")

init_nice = nice
command = input()
while presents > 0 and command != "Christmas morning":

    santa = moves(santa[0], santa[1])

    if matrix[santa[0]][santa[1]] == "V":
        presents -= 1
        nice -= 1

    elif matrix[santa[0]][santa[1]] == "C":

        for cookie_move in directions.values():
            cookie_pos = [santa[0] + cookie_move[0], santa[1] + cookie_move[1]]
            if 0 <= cookie_pos[0] < size and 0 <= cookie_pos[1] < size:
                if matrix[cookie_pos[0]][cookie_pos[1]] in ["V", "X"]:
                    if matrix[cookie_pos[0]][cookie_pos[1]]  == "V":
                        nice -= 1
                    matrix[cookie_pos[0]][cookie_pos[1]] = '-'
                    presents -= 1

    matrix[santa[0]][santa[1]] = '-'
    if presents <= 0:
        break
    command = input()

matrix[santa[0]][santa[1]] = 'S'
if presents <= 0 and nice > 0:
    print("Santa ran out of presents!")

[print(*m) for m in matrix]

if nice <= 0:
    print(f"Good job, Santa! {init_nice} happy nice kid/s.")
else:
    print(f"No presents for {nice} nice kid/s.")
