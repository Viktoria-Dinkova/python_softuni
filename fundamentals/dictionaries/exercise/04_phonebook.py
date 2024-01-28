# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

phonbook = {}

while True:
    command = input()

    if '-' in command:
        people = command.split('-')
        phonbook[people[0]] = people[1]
    else:
        searching_people = int(command)
        for _ in range(searching_people):
            human = input()
            if human in phonbook:
                print(f'{human} -> {phonbook[human]}')
            else:
                print(f'Contact {human} does not exist.')
        break