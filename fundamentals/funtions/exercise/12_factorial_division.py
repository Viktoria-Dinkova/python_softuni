# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial_devisidn(num_1: int, num_2: int) -> float:
    '''
    Divide calculated factorials of two integer numbers

        :param num_1: int
        :param num_2: int

        :return devision: float
    '''
    first_factorial, second_factorial = 1, 1
    x, y = 1, 1

    while x <= num_1:
        first_factorial *= x
        x += 1

    while y <= num_2:
        second_factorial *= y
        y += 1


    devision = first_factorial / second_factorial

    return print(f'{devision:.2f}')


first_num = int(input())
second_num = int(input())
factorial_devisidn(first_num, second_num)