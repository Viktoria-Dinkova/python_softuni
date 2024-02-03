'''
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
The number must be formatted to the first decimal point.
'''

numbers = tuple(map(float, input().split()))
inventory_num = {}

for num in numbers:
    if num not in inventory_num:
        inventory_num[num] = numbers.count(num)
        print(f'{num} - {inventory_num[num]} times')