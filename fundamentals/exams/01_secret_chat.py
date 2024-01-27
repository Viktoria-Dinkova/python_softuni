# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given,
# you will receive strings with instructions for different operations that need to be performed upon the concealed message
# to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string.
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

message = input()
out_message = message

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        print(f'You have a new text message: {out_message}')
        break

    if command[0] == 'InsertSpace':
        index = int(command[1])
        out_message = out_message[:index] + ' ' + out_message[index:]
        print(f'{out_message}')

    elif command[0] == 'Reverse':
        substr = command[1]
        if substr in out_message:
            start_index = out_message.find(substr)
            end_index = out_message.find(substr) + len(substr)
            out_message = out_message[:start_index] + out_message[end_index:] + substr[::-1]
            print(f'{out_message}')
        else:
            print('error')

    elif command[0] == 'ChangeAll':
        old_string = command[1]
        new_string = command[2]
        if old_string in out_message:
            out_message = out_message.replace(old_string, new_string)
        print(f'{out_message}')