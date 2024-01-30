# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.
import re

extracted_numbers = []

string = input()

while string:

    search = r'\d+'
    finded = re.findall(search, string)
    if len(finded) > 0:
        extracted_numbers.extend(finded)

    string = input()

print(f'{" ".join(extracted_numbers)}')