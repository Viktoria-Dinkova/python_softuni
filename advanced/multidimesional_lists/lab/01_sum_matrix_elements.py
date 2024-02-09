'''
Write a program that reads a matrix from the console and prints:
•	The sum of all numbers in the matrix
•	The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
 On the next rows, you will get elements for each column separated by a comma and a space ", ".
'''
# from datetime import datetime

# start = datetime.now()

rows, columns = [int(x) for x in input().split(', ')]

matrix = []
tot_sum = 0
for _ in range(rows):
    curr_row = [int(x) for x in input().split(', ')]
    matrix.append(curr_row)
    tot_sum += sum(curr_row)

# end = datetime.now()
#
# print(end - start)

print(tot_sum)
print(matrix)