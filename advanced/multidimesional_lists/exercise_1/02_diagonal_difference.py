'''
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix.
The following N lines hold the values for each column - N numbers separated by a single space.
Print the absolute difference between the primary and the secondary diagonal sums.
'''
size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []
for row_index in range(size):
    for column_index in range(size):
        if row_index == column_index:
            primary_diagonal.append(matrix[row_index][column_index])

for row_index in range(size):
    for column_index in range(size, -1, -1):
        column_index *= -1
        if row_index + column_index == -1:
            secondary_diagonal.append(matrix[row_index][column_index])

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(f'{result}')

