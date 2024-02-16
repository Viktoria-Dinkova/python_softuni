"""
You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.

It is given a sequence of numbers, separated by a ", ". Iterate through each number by its index,
and if the number is smaller or equal to 5, make a multiplication.
If the number is larger than 5 and smaller or equal to 10, divide the result by the number. In the end, print the final result.
"""

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    try:
        number = numbers_list[i]
    except IndexError:
        print("there is invalid index")
    if number <= 5:
        result *= number
    elif number <= 10:
        try:
            result /= number
        except ZeroDivisionError:
            print("Can't divide by zero ")

try:
    print(total)
except NameError:
    print(result)