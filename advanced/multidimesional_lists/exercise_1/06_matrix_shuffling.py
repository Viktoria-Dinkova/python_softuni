'''
Write a program that reads a matrix from the console and performs certain operations with its elements.
 User input is provided similarly to the problems above - first, you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix.
A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
    (thus, you will be able to check if the operation was performed correctly).
•	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
    or the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.
'''

rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

def valid_indices(indices):
    if indices[0] in range(rows) and indices[2] in range(rows) and indices[1] in range(cols) and indices[3] in range(cols):
        return True
    else:
        return False

def swap(act: str, indices: list):
    if act == 'swap' and len(indices) == 4 and valid_indices(indices):
        r1, c1, r2, c2 = indices
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

        [print(*r) for r in matrix]

    else:
        print('Invalid input!')


command = input()
while command != 'END':
    action, *coordinates = [int(x) if x.isdigit() else x for x in command.split()]

    swap(action, coordinates)

    command = input()

