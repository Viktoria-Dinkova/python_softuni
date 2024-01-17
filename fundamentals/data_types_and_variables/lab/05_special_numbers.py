# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

count_of_numbers = int(input())

for number in range(1,count_of_numbers + 1):
    char_number = str(number)
    sum_of_char_number = 0
    special = False
    for char in char_number:
        sum_of_char_number += int(char)

    if sum_of_char_number in [5,7,11]:
        special = True

    print(f'{number} -> {special}')
