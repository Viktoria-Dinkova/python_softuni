# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

lines_number = int(input())

courses = []
for line in range(lines_number):
    currant_cours = input()
    courses.append(currant_cours)

print(f'{courses}')