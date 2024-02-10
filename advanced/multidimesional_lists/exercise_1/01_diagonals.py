'''
Using a nested list comprehension, write a program that reads size of a square matrix and its elements, separated by a comma and a space ", ".
 You should find the matrix's diagonals, print them, and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
'''
size = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]

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

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
