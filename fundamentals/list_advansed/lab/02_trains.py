# You will receive a number representing the number of wagons a train has.
# Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.
train = [0] * int(input())

while True:
    command = list(input().split())

    if command[0] == 'End':
        print(f'{train}')
        break
    elif command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        train[int(command[1])] -= int(command[2])
