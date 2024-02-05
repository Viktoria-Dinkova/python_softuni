'''
Write a program that reads a text from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order.
'''

occurrences = {}

for letter in input():
    occurrences[letter] = text.count(letter)

for k, v in sorted(occurrences.items()):
    print(f'{k}: {v} time/s')


# text = input()
#
# occurrences = {}
#
# for letter in text:
#     occurrences[letter] = text.count(letter)
#
# for k, v in sorted(occurrences.items()):
#     print(f'{k}: {v} time/s')
