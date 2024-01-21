# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def palindrome_numbers(input_positive_integers: list) -> bool:
    '''
    check if number in list of positive integers is it palindrom

        :param input_positive_integers: list

        :return message: bool
    '''
    for num in input_positive_integers:
        rev_num = num[::-1]
        if num == rev_num:
            print(True)
        else:
            print(False)

input_list = list(input().split(', '))
palindrome_numbers(input_list)
