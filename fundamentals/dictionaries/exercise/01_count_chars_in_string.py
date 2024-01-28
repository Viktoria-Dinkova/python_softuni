# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
string = input().replace(' ','')
dict_string = {}
for character in string:
    if character not in dict_string:
        dict_string[character] = 1
    else:
        dict_string[character] += 1

for char, count in dict_string.items():
    print(f'{char} -> {count}')