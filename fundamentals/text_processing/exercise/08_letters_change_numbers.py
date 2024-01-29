# You receive a string consisting of a number between two letters.
# For the given string, you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping
# track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers,
# it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.
# Input
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly
# Output
# •	Print at the console a single number:
# o	The total sum of all processed numbers, formatted to the second decimal separator
import re

string = input().split()
total = 0

def position_in_alphabet(char: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for curr_position in range(len(alphabet) + 1):

        if char.lower() == alphabet[curr_position]:
            return curr_position + 1
            break


for element in string:
    reg_ex = r'\d+'
    number = re.search(reg_ex, element)
    start_of_num = number.start()
    end_of_num = number.end()

    front_letter = element[start_of_num - 1]
    end_letter = element[end_of_num]

    if front_letter == front_letter.upper():
       result = int(number.group()) / position_in_alphabet(front_letter)
    else:
        result = int(number.group()) * position_in_alphabet(front_letter)

    total += result

    if end_letter == end_letter.upper():
        total -= position_in_alphabet(end_letter)
    else:
        total += position_in_alphabet(end_letter)

# 12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=33012/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330
print(f'{total:.2f}')

