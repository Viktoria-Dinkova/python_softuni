# You will be receiving names until the command "Welcome!".
#
# · If the name is less than 5 chars, the student is going into Gryffindor
# o Print "{name} goes to Gryffindor."
# · If the name is exactly 5 chars, the student is going into Slytherin
# o Print "{name} goes to Slytherin."
# · If the name is exactly 6 chars, the student is going into Ravenclaw
# o Print "{name} goes to Ravenclaw."
# · If the name is more than 6 chars, the student is going into Hufflepuff
# o Print "{name} goes to Hufflepuff."
#
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!"
# and end the program. No more sorting for today!
#
# If all students are sorted successfully, print "Welcome to Hogwarts."

name = input()
message = ''

while name != 'Welcome!':
    if name != 'Voldemort':
        if len(name) < 5:
            message = ' goes to Gryffindor.'
        elif len(name) == 5:
            message = ' goes to Slytherin.'
        elif len(name) == 6:
            message = ' goes to Ravenclaw.'
        elif len(name) > 6:
            message = ' goes to Hufflepuff.'

        print(f'{name}{message}')
        name = input()
    else:
        print(f'You must not speak of that name!')
        break

if name != 'Voldemort':
    print('Welcome to Hogwarts.')