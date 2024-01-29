# Every gamer knows what rage-quitting means. It's when you're just not good enough, and you blame everybody else for losing a game
# - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular.
# He asks for your help. He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3".
# You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.
# Input
# •	The input data should be read from the console.
# •	It consists of a single line holding a series of string-number sequences.
# •	The input data will always be valid. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console. It should consist of exactly two lines:
# o	On the first line, print the number of unique symbols used in the message in the format described above.
# o	On the second line, print the rage message.
import re

strings = input()

sub_string = []
repeat = []
rage_string = ''

patt = r'(\D+)(\d+)'
code = re.findall(patt, strings)

for elements in code:
    sub_string.append(elements[0].upper())
    repeat.append(int(elements[1]))

for i in range(len(sub_string)):
    rage_string += sub_string[i] * repeat[i]

print(f'Unique symbols used: {len(set(rage_string))}')
print(rage_string)