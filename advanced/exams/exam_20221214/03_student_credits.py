"""
Write a function students_credits which receives a different number of strings.
Each string will be in the format: "{course name}-{credits}-{max test points}-{diyan's points}".
Your task is to calculate the credits Diyan manages to get from all courses.
The credits he gets are proportional to his points on the test. For example,
if the credits of a course are 25, and Diyan achieved to get 50 of 100 max test points, he will get 12.5 credits for the course.
Also, you need to keep track of each course and Diyan's credits and sort them in descending order by Diyan's credits.
Finally, return a string on multiple lines containing:
•	Diyan's achievement message:
o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
•	Information for each course and Diyan's credits:
o	"{course name} - {diyan's credits}"
o	Note: Each course data should be on a new line.
•	All credits must be formatted to the first decimal place.

Note: Submit only the function in the judge system
Input
•	There will be no input, just any number of strings with courses data passed to your function
Output
•	The function should return a string in the format described above:
"""


def students_credits(*info):
    diyans_credits = 0
    diyans_courses = {}
    output = ''
    for data in info:
        course_name, max_test_credits, max_test_points, diyans_points = data.split('-')
        diyans_credits = (int(diyans_points) / int(max_test_points))  * int(max_test_credits)

        if course_name not in diyans_courses:
            diyans_courses[course_name] = diyans_credits
        else:
            diyans_courses[course_name] += diyans_credits

    total_credits = sum(cr for cr in diyans_courses.values())

    if total_credits >= 240:
        output += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        output += f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n"

    for course in sorted(diyans_courses.items(), key=lambda item: -item[1]):
        output += f'{course[0]} - {course[1]:.1f}\n'

    return output

