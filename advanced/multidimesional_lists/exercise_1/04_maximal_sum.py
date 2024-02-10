'''
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements.
There will be no case with two or more 3x3 squares with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
•	On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
Output
•	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
•	On the following 3 lines, print each element of the found submatrix, separated by a single space
'''
rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]

size_sub_matrix = 3
max_sum = float('-inf')

for row_index in range(rows-size_sub_matrix+1):
    for col_index in range(cols-size_sub_matrix+1):

        sub_matrix = []
        sum_sub_matrix = 0
        for in_row_index in range(size_sub_matrix):
            sub_matrix.append([])
            for in_col_index in range(size_sub_matrix):
                sub_matrix[in_row_index].append(matrix[row_index+in_row_index][col_index+in_col_index])

        for i in range(size_sub_matrix):
            for j in range(size_sub_matrix):
                sum_sub_matrix += sub_matrix[i][j]

        if sum_sub_matrix > max_sum:
            max_sum = sum_sub_matrix
            end_matrix = sub_matrix

print(f'Sum = {max_sum}')
[print(*r) for r in end_matrix]

