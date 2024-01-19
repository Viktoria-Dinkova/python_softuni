# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

numbers_of_command = int(input())
serch_word = input()

all_stirngs = []
matching = []
for num in range(numbers_of_command):
    input_string = input()
    all_stirngs.append(input_string)

    if serch_word in input_string:
        matching.append(input_string)

print(f'{all_stirngs}\n{matching}')