# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first.
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel",
# you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
#       o	Insert the given string at that index only if the index is valid.
# •	"Remove Stop:{start_index}:{end_index}":
#       o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid.
# •	"Switch:{old_string}:{new_string}":
#       o	If the old string is in the initial string, replace it with the new one (all occurrences).
# Note: After each command, print the current state of the string!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}".

initial_trace = input()
trace = initial_trace

while True:
    command = input().split(':')
    action = command[0]
    if action == 'Travel':
        print(f'Ready for world tour! Planned stops: {trace}')
        break

    elif action == 'Add Stop':
        index = int(command[1])
        new_destination = command[2]
        if index >= 0 and index < len(trace):
            trace = trace[:index] + new_destination + trace[index:]
        print(f'{trace}')

    elif action == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index >= 0 and end_index < len(trace) and end_index >= start_index:
            trace = trace[:start_index] + trace[end_index + 1:]
        print(f'{trace}')

    elif action == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in trace:
            trace = trace.replace(old_string, new_string)
        print(f'{trace}')
