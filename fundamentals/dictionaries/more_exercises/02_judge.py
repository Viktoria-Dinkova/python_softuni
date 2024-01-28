# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every contest and points of each user:
# •	If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
# •	Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time".
# At that point, you should print each contest in order of input,
# for each contest print the participants ordered by points in descending order,
# then ordered by name in ascending order. After that, you should print individual statistics for every participant
# ordered by total points in descending order, and then by alphabetical order.

info = []
exam = {}
order_contests = []
students = {}
def printing():
    for i in order_contests:
        exit = {}
        for k, v in exam.items():
            if i in v:
                stud = k
                index = exam[k].index(i)
                exit[k] = v[index + 1]

        count = len(exit)
        sort_exit = sorted(exit.items(), key=lambda item: item[1], reverse=True)
        print(f'{i}: {count} participants')
        tup_index = 0
        for tup_element in sort_exit:
            tup_index += 1
            print(f'{tup_index}. {tup_element[0]} <::> {tup_element[1]}')

    print(f'Individual standings:')
    for ke, ve in exam.items():
        score = sum([int(x) for x in ve[1::2]])
        students[ke] += score
    sorted_students = sorted(students.items(), key=lambda it: it[1], reverse=True)
    ss_index = 0
    for s in sorted_students:
        ss_index += 1
        print(f'{ss_index}. {s[0]} -> {s[1]}')


while True:
    enter = input()
    if enter == 'no more time':
        printing()
        break
    else:
        info = enter.split(' -> ')
        username = info[0]
        contest = info[1]
        points = int(info[2])

        if username not in exam:
            exam[username] = [contest, points]
            students[username] = 0
        elif contest not in exam[username]:
            exam[username].append(contest)
            exam[username].append(points)
        else:
            index_of_contest = exam[username].index(contest)
            if exam[username][index_of_contest+1] < points:
                exam[username] = exam[username][:index_of_contest] + exam[username][index_of_contest+2:]
                exam[username].append(contest)
                exam[username].append(points)

        if contest not in order_contests:
            order_contests.append(contest)

