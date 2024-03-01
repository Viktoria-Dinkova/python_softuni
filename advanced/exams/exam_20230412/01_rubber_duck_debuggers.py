"""
You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a single task.
 The second one represents the number of tasks you’ve given to your programmers.
Your task is to count how many rubber ducks of each type you’ve given to your programmers.
While you have values in the sequences, you need to start from the first value of the programmers time's sequence and multiply them by the last value of the tasks' sequence:
•	If the calculated time is between any of the time ranges below, you give the corresponding ducky and remove the programmer time's value and the tasks' value.
•	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2. Then, move the programmer time's value to the end of its sequence, and continue with the next operation.
Rubber Ducky type	Time needed to earn it
Darth Vader Ducky	0 - 60
Thor Ducky	61 – 120
Big Blue Rubber Ducky	121 - 180
Small Yellow Rubber Ducky	181 - 240

Your task is considered done when the sequences are empty.
Input
•	The first line will represent each programmer’s time to complete a single task – integers, separated by a single space.
•	The second line will represent the number of tasks that should be completed_ducks – integers, separated by a single space.
Output
•	On the first line, you output:
o	"Congratulations, all tasks have been completed_ducks! Rubber ducks rewarded:"
•	On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
o	"Darth Vader Ducky: {count}
Thor Ducky: {count}
Big Blue Rubber Ducky: {count}
Small Yellow Rubber Ducky: {count}"
"""
from collections import deque

time_for_single_task = deque([int(t) for t in input().split()])
numbers_of_tasks = deque([int(nt) for nt in input().split()])

duck_type = {
    'Darth Vader Ducky': [0, 60],
    'Thor Ducky': [61, 120],
    'Big Blue Rubber Ducky': [121, 180],
    'Small Yellow Rubber Ducky': [181, 240]
}

completed_ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while True:
    if not time_for_single_task or not numbers_of_tasks:
        break
    time = time_for_single_task.popleft()
    task = numbers_of_tasks.pop()
    calculated_time = time * task
    for k, v in duck_type.items():
        if v[0] <= calculated_time <= v[1]:
            completed_ducks[k] += 1
            break
    else:
        task -= 2
        numbers_of_tasks.append(task)
        time_for_single_task.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for dn in duck_type:
    for cn, num in completed_ducks.items():
        if dn == cn:
            print(f"{cn}: {num}")