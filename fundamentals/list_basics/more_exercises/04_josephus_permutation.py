# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# •	the list itself - numbers separated by a single space representing the people in the circle
# •	a number k
# People are standing in a circle waiting to be executed.
# Counting begins from the first one in the circle and proceeds from left to right.
# After a specified number of people are skipped, the k person is executed.
# The procedure is repeated with the remaining people, starting with the next person,
# going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

waiting_circle = list(map(int, input().split()))
num_of_executed = int(input())
dead_people = []
counter = 1

while len(waiting_circle) > 0:
    for person in waiting_circle:
        if counter % num_of_executed == 0:
            dead_people.append(person)
        counter += 1

    for dead in dead_people[::-1]:
        if dead in waiting_circle:
            waiting_circle.remove(dead)

print(f'{str(dead_people).replace(" ", "")}')



