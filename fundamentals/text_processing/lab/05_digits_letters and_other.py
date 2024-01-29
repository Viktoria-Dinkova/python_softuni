# Write a program that receives a single string.
# On the first line, print all the digits found in the string,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.
received_string = input()

digits = ''
letters = ''
other = ''

for char in received_string:
    if char.isdigit() == True:
        digits += char
    elif char.isalpha() == True:
        letters += char
    else:
        other += char

print(f'{digits}')
print(f'{letters}')
print(f'{other}')