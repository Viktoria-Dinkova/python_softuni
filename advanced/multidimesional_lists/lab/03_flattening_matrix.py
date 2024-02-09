'''
Write a program that receives a matrix and prints its flattened version (a list with all the values).
For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows,
 you will get the elements for each column separated with a comma and a space ", ".
'''

matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
flat_matrix = []
for row in matrix:
    flat_matrix.extend(row)

print(flat_matrix)