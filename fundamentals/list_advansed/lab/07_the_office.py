# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employees_happiness = list(map(int, input().split()))
factor = int(input())

improved_happiness = [(x * factor) for x in employees_happiness]
avarage_happiness = sum(improved_happiness) / len(improved_happiness)
happy = [x for x in improved_happiness if x >= avarage_happiness]
no_happy = [x for x in improved_happiness if x < avarage_happiness]

if len(happy) >= len(employees_happiness) / 2:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are not happy!')