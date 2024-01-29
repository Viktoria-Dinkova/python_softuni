# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

text = input()
encrypted_text = ''

for char in text:
    new_char = chr(ord(char) + 3)
    encrypted_text += new_char

print(f'{encrypted_text}')