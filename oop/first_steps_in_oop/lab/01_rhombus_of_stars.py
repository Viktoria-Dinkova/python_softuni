"""
Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:
"""


def print_rombus(size):
    for i in range(1, size+1):
        print(' ' * (size - i), '* ' * i)
    for j in range(size-1, 0, -1):
        print(' ' * (size - j), '* ' * j)


number_of_stars = int(input())
print_rombus(number_of_stars)
