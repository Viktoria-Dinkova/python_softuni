# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
list_of_courses = {}
while True:
    command = input().split(':')
    if len(command) == 1:
        cours = command[0].replace('_',' ')
        if cours in list_of_courses.keys():
            print(f'{list_of_courses[cours]}')
            break
    else:
        if command[2] not in list_of_courses:
            list_of_courses[command[2]] = f'{command[0]} - {command[1]}'
        else:
            list_of_courses[command[2]] += f'\n{command[0]} - {command[1]}'

