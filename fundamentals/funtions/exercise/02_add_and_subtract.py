# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(number_1: int, number_2: int) -> int:
    '''
    returns the sum of the first two integers
        :param number_1 - int
        :param number_2 - int

        :return - int
    '''
    return number_1 + number_2

def substract(sum_of_tow: int, number_3: int) -> int:
    '''
    returns the difference between result of sum_numbers() and the third integer
        :param sum_of_tow - int
        :param number_3 - int

        :return - int
    '''
    return sum_of_tow - number_3


def add_and_subtract(first_num: int, second_num: int, third_num: int) -> int:
    '''
    receive the three numbers as parameters. Print the result of the subtract() function on the console.
        :param number_1 - int
        :param number_2 - int
        :param number_3 - int

        :return - int
    '''
    sum_of_tow = sum_numbers(first_num, second_num)
    return substract(sum_of_tow, third_num)

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))

