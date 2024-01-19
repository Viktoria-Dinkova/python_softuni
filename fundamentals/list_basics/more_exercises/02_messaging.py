# On the first line, you will receive a sequence of numbers separated by a single space.
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the first sequence.
# If the index is greater than the length of the text, continue counting from the beginning
# (so that you always have a valid index). When you find a char, you should add it to the message and remove it from the string.
# It means that for the following index, the text will contain one character less.
def massaging(cript_code: list, sorce_text: list) -> str:
    '''
    sends a message using chars from the given string by index - the sum of a number's digits from the first sequence

        :param cript_code: list
        :param sorce_text: str

        :return message: str
    '''
    message = ''
    for current_numbers_interval in cript_code: # findinf true index
        chars_index_num = list(x for x in current_numbers_interval)
        index_num = sum(list(int(y) for y in chars_index_num))

        if index_num >= len(sorce_text):
            index_num = index_num - len(sorce_text)

        message += sorce_text[index_num]
        sorce_text.pop(index_num)

    return message


shiffer_numbers = list(input().split())
start_string = list(input())

print(massaging(shiffer_numbers, start_string))