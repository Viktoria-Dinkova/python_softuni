# Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course and all the exercises for the lessons.
# Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next course, separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:
# •	"Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# •	"Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# •	"Remove:{lessonTitle}" - remove the lesson, if it exists.
# •	"Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# •	"Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
# Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.
# Input / Constraints
# •	On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
# •	Until "course start" you will receive commands in the format described above.
# Output
# •	Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".
# •	Allowed working time / memory: 100ms / 16MB.

course_schedule = input().split(', ')
command = []

while command != 'course start':
    command = input().split(':')
    tasks = command[0]

    if tasks == 'Add':
        if course_schedule.count(command[1]) == 0:
            course_schedule.append(command[1])

    elif tasks == 'Insert':
        if course_schedule.count(command[1]) == 0:
            course_schedule.insert(int(command[2]), command[1])

    elif tasks == 'Remove':
        if course_schedule.count(command[1]) != 0:
            course_schedule.remove(command[1])

    elif tasks == 'Swap':
        if course_schedule.count(command[1]) != 0 and course_schedule.count(command[2]) != 0:
            first_course = course_schedule.index(command[1])
            second_course = course_schedule.index(command[2])

            course_schedule[first_course] = command[2]
            course_schedule[second_course] = command[1]
            exercise_1 = command[1] + '-Exercise'
            exercise_2 = command[2] + '-Exercise'

            if course_schedule.count(exercise_1) != 0:
                course_schedule.remove(exercise_1)
                new_index1 = course_schedule.index(command[1])
                course_schedule.insert(new_index1 + 1, exercise_1)
            if course_schedule.count(exercise_2) != 0:
                course_schedule.remove(exercise_2)
                new_index2 = course_schedule.index(command[2])
                course_schedule.insert(new_index2 + 1, exercise_2)

    elif tasks == 'Exercise':
        if course_schedule.count(command[1]) > 0:
            lesson_index = course_schedule.index(command[1])
            exercise = command[1] + '-Exercise'
            if course_schedule.count(exercise) == 0:
                course_schedule.insert(lesson_index + 1, exercise)
        else:
            course_schedule.append(command[1])
            exercise = command[1] + '-Exercise'
            course_schedule.append(exercise)

    elif tasks == 'course start':
        break

    course_number = [str(x) for x in range(1, len(course_schedule) + 1)]
    output = [course_number[i]+'.'+course_schedule[i] for i in range(len(course_schedule))]
    output = "\n".join(output)

print(f'{output}')
