'''
Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.
For each student print all his/her grades and finally his/her average grade,
formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
'''
count_of_marks = int(input())
students_diary = {}

for _ in range(count_of_marks):
    name, mark = tuple(input().split())

    if name not in students_diary:
        students_diary[name] = [float(mark)]
    else:
        students_diary[name].append(float(mark))

for student, marks_of_current_student in students_diary.items():
    average_grade = sum(marks_of_current_student) / len(marks_of_current_student)
    marks_of_current_student = [str(f'{x:.2f}') for x in marks_of_current_student]
    print(f'{student} -> {" ".join(marks_of_current_student)} (avg: {average_grade:.2f})')