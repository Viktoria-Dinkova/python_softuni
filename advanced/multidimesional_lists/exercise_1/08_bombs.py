'''
You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line.
On the last line of input, you will receive indexes - coordinates of several cells separated by a single space,
in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given.
When a bomb explodes, it deals damage equal to its integer value to all the cells around it (in every direction and all diagonals).
One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).
Input
•	On the first line, you are given the integer N - the size of the square matrix.
•	The following N lines hold each column's values - N numbers separated by a space.
•	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
•	On the first line, you need to print the count of all alive cells in the format:
"Alive cells: {alive_cells}"
•	On the second line, you need to print the sum of all alive cells in the format:
"Sum: {sum_of_cells}"
•	In the end, print the matrix. A space must separate the cells.
'''
size = int(input())

matrix = []
cells_count = size ** 2
cells_sum = 0
for row in range(size):
    matrix.append([int(x) for x in input().split()])
    cells_sum += sum(matrix[row])

bombs = input().split()
def valid_index(indices: list):
    start_row, end_row = indices[0], indices[0]
    start_col, end_col = indices[1], indices[1]

    if start_row - 1 in range(size):
        start_row -= 1
    if end_row + 1 in range(size):
        end_row += 1
    if start_col - 1 in range(size):
        start_col -= 1
    if end_col + 1 in range(size):
        end_col += 1

    return [start_row, end_row, start_col, end_col]


for cur_bomb in bombs:
    cur_indices = list(int(x) for x in cur_bomb.split(','))
    damage = matrix[cur_indices[0]][cur_indices[1]]

    damage_start_row, damage_end_row, damage_start_col, damage_end_col = valid_index(cur_indices)
    for cel_row in range(damage_start_row, damage_end_row+1):
        for cel_col in range(damage_start_col, damage_end_col+1):
            if matrix[cel_row][cel_col] > 0:
                if matrix[cel_row][cel_col] >= damage:
                    cells_sum -= damage
                else:
                    cells_sum -= matrix[cel_row][cel_col]
                matrix[cel_row][cel_col] -= damage
                if matrix[cel_row][cel_col] <= 0:
                    cells_count -= 1


print(f'Alive cells: {cells_count}')
print(f'Sum: {cells_sum}')
[print(*r) for r in matrix]



