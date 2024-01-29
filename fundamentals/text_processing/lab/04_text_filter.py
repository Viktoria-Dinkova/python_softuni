# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.
ban_list = input().split(', ')
text = input()

for ban_word in ban_list:
    text = text.replace(ban_word, '*' * len(ban_word))

print(f'{text}')