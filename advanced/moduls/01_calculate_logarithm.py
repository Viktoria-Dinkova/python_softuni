"""
Write a program that prints the calculated logarithm of any given number
Input
· On the first line, you will receive the number (an integer)
· On the second line, you will receive a number, which is the logarithm base. It can be either a number or the word "natural"
The output should be formatted to the 2nd decimal digit
"""
from math import log

the_number = int(input())
base = input()

result = 0

if base == "natural":
    result = log(the_number)
elif isinstance(base, int):
    base = int(base)
    result = log(the_number, base)

print(f'{result:.2f}')

