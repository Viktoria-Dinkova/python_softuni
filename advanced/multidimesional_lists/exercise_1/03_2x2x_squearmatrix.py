'''
Find the number of all 2x2 squares containing identical chars in a matrix.
On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
In the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.
'''
rows, cols = [int(x) for x in input().split()]
matrix = [input().split(' ') for _ in range(rows)]

size_sub_matrix = 2

count_sub_matrix = 0

for row_index in range(rows-size_sub_matrix+1):
    for col_index in range(cols-size_sub_matrix+1):

        sub_matrix = []
        equel_el = set()
        for in_row_index in range(size_sub_matrix):
            sub_matrix.append([])
            for in_col_index in range(size_sub_matrix):
                sub_matrix[in_row_index].append(matrix[row_index+in_row_index][col_index+in_col_index])
                equel_el.add(matrix[row_index+in_row_index][col_index+in_col_index])

        if len(equel_el) == 1:
            count_sub_matrix += 1
            #sub_matrix

print(count_sub_matrix)
