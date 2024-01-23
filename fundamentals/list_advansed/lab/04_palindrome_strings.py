# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

input_list = input().split()
palindrom = input()
finded_palindrom = []

for word in input_list:
    current_word = word[::-1]
    if word == current_word:
        finded_palindrom.append(word)

print(f'{finded_palindrom}')
print(f'Found palindrome {finded_palindrom.count(palindrom)} times')