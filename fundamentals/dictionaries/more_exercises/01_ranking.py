# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests".
# Save that data because you will need it later. After that you will receive other type of
# inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
# ere is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests)
# and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in)
# in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names.
# For each user print each contest with the points in descending order. See the examples.
# Input
# •	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
# •	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with same total points!
# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"

test_sequre ={}
students = {}

while True:
    line = input().split(':')
    contest = line[0]
    if len(line) > 1:
        password = line[1]
    if contest == 'end of contests':
        break
    else:
        test_sequre[contest] = password

while True:
    income = input().split('=>')
    submission = income[0]
    if len(income) > 1:
        pass_submission = income[1]
        student = income[2]
        points = int(income[3])
    if submission == 'end of submissions':
        break
    else:
        if submission in test_sequre.keys() and test_sequre[submission] == pass_submission:
            if student not in students.keys():
                students[student] = [submission, points]
            else:
                if submission in students[student]:
                    for i in range(len(students[student])):
                        if students[student] == submission:
                            curr_exam = students[student][i]
                            if points > students[student][i + 1]:
                                students[student][i + 1] = points
                else:
                    students[student].append(submission)
                    students[student].append(points)
rang = {}
for k, v in students.items():
    total_points = 0
    for spec_point in v:
        if isinstance(spec_point, int):
            total_points += spec_point
    rang[k] = total_points

max_points = max(rang.values())
for k, v in rang.items():
    if v == max_points:
        print(f'Best candidate is {k} with total {v} points.\nRanking:')

students = dict(sorted(students.items()))
for key, value in students.items():
    print(f'{key}')
    sorted_value = sorted((value[j] for j in range(len(value)) if j % 2 != 0), reverse=True)
    for sv in sorted_value:
        lesson = value[value.index(sv) - 1]
        score = sv
    # for i in range(0, len(value), 2):
    #     lesson = value[i]
    #     score = value[i + 1]
        print(f'#  {lesson} -> {score}')
