'''
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
'''
from collections import deque
from datetime import datetime, timedelta

robots = input().split(';')
temp_time = input()
beginning = datetime.strptime(temp_time, '%H:%M:%S')
start_time = datetime.strptime(temp_time, '%H:%M:%S')

products = deque([])

command = input()
while command != 'End':
    products.append(command)
    command = input()

while products:
    for curr_robot in robots:
        robot_info = curr_robot.split('-')
        name = robot_info[0]
        processing_time = int(robot_info[1])
        start_time += timedelta(seconds=1)

        diff = (start_time - beginning)
        time_diff = int(diff.total_seconds())

        if time_diff == robots.index(curr_robot) + 1 :
            detail = products.popleft()
            print(f'{name} - {detail} [{start_time.strftime("%H:%M:%S")}]')

        elif time_diff % processing_time == 0:
            detail = products.popleft()
            print(f'{name} - {detail} [{start_time.strftime("%H:%M:%S")}]')

        else:
            products.rotate(-1)

