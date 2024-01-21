# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

def min_max_sum(input_sequence: list) -> int:
    '''
    print the min, max values and the sum of all numbers in input sequence of integers

        :param input_sequence: list

        :return min_number: int,
                max_number: int,
                numbers_sum: int
    '''
    num_input_sequence = [int(i) for i in input_sequence]

    min_number = min(num_input_sequence)
    max_number = max(num_input_sequence)
    numbers_sum = sum(num_input_sequence)

    return min_number, max_number, numbers_sum

numbers_sequence = input().split()
min_number, max_number, numbers_sum = min_max_sum(numbers_sequence)
print(f'The minimum number is {min_number}\n'
      f'The maximum number is {max_number}\n'
      f'The sum number is: {numbers_sum}')