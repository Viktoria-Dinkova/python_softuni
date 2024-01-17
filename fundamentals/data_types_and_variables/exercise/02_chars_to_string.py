# Write a function that receives 3 characters.
# Concatenate all the characters into one string and print it on the console.

char = ''
text = ''

for num_of_chdar in range(3):
    char = input()
    text += char

print(f'{text}')