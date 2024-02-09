'''
Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
On the first line, you will get matrix sizes in the format "{rows}, {columns}".
On the next rows, you will get elements for each column separated with a single space.
'''

rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for i in range(columns):
    column_sum = 0
    for j in range(rows):
        column_sum += matrix[j][i]
    print(column_sum)