# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
string = input()
output = ''
stamp = ''
for char in string:
    if stamp != char:
        output += char
        stamp = char

print(f'{output}')