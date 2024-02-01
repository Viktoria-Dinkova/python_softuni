# Write a program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

string = list(input())

while string:
    print(f'{string.pop()}', end='')