'''
Write a program that reads a number - N, representing the rows and columns of a square matrix.
On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
It would help if you started searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".
'''

size = int(input())

matrix = [[x for x in input()] for _ in range(size)]
symbol = input()

for row_index in range(size):
    for col_index in range(size):
        if symbol == matrix[row_index][col_index]:
            print(f'({row_index}, {col_index})')
            exit()
else:
    print(f'{symbol} does not occur in the matrix')