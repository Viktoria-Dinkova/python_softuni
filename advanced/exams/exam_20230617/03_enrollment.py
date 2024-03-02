'''
Write a function called gather_credits that receives information about credits needed, courses, and their credits, and returns the result.
The function will receive a different number of arguments. The arguments will be passed as follows:
•	The first argument will be the number of credits you need - an integer in the range [0, 200];
•	The following arguments will be the tuples with two elements - the first one is the course name (string), and the second one is the course credits (integer);
After receiving the information and calling the function, the program should start tracking the enrollment process:
•	Take the course’s name from each tuple successively and if you need more credits, enroll in it, and proceed to the next one.
•	If a course has already been enrolled in, ignore it, and proceed to the next one.
•	If you have reached the needed number of credits, STOP enrolling!
 In the end:
•	If you’ve managed to gather the needed credits, return the message, including the enrolled courses on a new line:
"Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {course1, course2, …, courseN}"
o	return the courses’ names sorted alphabetically, in ascending order.
•	Otherwise, return the message:
"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return one of the strings shown above depending on the result.
'''


def gather_credits(needed_credits, *info):
    number_of_credits = 0
    courses = info
    enrolled = []
    output = ''

    for course in courses:
        name = course[0]
        credits = int(course[1])

        if name not in enrolled:
            enrolled.append(name)
            number_of_credits += credits
            if number_of_credits >= needed_credits:
                break

    diff = needed_credits - number_of_credits
    if diff <= 0:
        output += f"Enrollment finished! Maximum credits: {number_of_credits}.\nCourses: {', '.join(sorted(enrolled))}"
    else:
        output += f"You need to enroll in more courses! You have to gather {diff} credits more."

    return output


# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
