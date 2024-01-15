# Write a program that takes a single string and prints a list of all the capital letters indices.

string = input()
output = []

for letter in range(len(string)):
    if string[letter] == string[letter].upper():
        output.append(letter)

print(f'{output}')