# During World War 2, you are a mathematician who joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message.
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations
# that need to be performed upon the concealed message to interpret it and reveal its true content.
# There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"During World War 2, you are a mathematician who joined the cryptography team to decipher the enemy's enigma code. Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

encrypted_message = input()
message = encrypted_message

while True:
    instruction = input().split('|')

    if instruction[0] == 'Decode':
        print(f'The decrypted message is: {message}')
        break

    elif instruction[0] == 'Move':
        index = int(instruction[1])
        message = message[index:] + message[:index]

    elif instruction[0] == 'Insert':
        index = int(instruction[1])
        value_for_insert = instruction[2]
        message = message[:index] + value_for_insert + message[index:]

    elif instruction[0] == 'ChangeAll':
        search_substring = instruction[1]
        substring_for_replace = instruction[2]
        message = message.replace(search_substring,substring_for_replace)


