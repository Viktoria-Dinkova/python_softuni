"""
Create a program that will receive commands until the command "End". The commands can be:
· "Create-{file_name}" - Creates the given file with empty content. If the file already exists, remove the existing text in it (as if the file is created again)
· "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
· "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
· "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
"""
import os.path


def creation(name):
    way = os.path.join('texts', name)
    with open(way, 'w') as file:
        file.write('')


def writing(name, text):
    way = os.path.join("texts", name)
    with open(way, 'a') as file:
        file.write(text)


def editing(name, old, new):
    way = os.path.join('texts', name)
    try:
        with open(way, 'r+') as file:
            text = file.read()
            text = text.replace(old, new)

            file.seek(0)
            file.write(text)
            file.truncate()

    except (FileNotFoundError, FileExistsError):
        print("file not exist")


def deleting(name):
    way = os.path.join('texts', name)
    try:
        os.remove(way)
    except (FileNotFoundError, FileExistsError):
        print("file not exist")


while True:
    command = input().split('-')
    action = command[0]

    if action == "End":
        break

    if action == 'Create':
        creation(command[1])
    elif action == 'Add':
        writing(command[1], command[2])
    elif action == 'Replace':
        editing(command[1], command[2], command[3])
    elif action == 'Delete':
        deleting(command[1])

