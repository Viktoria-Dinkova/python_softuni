'''
Write a function called softuni_students that receives information about students, their course id, and course name and returns the result.
The function will receive a different number of arguments and keyword arguments. The arguments will be passed as follows:
•	The first arguments will be tuple key-value pairs – the first one is the course id (string) and the second one is the username (every username will be unique) of the student (string);
•	The following data will be the keyword arguments - the first one is the course id (string), and the second one is the course name (string);
After receiving the information and calling the function:
•	You should link the student to their course.
•	Sort the data by student’s username (alphabetically), and if a student's course ID is not linked to a certain course, consider the student invalid.
•	Keep in mind that one course could be linked to one or more students.
 In the end:
•	Return all valid students each one on a new line:
"*** A student with the username {student username} has successfully finished the course {course_name}!"
•	Afterward, if there are invalid students return them with the following message:
"!!! Invalid course students: {student_1, student_2, student_N}"
Note: Submit only the function in the judge system.
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return the string as described above.
Constraints
•	The arguments will be always before the keyword arguments.
•	Each tuple given will always contain the course id of a student.
•	You will always receive at least one tuple with course id and student.
•	You will always receive at least one valid course id and course name.

'''
def softuni_students(*args, **kwargs):
    students = {}
    courses = {}
    students_by_courses = {}
    non_linked = []
    text = ''
    for curr_arg in args:
        students[curr_arg[1]] = curr_arg[0]

    for curr_course in kwargs.items():
        courses[curr_course[0]] = curr_course[1]

    for name, id_student in students.items():
        if id_student in courses:
            students_by_courses[name] = courses[id_student]
        else:
            non_linked.append(name)

    for k, v in sorted(students_by_courses.items()):
        text += f"*** A student with the username {k} has successfully finished the course {v}!\n"

    if  non_linked:
        text += f"!!! Invalid course students: {', '.join(sorted(non_linked))}"
    return text


# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))
