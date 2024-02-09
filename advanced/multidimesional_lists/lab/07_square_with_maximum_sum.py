'''
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its values.
On the first line, you will get matrix sizes in the format "{rows}, {columns}".
On the next rows, you will get elements for each column, separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements, as shown in the examples.
'''
rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')]for row in range(rows)]

max_sum = float('-inf')

for row in range(rows-1):
    for col in range(cols-1):
        suma = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]

        if suma > max_sum:
            max_sum = suma
            sub_matrix = [[matrix[row][col], matrix[row][col+1]], [matrix[row+1][col], matrix[row+1][col+1]]]

for r in range(2):
    print(*sub_matrix[r])
print(max_sum)

