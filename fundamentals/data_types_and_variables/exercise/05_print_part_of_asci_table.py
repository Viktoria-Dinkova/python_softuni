# Write a program that prints part of the ASCII table characters on the console,
# separated by a single space. On the first line of input,
# you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

start_character = int(input())
last_character = int(input())

text = ''

for char in range(start_character, last_character + 1):
    current_char = chr(char)
    text += (current_char + ' ')

print(f'{text[:len(text) - 1]}')
