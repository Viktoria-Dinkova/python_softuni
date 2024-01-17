# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

number_of_letters = int(input())
text = ''

for first_char in range (97, 97 + number_of_letters):
    for second_char in range (97, 97 + number_of_letters):
        for third_char in range (97, 97 + number_of_letters):
            text = chr(first_char) + chr(second_char) + chr(third_char)
            print(f'{text}')
