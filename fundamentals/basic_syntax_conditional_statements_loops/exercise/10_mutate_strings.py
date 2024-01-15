# You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first one. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()
new_string = ''

for letter in range(len(first_string)):
    new_string = new_string[:letter] + (second_string[letter] + first_string[letter + 1:])
    if first_string[letter] != second_string[letter]:
        print(f'{new_string}')
