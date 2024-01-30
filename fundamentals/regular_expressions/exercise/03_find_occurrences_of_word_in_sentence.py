# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.
import re

string = input()
sub_string = input()
output_names = []

patt = fr'\b{sub_string}\b'

found = re.findall(patt, string, re.I)
if len(found) > 0:
    output_names.extend(found)



print(f'{len(output_names)}')