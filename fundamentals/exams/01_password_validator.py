# Create a program that manipulates a string and makes it suitable for a password.
# Password rules are:
# •	Must be at least 8 characters long
# •	Consists only of letters, digits, and underscore - "_"
# •	Must have at least one uppercase letter
# •	Must have at least one lowercase letter
# •	Must have at least one digit
# First, you are going to receive the password that the user wants to use.
# Next, you will be receiving commands until you receive the "Complete" command. There are five possible commands:
# •	"Make Upper {index}"
# o	Replace the letter at the given index with upper case, then print the password.
# •	"Make Lower {index}"
# o	Replace the letter at the given index with lower case, then print the password.
# •	"Insert {index} {char}"
# o	Inserts the given char at the given index in the string, then print the password.
# o	If the index is not valid, ignore the command.
# •	"Replace {char} {value}"
# o	Get the ASCII value of the given char. Sum its value with the given value and replace all occurrences of the char with the new symbol corresponding to the sum result in the ASCII table. Print the password.
# o	If the char is not in the password, ignore the command.
# •	"Validation"
# o	Check why the password is not valid. Each of the checks should be performed in the order shown and are independent of each other:
# 1)	If it is not at least 8 characters, print: "Password must be at least 8 characters long!"
# 2)	If it does not consist only of letters, digits and underscore, print: "Password must consist only of letters, digits and _!"
# 3)	If it does not have at least one uppercase letter, print: "Password must consist at least one uppercase letter!"
# 4)	If it does not have at least one lowercase letter, print: "Password must consist at least one lowercase letter!"
# 5)	If it does not have at least one digit, print: "Password must consist at least one digit!"
# If a given command is not valid, you should ignore it.
# Input
# •	On the 1st line, you are going to receive the password in the form of a string.
# •	On the next lines, until you receive the "Complete" command, you will be receiving commands.
# •	The indexes will always be valid.
# Output
# •	Print the output of every command in the format described above.
import re
user_password = str(input())

while True:
    command = input().split()
    task = command[0]

    if task == 'Complete':
        break

    if task == 'Make':
        size = command[1]
        index = int(command[2])
        char = user_password[index]
        if abs(index) < len(user_password) - 2:
            if size == 'Upper':
                user_password = user_password[:index] + char.upper() + user_password[index+1:]
                print(f'{user_password}')
            elif size == 'Lower':
                user_password = user_password[:index] + char.lower() + user_password[index+1:]
                print(f'{user_password}')
        elif abs(index) >= 0 and index == len(user_password) - 1:
            if size == 'Upper':
                user_password = user_password[:index] + char.upper()
                print(f'{user_password}')
            elif size == 'Lower':
                user_password = user_password[:index] + char.lower()
                print(f'{user_password}')

    elif task == 'Insert':
        index = int(command[1])
        char = command[2]
        if abs(index) < len(user_password):
            user_password = user_password[:index] + char +user_password[index:]
            print(f'{user_password}')

    elif task == 'Replace':
        char = command[1]
        value = int(command[2])
        new_char = ord(char) + value
        if char in user_password:
            user_password = user_password.replace(char, chr(new_char))
            print(f'{user_password}')

    elif task == 'Validation':
        pattern = r'^\w+$'
        match = re.findall(pattern, user_password)

        if len(user_password) < 8:
            print("Password must be at least 8 characters long!")
        elif len(match) == 0:
            print('Password must consist only of letters, digits and _!')
        elif not any(x.isupper() for x in user_password):
            print('Password must consist at least one uppercase letter!')
        elif not any(x.islower() for x in user_password):
            print('Password must consist at least one lowercase letter!')
        elif not any(x.isdigit() for x in user_password):
            print('Password must consist at least one digit!')
