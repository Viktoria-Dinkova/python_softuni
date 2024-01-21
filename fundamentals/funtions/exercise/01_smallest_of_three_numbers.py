# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.
def smallest(numbers: list) -> int:
    result = min(numbers)
    print(f'{result}')

in_numbers = [int(input()), int(input()),int(input())]

smallest(in_numbers)
