# A company hires you to create a program that implements a chat logger which works with commands.
# You may receive the following commands:
# • "Chat {message}": o Add the message at the last position in the chat.
# • "Delete {message}": o Delete the message if it exists. o Otherwise, ignore the command.
# • "Edit {message} {editedVersion}": o Update the message with the edited version. o If it does not exist, ignore the command.
# • "Pin {message}": o Find the given message and move it to the last index. o If it does not exist, ignore the command.
# • "Spam {message1} {message2} {messageN}": o Add all messages at the end of the chat.
# • "end": o Stop receiving commands. After the "end" command, you should print the chat history starting from the first message.
# Input • Until you receive "end", you will be receiving commands.
# Output • As output, you must print the chat starting from the first message. Every message must be in a new line.
# Constraints • The command will always be valid.
message = []
while True:
    command = input().split()
    if command[0] == 'Chat':
        message.append(command[1])
    elif command[0] == 'Delete' and command[1] in message:
        message.remove(command[1])
    elif command[0] == 'Edit' and command[1] in message:
        index = message.index(command[1])
        message.remove(command[1])
        message.insert(index, command[2])
    elif command[0] == 'Pin' and command[1] in message:
        message.remove(command[1])
        message.append(command[1])
    elif command[0] == 'Spam':
        count_message = len(command)
        for curr_message in range(1, count_message):
            message.append(command[curr_message])

    if command[0] == 'end':
        out = "\n".join(message)
        print(f'{out}')
        break