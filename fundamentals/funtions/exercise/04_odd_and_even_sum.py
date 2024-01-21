# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def even_odd_sum(input_number: str) -> str:
    '''
    returns the sum of all even and all odd digits in a given input

        :param input_number: str

        :return even_sum: int, odd_sum: int
    '''
    even_sum = 0
    odd_sum = 0

    for i in input_number:
        current_num = int(i)

        if current_num % 2 ==0:
            even_sum += current_num
        else:
            odd_sum += current_num

    return even_sum, odd_sum

numbers = input()
even_s, odd_s = even_odd_sum(numbers)
print(f'Odd sum = {odd_s}, Even sum = {even_s}')
