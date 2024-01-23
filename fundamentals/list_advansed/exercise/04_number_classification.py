# Using a list comprehension, write a program that receives numbers, separated by comma and space ", "
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number
input_numbers = input()
print(f'Positive: {", ".join([str(element) for element in [int(num) for num in input_numbers.split(", ") if int(num) >= 0]])}')
print(f'Negative: {", ".join([str(element) for element in [int(num) for num in input_numbers.split(", ") if int(num) < 0]])}')
print(f'Even: {", ".join([str(element) for element in [int(num) for num in input_numbers.split(", ") if int(num) % 2 == 0]])}')
print(f'Odd: {", ".join([str(element) for element in [int(num) for num in input_numbers.split(", ") if int(num) % 2 != 0]])}')

