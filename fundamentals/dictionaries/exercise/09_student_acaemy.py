# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

count_of_information = int(input())
grades = {}
all_information = []
for information in range(count_of_information * 2):
   all_information.append(input())
for current_grade in range(len(all_information)):
    if current_grade % 2 == 0:
        if all_information[current_grade] not in grades:
            grades[all_information[current_grade]] = [float(all_information[current_grade + 1])]
        else:
            grades[all_information[current_grade]].append(float(all_information[current_grade + 1]))

avarage_grade = {name: sum(mark) / len(mark) for name,mark in grades.items() if sum(mark) / len(mark) >= 4.5}

for k,v in avarage_grade.items():
    print(f'{k} -> {v:.2f}')