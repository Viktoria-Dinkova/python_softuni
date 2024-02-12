'''
Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N.
You will get elements for each column on the following N lines, separated with a single space.
You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in the range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.
'''
rows = int(input())
matrix = []
cols = {}
for i in range(rows):
    i_row = [int(x) for x in input().split()]
    matrix.append(i_row)
    cols[i] = len(i_row)

command = input()
while command != "END":
    action, row_index, col_index, value = [z if z.isalpha() else int(z) for z in command.split()]

    if 0 <= row_index < rows and 0 <= col_index < cols[row_index]:
        if action == "Add":
            matrix[row_index][col_index] += value
        elif action == "Subtract":
            matrix[row_index][col_index] -= value
    else:
        print(f'Invalid coordinates')

    command = input()

[print(*el) for el in matrix]
