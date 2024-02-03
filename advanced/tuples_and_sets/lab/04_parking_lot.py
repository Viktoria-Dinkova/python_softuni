'''
Write a program that:
•	Records a car number for every car that enters the parking lot
•	Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N.
On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}".
The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.
'''

count_of_comands = int(input())
car_set = set()

for _ in range(count_of_comands):
    comand, reg_num = input().split(', ')

    if comand == "IN":
        car_set.add(reg_num)
    elif comand == "OUT":
        car_set.remove(reg_num)

if car_set:
    print(*car_set, sep='\n')
else:
    print('Parking Lot is Empty')