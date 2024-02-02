'''
Sam is on a single lane of total_cars_passed that queue until the light goes green. When it does, they start passing one by one on a
flashing green light and during the free window before the intersecting road's light goes green.
For each second, only one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads
when the free window ends, it will get hit at the first character that is still in the crossroads.
Input
•	On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
•	On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
•	On the following lines, until you receive the "END" command, you will receive one of two things:
	A car - a string containing the model of the car, or
	The command "green" that indicates the start of a green light cycle
A green light cycle goes as follows:
•	During the green light, total_cars_passed will enter and exit the crossroads one by one
•	During the free window, total_cars_passed will only exit the crossroads
Output
•	If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {character_hit}."
•	If everything goes smoothly and you receive an "END" command, print:
"Everyone is safe."
"{total_cars_passed} total total_cars_passed passed the crossroads."
'''
from collections import deque

green_light = int(input())
free_window = int(input())

cars_queue = deque()
crossroad = deque()

crash = False
total_cars_passed = 0

comand = input()
while comand != 'END':

    if comand != 'green':
        cars_queue.append(comand)
    else:
        if cars_queue:
            cur_car = cars_queue.popleft()
            rest_time = green_light - len(cur_car)
            total_cars_passed += 1
            while rest_time > 0:
                if cars_queue:
                    cur_car = cars_queue.popleft()
                    rest_time -= len(cur_car)
                    total_cars_passed += 1
                else:
                    break
            else:
                if free_window < abs(rest_time):
                    index = free_window + rest_time
                    print('A crash happened!')
                    print(f'{cur_car} was hit at {cur_car[index]}.')
                    crash = True
                    break

    comand = input()

if not crash:
        print('Everyone is safe.')
        print(f'{total_cars_passed} total cars passed the crossroads.')