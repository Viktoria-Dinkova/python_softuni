'''
Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
On the first line, you will receive an integer N – the size of a square matrix.
The next N lines hold the values for each column - N numbers, separated by a single space.
'''
rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

dsum = 0
for row_index in range(rows):
    for column_index in range(rows):
        if row_index == column_index:
            dsum += matrix[row_index][column_index]

# right_diagonal
# for row_index in range(rows):
#     for column_index in range(rows, -1, -1):
#         column_index *= -1
#         if row_index + column_index == -1:
#             dsum += matrix[row_index][column_index]

print(dsum)